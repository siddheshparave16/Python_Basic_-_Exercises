from ebooklib import epub
from bs4 import BeautifulSoup
import warnings

# Suppress warnings about future versions of EbookLib
warnings.filterwarnings("ignore")


def epub_to_text(epub_file):
    book = epub.read_epub(epub_file)
    text = ""
    for item in book.get_items():
        if item.get_type() == 9:  # The type 9 corresponds to ITEM_DOCUMENT
            soup = BeautifulSoup(item.content, 'html.parser')
            text += soup.get_text()
    return text

epub_file = r"C:\Users\Lenovo\Downloads\dokumen.pub_let-us-python-solutions-5th-edition-learn-by-doing-the-python-learning-mantra-solutions-to-all-exercises-5nbsped-9789355511850.epub"
text = epub_to_text(epub_file)

with open("output.txt", "w", encoding="utf-8") as file:
    file.write(text)
