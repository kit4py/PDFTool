import PyPDF2
import os
from merge import MERGED_PDF

WATERMARK_FILE = 'watermark'
OUTPUT_PDF = 'merged_and_watermarked'


# pdf_combiner(inputs)
template = PyPDF2.PdfReader(open(f'{MERGED_PDF}.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open(f'{WATERMARK_FILE}.pdf', 'rb'))
output = PyPDF2.PdfWriter()


def add_watermark():
    for i in range(len(template.pages)):
        page = template.pages[i]
        page.merge_page(watermark.pages[0])
        output.add_page(page)

        with open(f'./results/{OUTPUT_PDF}.pdf', 'wb') as file:
            output.write(file)


if __name__ == '__main__':
    add_watermark()  # creates watermark on the combined file :)
