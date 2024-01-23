# from pdf2docx import Converter
# from pdf2docx import parse

# from docx import Document
import argostranslate.package
import argostranslate.translate


def download_argos_language(from_code, to_code):
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())


def get_available_languages():

    available_packages = argostranslate.package.get_available_packages()
    return {'input': { package.from_code: package.from_name for package in available_packages},
            'output': { package.to_code: package.to_name for package in available_packages}}


def get_installed_languages():
    installed_packages = argostranslate.package.get_installed_packages()
    return {'input': { package.from_code: package.from_name for package in installed_packages},
            'output': { package.to_code: package.to_name for package in installed_packages}}



def argos_translate(input_text, input_lang, output_lang):
    print(input_text)
    translatedText = argostranslate.translate.translate(input_text, input_lang, output_lang)
    return translatedText


docx= "C:/Users/zales/Documents/BSB4/PWC/5. Translation of PDF/hope.docx"
# myPdf= "C:/Users/zales/Documents/BSB4/PWC/5. Translation of PDF/YO.pdf"
# sup = "C:/Users/zales/Documents/BSB4/PWC/5. Translation of PDF/letter.pdf"

# def convert_pdf_doc(pdf):
#     docx= "C:/Users/zales/Documents/BSB4/PWC/5. Translation of PDF/test-1-21.docx"
#     cv = Converter(pdf)
#     cv.convert(docx)

#     cv.close()


# def convert_doc_pdf(doc):
#     pdf = "C:/Users/zales/Documents/BSB4/PWC/5. Translation of PDF/Prague.pdf"
#     cv = Converter(docx)
#     cv.convert(pdf)
#     cv.close()

# def loop_doc():

#     myDoc = "C:/Users/zales/Documents/BSB4/PWC/5. Translation of PDF/test-1-21.docx"
#     docs = Document(myDoc)
#     doc_text = list(set([ p.text for p in docs.paragraphs]))
#     doc_text.remove('')
#     for paragraph in docs.paragraphs:
#         print(paragraph.text)

#     for paragraph in docs.paragraphs:
#         # Replace consecutive spaces with a single space
#         paragraph.text = ' '.join(paragraph.text.split())

#     # Save the modified document
#     docs.save(myDoc)

#     for paragraph in docs.paragraphs:
#         print(paragraph.text)


# def translate_text(docx, ):
   
#   from_code = "en"
#   to_code = "ru"
  
#   docs = Document(docx)
#   doc_text = list(set([ p.text for p in docs.paragraphs]))
#   doc_text.remove('')
  
#   for paragraph in docs.paragraphs:

#     text = paragraph.text
      
#     if text in doc_text:  
#         if "•" in text:
#             translation = argostranslate.translate.translate(text, from_code, to_code)
#             paragraph.text = translation
#         else:
        
#             runs = iter(paragraph.runs)
#             counter = 0
            
#             for run in runs:
#                 if(counter == 0):
#                     run.text = argostranslate.translate.translate(text, from_code, to_code)
#                 else:
#                     run.text = ''
#                 counter+= 1
#                 #print(run.text)
#                 #print("Counter: ", counter)
#                 print("style: ", run.font.size)
#                 if "\t" in run.text:
#                     print("tab found!!!")
            
#     for table in docs.tables:
#         for row in table.rows:
#             for cell in row.cells:
#                 for parag in cell.paragraphs:
#                     for run in parag.runs:
#                         run.text = argostranslate.translate.translate(run.text, from_code, to_code)
                
  
#   docs.save(docx)


if __name__ == "__main__":
  
#   convert_pdf_doc("C:/Users/zales/Documents/BSB4/PWC/5. Translation of PDF/letter.pdf")
#   loop_doc()
  #replacement_option()

#   translate_text(docx)
    
  #convert_doc_pdf(docx)
    

    # available_packages = argostranslate.package.get_available_packages()


    # print({ package.from_code: package.from_name for package in available_packages})
    # print({ package.to_code: package.to_name for package in available_packages})


    # print("starting translation...")
    # translatedText = argostranslate.translate.translate("Hello World! My name is Olivia, I am a student. I would like a job, please. Give me your money.", "en", "es")
    # print(translatedText)

    installed_languages = argostranslate.package.get_installed_packages()

    # Print the list of installed languages
    print(installed_languages)