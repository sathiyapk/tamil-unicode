# Tamil Unicode Text Converter:

Tamil Nadu govenment demands e-documents in a specific non-unicode font, which may not come in handy to achieve better/ needed formating.

The converter.py in this repository reads tamil texts written in the government specified font from a .docx file and save the unicode texts in a separate .txt file. This would save you the trouble of rewriting the entire document in an unicode font once again. 

# Dependencies
The converter uses python docx library for reading the *.docx* file. Install the needed dependency using the following command:

```bash
pip install python-docx
```

# Usage:

```bash
>>>python converter.py input_file_name.docx
```
