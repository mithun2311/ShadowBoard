from docx import Document


def extract_docx_text(file_path: str) -> str:
    document = Document(file_path)

    paragraphs = [
        p.text
        for p in document.paragraphs
        if p.text.strip()
    ]

    return "\n".join(paragraphs)