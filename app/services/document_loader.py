from pathlib import Path

import pdfplumber

class UnsupportedFileTypeError(Exception):
    """Raised when the uploaded document type is not supported."""


class DocumentNotFoundError(Exception):
    """Raised when the document path does not exist."""


def load_txt_file(file_path: Path) -> str:
    """
    Load text content from a TXT file.
    """

    return file_path.read_text(encoding="utf-8")


def load_pdf_file(file_path: Path) -> str:
    """
    Extract text content from a PDF file.

    Note;
    This works for text-based PDFs
    Scanned image PDFs would need OCR support, which can be added later
    """

    extracted_pages: list[str] = []

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text() or ""
            extracted_pages.append(page_text)
    
    return "\n".join(extracted_pages).strip()


def load_document(file_path: Path) -> str:
    """
    Load document content from TXT or PDF files.
   
    Args:
        file_path: Path to input FNOL document.

    Returns:
        Extracted text from the document.

    Raises:
        DocumentNotFoundError: If the file does not exist at the given path.
        UnsupportedFileTypeError: If the file type is not supported (not TXT or PDF).
        ValueError: If the file is empty or contains only whitespace.

    """

    path = Path(file_path)

    if not path.exists():
        raise DocumentNotFoundError(f"Document not found at path: {file_path}")
    
    suffix = path.suffix.lower()

    if suffix == ".txt":
        content = load_txt_file(path)
    elif suffix == ".pdf":
        content = load_pdf_file(path)
    else:
        raise UnsupportedFileTypeError(f"Unsupported file type: {suffix}. Only .txt and .pdf are supported.")
    
    
    cleaned_content = content.strip()

    if not cleaned_content:
        raise ValueError(f"The document at {file_path} is empty or contains only whitespace.")
    
    return cleaned_content