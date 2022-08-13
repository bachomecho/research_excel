import os, re, time
import pandas as pd
from PyPDF2 import PdfReader
from custom_modules.exceptionhandler import escape_xlsx_string


def extract_text_func(reader)-> str:
    text = str()
    for page in range(round(len(reader.pages)/2), len(reader.pages)):
        text += reader.pages[page].extract_text()
    return text


def conclusion_index_search(pure_text):
    conclusion_list = ["Conclusion", "Conclusions", "CONCLUSION", "CONCLUSIONS"]
    for i in range(len(pure_text.split())):
        for j in conclusion_list:
            if re.search(j, pure_text.split()[i]):
                return i


def conclusion_text(pure_text, start_number:int) -> str:
    c_text_list: list[str] = list()

    len_number = len(pure_text.split())

    for k in range(start_number, len_number):
        c_text_list.append(pure_text.split()[k])

    return " ".join(c_text_list)


def reference_index_search(conc_text):
    ref_list = ["Acknowledgment", "ACKNOWLEDGMENT", "REFERENCES", "References"]
    for i in range(len(conc_text)-1):
        for j in ref_list:
            if re.search(j, conc_text.split()[i]):
                return i

def run():
    path = input("SPECIFY FOLDER WITH YOUR STUDIES: ") + '\\'

    start_time = time.time() # used to measure runtime

    name_list: list[str] = list()
    size_list: list[float] = list()
    conc_list: list[str] = list()

    with os.scandir(path) as files:
        for file in files:
            reader = PdfReader(path + file.name)

            name_list.append(file.name.split('.')[0])
            size_list.append(round(os.path.getsize(path+file.name)/1024/1024, 2))

            pure_text = extract_text_func(reader)
            start_number = conclusion_index_search(pure_text)
            try:
                conc_text = conclusion_text(pure_text, start_number)
                end_number = reference_index_search(conc_text)
                
                conc_text = escape_xlsx_string(conc_text)
                conc_text = conc_text.split()[:end_number]

                conc_list.append(" ".join(conc_text))
                print(f"[+] FOR FILE {file.name}: APPENDED TEXT")
            except TypeError:
                conc_list.append("")
                print(f"[-] FOR FILE {file.name}: COULD NOT APPENDED TEXT")
            
            print(f"{file.name} done.\n")
            

    # list of titles, list of lengths and list of c_text
    dict_ = {"TITLE": name_list, "SIZE IN MB": size_list, "CONCLUSION_TEXT": conc_list}

    df = pd.DataFrame(dict_)

    df.to_excel("../conclusion_excel.xlsx", index=False)
    print("[++] Successfully saved to excel.")
    print(f"[LOG] Execution time: {time.time() - start_time} seconds")


if __name__ == "__main__":
    run()
