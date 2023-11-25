from openai_messenger import send_message
import pandas as pd
import os
import math

title_column_name = 'Title From File'
salary_column_name = 'New Salary'
description_column_name = 'Description'
column_names = [title_column_name, salary_column_name, description_column_name]

def get_experience_level(csv_data):
    query = f"""Using the 'Job Title', 'Salary' value and the 'Job Description' provided in csv format, 
                identify the 
                required minimum level of experience for this position. Only state the appropriate 
                experience level, without additional explanation or analysis. The experience levels 
                are: 'No Experience', '0-3 years (Beginner)', '4-7 years (Mid)', '8-10 years (Experienced)',
                '11+ years (Professional/Expert)'. Exclude all other information except for the 
                specified experience level.
                Output Example: Experience level
                below is data available in csv format. return each row data in csv format for all rows.
                {csv_data}
                """
    answer = send_message(query)

    return answer


def split_long_text(new_dataframe):

    # Maximum token length allowed for the model
    max_length = 5  # Replace with the maximum token length supported by your model
    counter = 0
    iters = math.ceil(len(new_dataframe) / max_length)
    return get_experience_level(new_dataframe)
    # if math.ceil(len(new_dataframe))  <= 5:
    # results = []
    # for i in range(iters):
    #     data = new_dataframe.iloc[counter:max_length-1]
    #     response = get_experience_level(data)
    #     print(f"response: {counter}-{max_length}")
    #     print(response)
    #     results.append(response)
    #     counter += 5
    #     max_length += 5

    # return results





# read excel/csv file and get city or town
def get_data_columns(file_name):
    
    if not os.path.exists(file_name):
        print(f"'{file_name}' does not exists. Please try again!")
        return None
    
    if 'csv' in file_name:
        df = pd.read_csv(file_name)
    elif file_name in ['xlxs', 'xls']:
        df = pd.read_excel(file_name)
    else:
        print("This file type is not supported!")
        return None
    new_dataframe = df[column_names]
    return new_dataframe

while True:
        file_name = input("Enter your excel/csv file name: ")
        if file_name.lower() == 'quit':
                print("Quitting...")
                break
        
        csv_data = get_data_columns(file_name)
        if csv_data is not None and not csv_data.empty:
            data = split_long_text(csv_data)
            print(data)






