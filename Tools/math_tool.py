from langchain.tools import tool
import sympy
from sympy import preview
from fpdf import FPDF

class MathEnvironmentTool:
    @tool("Render Math Equations")
    def render_math(self, equations):
        """Renders mathematical equations as images and returns them."""
        try:
            rendered_equations = []
            for equation in equations:
                expr = sympy.sympify(equation)
                rendered_expr = preview(expr, viewer='BytesIO', euler=False, fontsize=12)
                rendered_equations.append(rendered_expr.getvalue())

            return rendered_equations
        except Exception as e:
            return f"Error rendering math equations: {str(e)}"

    @tool("Create PDF with Math Equations")
    def create_pdf_with_math(self, text, equations):
        """Creates a PDF document with text and rendered mathematical equations."""
        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            for line in text.split("\n"):
                pdf.multi_cell(0, 10, txt=line)

            rendered_equations = self.render_math(equations)

            for equation_image in rendered_equations:
                pdf.add_page()
                pdf.image(equation_image, x=10, y=10, w=180)

            pdf_bytes = pdf.output(dest="S").encode("latin-1")
            return pdf_bytes
        except Exception as e:
            return f"Error creating PDF with math equations: {str(e)}"