from os import path
import pandas as pd
import json

def excelToJson(path, sheet=False):
    if sheet:
        fileContent = pd.read_excel(path,sheet)
    else:
        fileContent = pd.read_excel(path)
    funkyTown = []
    for i in fileContent.index:
        record = fileContent.iloc[i].to_json()
        record = json.loads(record)
        funkyTown.append(record)
    return funkyTown


def writeToJson(dictionary):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=4)
