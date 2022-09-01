import pandas as pd
import glob

def load_excel_to_dict():
    tr = pd.read_excel('redash_localization_words.xlsx')
    return tr.set_index('Text to translate')['Translation'].to_dict()

def wrap_as_variable(str):
    return '"' + str + '"'

def wrap_as_tag(str):
    return '>' + str + '<'

def localize(dict):
    file_path = glob.glob('app.*.js')[0]
    with open(file_path) as file:
        file_string = file.read()
        
    for key, value in dict.items():
        if " " in key:
            file_string = file_string.replace(key, value.replace("'","\\'"))
        file_string = file_string.replace(wrap_as_tag(key), wrap_as_tag(value.replace("'","\\'")))

    with open(file_path, 'w') as out:
        out.write(file_string)

translations = load_excel_to_dict()
localize(translations)
