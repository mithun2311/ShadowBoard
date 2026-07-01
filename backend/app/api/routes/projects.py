from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import get_current_user
from app.db.models.project import Project
from app.db.models.user import User
from app.db.session import get_db
from app.schemas.project import (
    ProjectCreate,
    ProjectUpdate,
    ProjectResponse,
)
from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import select
router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)

@router.post(
    "",
    response_model=ProjectResponse,
)
async def create_project(
    request: ProjectCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    project = Project(
        owner_id=current_user.id,
        title=request.title,
        description=request.description,
        industry=request.industry,
        company_stage=request.company_stage,
        decision_type=request.decision_type,
    )

    db.add(project)

    await db.commit()

    await db.refresh(project)

    return project

@router.get(
    "",
    response_model=list[ProjectResponse],
)
async def list_projects(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    result = await db.execute(
        select(Project).where(
            Project.owner_id == current_user.id
        )
    )

    projects = result.scalars().all()

    return projects

@router.get(
    "/{project_id}",
    response_model=ProjectResponse,
)
async def get_project(
    project_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

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

    return project

@router.put(
    "/{project_id}",
    response_model=ProjectResponse,
)
async def update_project(
    project_id: UUID,
    request: ProjectUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

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

    update_data = request.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(project, field, value)

    await db.commit()
    await db.refresh(project)

    return project

@router.delete(
    "/{project_id}",
)
async def delete_project(
    project_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

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

    await db.delete(project)
    await db.commit()

    return {
        "message": "Project deleted successfully"
    }

