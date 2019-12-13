import PyPDF2
import textract
# import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# nltk.download('stopwords')

filename = "Berita Acara pt1.pdf"

pdfFileObj = open(filename, "rb")

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

num_pages = pdfReader.numPages
count = 0
text = ""

text = textract.process(filename, method="tesseract", languange="eng")
# while count < num_pages:
#     pageObj = pdfReader.getPage(count)
#     count += 1
# text += pageObj.extractText()

# if text != "":
#     print("masuk if")
#     text = text

# else:
#     print("masuk else")

text = text.decode("utf-8")

tokens = word_tokenize(text)

punctuations = ['(', ')', ';', ':', '[', ']', ',']

stop_words = stopwords.words('english')

keywords = [
    z for z in tokens if not z in stop_words and not z in punctuations]

print(text)
print("====================================================================================================================")
print(tokens)
print("====================================================================================================================")
print(keywords)

file = open('result.txt', 'w')
file.write(text)
file.close()
