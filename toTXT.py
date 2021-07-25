
import pdftotext
book = input('input file path: ')
# Load your PDF
with open(book, "rb") as f:
    pdf = pdftotext.PDF(f)
 
# Save all text to a txt file.
with open(r"/home/davit/Desktop/book_influence.py/book.txt", 'w') as f:
    f.write("\n\n".join(pdf))
 
 
 
 




