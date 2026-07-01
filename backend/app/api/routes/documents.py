from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
    HTTPException,
)

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import get_current_user
from app.db.models.document import Document
from app.db.models.project import Project
from app.db.models.user import User
from app.db.session import get_db
from app.schemas.document import DocumentResponse
from app.utils.file_storage import save_uploaded_file

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

@router.post(
    "/upload/{project_id}",
    response_model=DocumentResponse,
)
async def upload_document(
    project_id: UUID,
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    allowed = {
        "pdf",
        "docx",
        "pptx",
        "txt",
    }

    extension = file.filename.split(".")[-1].lower()

    if extension not in allowed:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type",
        )

    result = await db.execute(
        select(Project).where(
            Project.id == project_id,
            Project.owner_id == current_user.id,
        )
    )

    project = result.scalar_one_or_none()

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    filename, path = await save_uploaded_file(file)

    document = Document(
        project_id=project.id,
        filename=file.filename,
        file_path=path,
        file_type=extension,
    )

    db.add(document)

    await db.commit()

    await db.refresh(document)

    return document