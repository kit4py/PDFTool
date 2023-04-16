import PyPDF2
import sys

MERGED_PDF = 'merged'

inputs = sys.argv[1:]  # grab all args besides 1st


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write(f'./results/{MERGED_PDF}.pdf')


if __name__ == '__main__':
    pdf_combiner(inputs)  # give args sys names of pdf files to combine

