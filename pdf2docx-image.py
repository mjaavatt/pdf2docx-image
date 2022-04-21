from docx import Document
from docx.shared import Mm
import sys
import glob
import pathlib

document = Document()
section = document.sections[0]
section.page_height = Mm(297)
section.page_width = Mm(210)
section.left_margin = Mm(25.4)
section.right_margin = Mm(25.4)
section.top_margin = Mm(25.4)
section.bottom_margin = Mm(25.4)
section.header_distance = Mm(12.7)
section.footer_distance = Mm(12.7)

filename = sys.argv[1]

p = pathlib.Path(filename)
globpath = p.parents[0] / (p.stem + '*' + p.suffix)
filenames = glob.glob(str(globpath))

for i in filenames:
    document.add_picture(i, width=section.page_width*0.8)

document.save('demo.docx')
