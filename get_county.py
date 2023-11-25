from openai_messenger import send_message
import pandas as pd
import os

# read excel/csv file and get city or town
def get_city_names(file_name):
    
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
    
    return df['City'].to_list()



def get_county_name(city_or_town):
    query = f"""City or town list: '{city_or_town}'
           County names list:"""
    answer = send_message(query)

    print(answer)


while True:
        file_name = input("Enter your City excel/csv file name: ")
        if file_name.lower() == 'quit':
                print("Quitting...")
                break
        
        city_or_town_names = get_city_names(file_name)
        if city_or_town_names!=[] or city_or_town_names == None:
            get_county_name(city_or_town_names)

        




