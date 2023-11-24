from pdf_reader import extract_text_from_pdf
from openai_messenger import send_message
from document_reader import read_doc

def get_titles_from_text(text):
        query = f"""Analyze the provided JSON-formatted CV or simple text, focusing on the candidate's educational background, professional experience, and skill set. Identify the three most suitable job roles for the candidate based on this information. Output only the job titles, with no additional commentary or details.. 3 titles with comma seperated. below is the c.v text:
                                {text}
                """

        answer = send_message(query)

        print(answer)



while True:
        file_name = input("Enter your file name: ")
        if 'pdf' in file_name:
                text = extract_text_from_pdf(file_name)
                if not text:
                        continue
                get_titles_from_text(text)
        elif 'doc' in file_name or 'docx' in file_name:
                text = read_doc(file_name)
                if not text:
                        continue
                get_titles_from_text(text)
        elif file_name.lower() == 'quit':
                print("Quitting...")
                break
        else:
                print("Only docx, doc and pdf file types are supported!")


