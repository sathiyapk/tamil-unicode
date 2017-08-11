import sys, re
from docx import Document

from dictionary import mapping

if (len(sys.argv) < 2 or not sys.argv[1].endswith(".docx")):
	raise Exception("Usage: python converter.py file_name.docx \n")

input_file = sys.argv[1]

output_file = sys.argv[1][:-5] + "_unicode.txt"

document = Document(input_file)

def convert(text):
	for pattern in mapping:
		text = re.sub(pattern, mapping[pattern], text)
	return text

with open(output_file, 'wb') as fp:
	for paragraph in document.paragraphs:
		fp.write(convert(paragraph.text).encode('utf-8'))
		fp.write("\n".encode('utf-8'))



