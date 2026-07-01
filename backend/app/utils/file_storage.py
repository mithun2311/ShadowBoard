import os
import uuid
import aiofiles
from fastapi import UploadFile

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


async def save_uploaded_file(file: UploadFile):

    extension = file.filename.split(".")[-1]

    unique_filename = f"{uuid.uuid4()}.{extension}"

    file_path = os.path.join(
        UPLOAD_DIR,
        unique_filename,
    )

    async with aiofiles.open(file_path, "wb") as out_file:
        while content := await file.read(1024 * 1024):
            await out_file.write(content)

    return unique_filename, file_path