from PyPDF2 import PdfReader     #used for extracting and opening a Pdf
from reportlab.pdfgen import canvas  #used for creating and copying content in a pdf 
from reportlab.lib.units import inch


#using a dummy pdf with questions
pdf_path1 = "./A.pdf"
pdf_reader = PdfReader(pdf_path1)

#the output(form preview) pdf
output_pdf_path = "created.pdf"

c = canvas.Canvas(output_pdf_path)
c.setFont("Helvetica", 12)

line_height = 0.4 * inch
y = 10 * inch

#extracting the data from the pdf to store it in a dictionary
preview_form ={}
for page in pdf_reader.pages:
    page_content = page.extract_text()
    '''lines is the list of all the questions from the PDF'''
    lines = page_content.strip().split('\n')
    lines = [question for question in lines if question.strip()]  # Filter out empty lines
 

    for question in lines:
        response = input(f'{question} ')
        preview_form[question] = response

'''To redirect the client to a new set of question based on the response of the last question. Using questions from PDF B .
PS: This is just an example and will be changed in the final evaluation'''
'''The algorithm/function used here is the same as used above. Hence the code may seem repetitive but will be changed later'''       
if preview_form[lines[len(lines)-1]] == "Yes":
    pdf_path1 = "./B.pdf"
    pdf_reader = PdfReader(pdf_path1)

    for page in pdf_reader.pages:
        page_content = page.extract_text()
        lines = page_content.strip().split('\n')
        lines = [question for question in lines if question.strip()]  # Filter out empty lines

        for question in lines:
            response = input(f'{question} ')
            preview_form[question] = response
else:
    '''Else we use PDF C for the people with response other than Yes. Again the code/function used is the same '''
    pdf_path1 = "./C.pdf"
    pdf_reader = PdfReader(pdf_path1)

    for page in pdf_reader.pages:
        page_content = page.extract_text()
        lines = page_content.strip().split('\n')
        lines = [question for question in lines if question.strip()]  # Filter out empty lines

        for question in lines:
            response = input(f'{question} ')
            preview_form[question] = response

'''Copying the entire dictionary as the form of content in a new pdf (that contains the client's data)'''
for question in preview_form :   
    c.drawString(1 * inch, y, f'{question}: {preview_form[question]}')
    y -= line_height

c.save()


'''Printing the final preview form for the user validation '''
#previewing the entire PDF:
new_pdf_path = "./created.pdf"
pdf_reader = PdfReader(new_pdf_path)
for page in pdf_reader.pages:
    print(page.extract_text())
