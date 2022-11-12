import requests
from bs4 import BeautifulSoup
import pandas as pd
import time





start = time.perf_counter()

#3 Head Data
lst_set = []
lst_total = []
lst_percent = []
#7 Detils Data
lst_name = []
lst_school = []
lst_educational_management = []
lst_student_status = []
lst_kind_of_educational = []
lst_division = []
#13 Degree
lst_arabic = []
lst_first_forign_language = []
lst_second_forign_language = []
lst_pure_mathematics = []
lst_history = []
lst_geography = []
lst_philosophy_logic = []
lst_psychology_sociology = []
lst_chemistry = []
lst_biology = []
lst_geology_environmental_sciences = []
lst_applied_mathematics = []
lst_physics  = []
#3 Extera
lst_religion = []
lst_educational_nationality = []
lst_statistics_economics = []
#input
start_set = int(input("Enter the start set number: "))
end_set = int(input("Enter the end set number: "))
start_name = start_set
lst_valid_sets = []
lst = []
lst_error = []
count = 0


while start_set <= end_set:  
    start_set += 1
    lst.append(start_set-1)
print(lst)


for i in lst:
    try:
        headers = {
            'referer': 'https://shbabbek.com/natega',
        }

        response = requests.get(f'https://shbabbek.com/natega/{str(i)}', headers=headers)

        #print(response.text)
        #print(response)

        soup = BeautifulSoup(response.content, "html.parser")
        #print(soup)
        
        #3 Head Data

        set_number = soup.find(attrs={'class': 'table table-striped table-customize'}).find_all('td')[1].get_text() 
        print("Valid set number")
        lst_valid_sets.append(i)
    except:
        print("invalid set number")

print(lst_valid_sets)


