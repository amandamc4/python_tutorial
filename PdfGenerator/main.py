from fpdf import FPDF
import pandas as pd

# Orientation P portrait or L landscaping
# pdf = FPDF(orientation='P', unit="mm",format='A4')
#
# pdf.add_page()
#
# #ln is a breakline, means next cell will be on next line
# pdf.set_font(family="Times", style="B", size=12)
# pdf.cell(w=0, h=12, txt="Hello There", align="L", ln=1, border=1)
# pdf.cell(w=0, h=12, txt="Wooow", align="L", ln=1, border=1)
#
# pdf.output('output.pdf')

pdf = FPDF(orientation='P', unit="mm",format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 21, 200, 21)

    # set footer
    pdf.ln(265) #adds breaklines for 265mm
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="L", ln=1)

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

pdf.output("output.pdf")

