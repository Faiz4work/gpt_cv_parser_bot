from pdf_reader import extract_text_from_pdf
from openai_messenger import send_message
from document_reader import read_doc

def get_years_of_experience(text, job_title):
        query = f"""
                {text}

                Given the CV or text data containing details about the {job_title} work experience, extract the total years of experience as a numeric value. If the experience is less than 1 year, return '0'. If no experience is available or less than 1 year, return 'Beginner'. Otherwise, return only the numeric value representing the total years of experience (e.g., 1, 2, 3, etc.). Ensure the output contains only the numeric value without any accompanying text or explanation.
        """
        answer = send_message(query)

        print(answer)



while True:
        file_name = input("Enter your file name: ")
        if 'pdf' in file_name:
                text = extract_text_from_pdf(file_name)
                if not text:
                        continue
                job_title = input("Enter job title: ")
                get_years_of_experience(text, job_title)
        elif 'doc' in file_name or 'docx' in file_name:
                text = read_doc(file_name)
                if not text:
                        continue
                job_title = input("Enter job title: ")
                get_years_of_experience(text, job_title)
        elif file_name.lower() == 'quit':
                print("Quitting...")
                break
        else:
                print("Only docx, doc and pdf file types are supported!")