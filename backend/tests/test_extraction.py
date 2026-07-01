from app.services.extraction.extractor import extract_document

text = extract_document(
    "uploads/825ade6b-d4d6-441c-9931-03bb5431c539.pdf"
)

print(text)