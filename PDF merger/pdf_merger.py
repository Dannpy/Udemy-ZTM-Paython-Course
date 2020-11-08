import PyPDF2
import os


input_dir_name = "Input PDFs"
output_dir_name = "Merged PDF"

if not os.path.isdir(input_dir_name):
    os.mkdir(input_dir_name)

if not os.path.isdir(output_dir_name):
    os.mkdir(output_dir_name)

merger = PyPDF2.PdfFileMerger()
for pdf in os.listdir(input_dir_name):
    merger.append(input_dir_name+"/"+pdf)
merger.write(output_dir_name+"/""Merged PDF.pdf")
