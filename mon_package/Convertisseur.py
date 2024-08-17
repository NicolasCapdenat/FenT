import PyPDF2

def pdf_to_text(pdf_path):
    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PdfReader object instead of PdfFileReader
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        

        # Initialize an empty string to store the text
        text = ''

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    new_txt=pdf_path.replace(".pdf",".txt")
    new_txt=new_txt.replace("Fiches_sanitaire\\","cache\\")
    # Write the extracted text to a text file
    with open(new_txt, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)
