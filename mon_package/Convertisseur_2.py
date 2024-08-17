from pypdf import PdfReader

def pdf_reader(pdf_path):
    reader=PdfReader(pdf_path)
    number_of_pages=len(reader.pages)
    #print(number_of_pages)
    i=0
    text=""
    while i<number_of_pages:
        page=reader.pages[i]
        text=text+page.extract_text()
        i=i+1

    new_txt=pdf_path.replace(".pdf",".txt")
    new_txt=new_txt.replace("Fiches_sanitaire\\","cache\\")
    # Write the extracted text to a text file
    with open(new_txt, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)
    