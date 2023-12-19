from bs4 import BeautifulSoup
import re
import pandas as pd

with open("table.html", "r") as f:
    html_code = BeautifulSoup(f, "html.parser")

trs = html_code.find_all("tr")

dct = {'Sector': [], 'Contract Number': [], 'Supplier': [],
       'Medical Doctor': [], 'Adress': [], 'Phone Number': []}

for tr in trs:
    tds = tr.find_all("td")
    # extract and convert adress to string
    adress = ''.join(str(tds[4].string).split())
    # extract sector number from the adress using regex
    sector_number = int(re.match('.+([0-9])[^0-9]*$', adress).group(1))

    # creating a dictionary with my data
    dct['Sector'].append(sector_number)
    dct['Contract Number'].append(str(tds[1].string))
    dct['Supplier'].append(str(tds[2].string))
    dct['Medical Doctor'].append(str(tds[3].string))
    dct['Adress'].append(str(tds[4].string))
    dct['Phone Number'].append(str(tds[5].string))

data = pd.DataFrame(dct)    # creating dataframe from my dictionary with pandas

data.to_excel("output.xlsx")    # storing data into xlsx file
