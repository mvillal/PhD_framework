import sys
import os
from pathlib import Path
from markitdown import MarkItDown
# marker-pdf is often used via CLI or specific imports, we'll try markitdown first as it's more general.

def process_pdf(pdf_path: str, output_path: str = None):
    """
    Converts a PDF file to Markdown using MarkItDown.
    """
    md = MarkItDown()
    try:
        result = md.convert(pdf_path)
        content = result.text_content
        
        if output_path:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Successfully converted {pdf_path} to {output_path}")
        else:
            # Print to stdout if no output path provided
            print(content)
            
    except Exception as e:
        print(f"Error processing PDF {pdf_path}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pdf_processor.py <pdf_path> [output_path]")
        sys.exit(1)
    
    path = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else None
    process_pdf(path, out)
