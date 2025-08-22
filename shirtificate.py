
from fpdf import FPDF

def main():
    create(input("Name: "))

def create(s: str) -> None:
    pdf = FPDF()
    pdf.add_page()
    pdf.image("shirtificate.png", 15, 70, int(0.3*593), int(0.3*592))
    pdf.set_font("helvetica", style = "B", size = 45)
    pdf.cell(0, 50, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align = "C")
    pdf.set_font("helvetica", style = "B", size = 20)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, 140, f"{s} CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align = "C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