if len(lst_valid_sets) > 0:
    try:
        for w in lst_valid_sets:
            
            headers = {
                'referer': 'https://shbabbek.com/natega',
            }

            response = requests.get(f'https://shbabbek.com/natega/{str(w)}', headers=headers)

            #print(response.text)
            #print(response)

            soup = BeautifulSoup(response.content, "html.parser")
            #= soup.select('')[0].text.strip()
            set_code = soup.select('div.row:nth-child(4) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)')[0].text.strip()
        #     net_code = set_code.find('"\n"')
        #     setset = set_code[:net_code]
        #     print(setset[1:])
        #    lst_set.append(setset[1:])
        #    lst_set.append(set_code[1:-1])
        #    lst_set.append(set_code.strip())
            lst_set.append(set_code)
            name = soup.select('div.row:nth-child(4) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(2)')[0].text.strip()
            lst_name.append(name)
            total_marks = soup.select('div.row:nth-child(4) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(6) > td:nth-child(2) > strong:nth-child(1)')[0].text.strip()
            lst_total.append(total_marks)    
            percent = soup.select('div.row:nth-child(4) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(7) > td:nth-child(2) > strong:nth-child(1)')[0].text.strip()
            p = percent.find("%")
            lst_percent.append(percent[:p])
            school = soup.select('div.row:nth-child(4) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(2) > a:nth-child(1)')[0].text.strip()
            lst_school.append(school)
            managment = soup.select('div.row:nth-child(4) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(2) > a:nth-child(1)')[0].text.strip()
            lst_educational_management.append(managment)
            status = soup.select('div.row:nth-child(4) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(9) > td:nth-child(2)')[0].text.strip()
            lst_student_status.append(status)
            kind = soup.select('div.row:nth-child(4) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(8) > td:nth-child(2)')[0].text.strip()
            lst_kind_of_educational.append(kind)
            division = soup.select('div.row:nth-child(4) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(5) > td:nth-child(2)')[0].text.strip()
            lst_division.append(division)
            arabic = soup.select('div.row:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)')[0].text.strip()
            lst_arabic.append(arabic)
            first_forign_language = soup.select('div.row:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(2)')[0].text.strip()  
            lst_first_forign_language.append(first_forign_language)
            second_forign_language = soup.select('div.row:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(2)')[0].text.strip()  
            lst_second_forign_language.append(second_forign_language)
            pure_mathematics = soup.select('div.row:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(2)')[0].text.strip()  
            lst_pure_mathematics.append(pure_mathematics)
            history = soup.select('div.row:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(5) > td:nth-child(2)')[0].text.strip()  
            lst_history.append(history)
            geography = soup.select('div.row:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(6) > td:nth-child(2)')[0].text.strip()  
            lst_geography.append(geography)
            philosophy_logic = soup.select('div.row:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(7) > td:nth-child(2)')[0].text.strip()  
            lst_philosophy_logic.append(philosophy_logic)
            psychology_sociology = soup.select('div.row:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(8) > td:nth-child(2)')[0].text.strip()  
            lst_psychology_sociology.append(psychology_sociology)
            chemistry = soup.select('div.row:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(9) > td:nth-child(2)')[0].text.strip()  
            lst_chemistry.append(chemistry)
            biology = soup.select('div.row:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(10) > td:nth-child(2)')[0].text.strip()  
            lst_biology.append(biology)
            geology_environmental_sciences = soup.select('div.row:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(11) > td:nth-child(2)')[0].text.strip()  
            lst_geology_environmental_sciences.append(geology_environmental_sciences)
            applied_mathematics = soup.select('div.row:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(12) > td:nth-child(2)')[0].text.strip()  
            lst_applied_mathematics.append(applied_mathematics)
            physics = soup.select('div.row:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(13) > td:nth-child(2)')[0].text.strip()  
            lst_physics.append(physics)
            #3 Extera
            religion = soup.select('div.row:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(15) > td:nth-child(2)')[0].text.strip() 
            lst_religion.append(religion)
            educational_nationality = soup.select('div.row:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(16) > td:nth-child(2)')[0].text.strip()  
            lst_educational_nationality.append(educational_nationality)
            statistics_economics = soup.select('div.row:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(17) > td:nth-child(2)')[0].text.strip()  
            lst_statistics_economics.append(statistics_economics)    

    except:
        print(f"Error happen in {w}")    
        lst_error.append(w)


    a =(
        {'set_number': lst_set,'name': lst_name, 'school': lst_school,
        'educational_management': lst_educational_management, 'student_status': lst_student_status,
        'kind_of_educational': lst_kind_of_educational, 'division': lst_division, 'arabic': lst_arabic, 'first_forign_language': lst_first_forign_language,
        'second_forign_language': lst_second_forign_language, 'pure_mathematics': lst_pure_mathematics, 'history': lst_history,
        'geography': lst_geography, 'philosophy_logic': lst_philosophy_logic, 'psychology_sociology': lst_psychology_sociology,
        'chemistry': lst_chemistry, 'biology': lst_biology, 'geology_environmental_sciences': lst_geology_environmental_sciences,
        'applied_mathematics': lst_applied_mathematics, 'physics': lst_physics, 'religion': lst_religion, 'educational_nationality': lst_educational_nationality,
        'statistics_economics': lst_statistics_economics, 'totla_degree': lst_total, 'percentage':lst_percent})
    print(a)
    df = pd.DataFrame.from_dict(a, orient='index')
    df = df.transpose()
    df.to_csv(f'shabeak_thanwey_{str(start_name)}_to_{str(end_set)}_data.csv', encoding="utf-8-sig", index=False)
    if len(lst_error) > 0:        
        file_name = open(f"{str(start_name)}_to_{str(end_set)}_Erorr.txt", "w", encoding="utf-8")
        for e in lst_error:
            file_name.write("\n1-"+f"{e}")
else:
    print("Error no valid data")
    file_name = open(f"{str(start_name)}_to_{str(end_set)}_No_valid_data.txt", "w", encoding="utf-8")
    file_name.write("\n1-"+f"{str(count)}")


finish = time.perf_counter()
print('Finished in {} secound'.format(round(finish-start, 2)))
