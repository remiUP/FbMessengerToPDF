from fpdf import FPDF
import json
from urllib.request import urlopen
import os
import cgi
import sys
# set system encoding to unicode
import sys
pdf = FPDF()
pdf.add_page()
pdf.add_font('DejaVu', '', "C:\\Users\\remiUP\\AppData\\Local\\Microsoft\\Windows\\Fonts\\DejaVuSansCondensed.ttf", uni=True)
pdf.set_font('DejaVu','',12)
pdf.multi_cell(0,10,txt="Salut c'est rémi, aïeux de jsp :à) 12 \u1f923")
pdf.output("title.pdf")
