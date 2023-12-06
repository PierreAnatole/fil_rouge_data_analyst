import csv, re
from random import randint

filepath_read="./exo/fil_rouge/bikeshare/cleaned_chicago_city.csv"
filepath_result="./exo/fil_rouge/bikeshare/t_cleaned_chicago_city.csv"

def clean_data(l) :
    # res=re.sub(r"([0-9]{4},|NULL,)([0-9]{2,}|[3-9])", r"\1", l)
    return l

with open(filepath_read,"r",encoding="UTF-8") as filereader :
    with open(filepath_result,"w",encoding="UTF-8") as filewriter :
        i=0
        for line in filereader :
            i+=1
            if i==10000 :
                break
            filewriter.write(clean_data(line))