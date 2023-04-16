# PDFTool
Merge PDF files into one PDF file and add watermark to each page


Installation:
1. git clone
2. cd JPGtoPNG-Converter/
3. python3 -m venv venv # create virtual environment
4. . venv/bin/activate (.fish # if you're using fish)
5. python3 install -r requirements.txt


Example:

- pdf1, pdf2, pdf3 single files 
- in the /results you can see 
- merged PDF and merged_watermaked PDF 


Usage:
1. Open Directory and add your PDFs to merge (delete example files)
2. Run: python3 merge.py pdfname1.pdf pdfname2.pdf pdfname3.pdf etc...
3. Merged PDF was saved to: ./results/merged.pdf

4. Add watermark.pdf to the rest of the files in main directory 
5. Run: python3 watermark.py
6. Watermarked PDF was saved to: ./results/merged_and_watermarked.pdf
