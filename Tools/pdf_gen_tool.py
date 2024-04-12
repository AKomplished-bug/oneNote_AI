from langchain.tools import tool
from fpdf import FPDF

class PDFCreationTool:
    @tool("Create PDF from Text and Images")
    def create_pdf(self, text, images):
        """Create a PDF document from given text and images"""
        try:
            pdf = FPDF()
            for line in text.split("\n"):
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                pdf.multi_cell(0, 10, txt=line)
            
            for image_path in images:
                pdf.add_page()
                pdf.image(image_path, x=10, y=10, w=180)
            
            pdf_bytes = pdf.output(dest="S").encode("latin-1")
            return pdf_bytes
        except Exception as e:
            return f"Error creating PDF: {str(e)}"