from pathlib import Path

from app.services.extraction.pdf import extract_pdf_text
from app.services.extraction.docx import extract_docx_text

from app.services.extraction.txt import extract_txt_text


def extract_document(file_path: str):

    extension = (
        Path(file_path)
        .suffix
        .lower()
        .replace(".", "")
    )

    if extension == "pdf":
        return extract_pdf_text(file_path)

    if extension == "docx":
        return extract_docx_text(file_path)

    

    if extension == "txt":
        return extract_txt_text(file_path)

    raise ValueError(
        f"Unsupported file type: {extension}"
    )
