import xml.etree.ElementTree as xet

import pandas as pd

parsedXml = xet.parse('myFile.xml')
columns = ['name', 'phone', 'email', 'date', 'country']
rows = []

root = parsedXml.getroot()

for each in root:
    name = each.find("name").text
    phone = each.find("phone").text
    email = each.find("email").text
    date = each.find("date").text
    country = each.find("country").text

    rows.append({"name": name,
                 "phone": phone,
                 "email": email,
                 "date": date,
                 "country": country})
df = pd.DataFrame(rows, columns)
df.to_csv('myFile.csv')
