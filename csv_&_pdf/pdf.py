import PyPDF2

f = open("pypdf2.pdf", "rb")

pdf_reader = PyPDF2.PdfReader(f)

num_pages = len(pdf_reader.pages)

page_one = pdf_reader.pages[0]
print(page_one.extract_text())

f.close()

f = open("pypdf2.pdf", "rb")

pdf_reader = PyPDF2.PdfReader(f)
page_one = pdf_reader.pages[0]

pdf_writer = PyPDF2.PdfWriter()
pdf_writer.add_page(page_one)

pdf_output = open("new.pdf", "wb")
pdf_writer.write(pdf_output)
f.close()