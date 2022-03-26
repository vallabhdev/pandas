import pandas as pd
import os

raw_files = os.listdir('..\..\..\data\\')

for file in raw_files:
    df = pd.read_csv('..\..\..\data\\'+file,encoding='unicode_escape')
    columns=[]
    for i in df:
        columns.append(i)

    for column_value in columns:
        if column_value=="Population":
            index = columns.index('Population')
            cleaning_column = df['Population'].to_list()
            i=0
            for i in range(len(cleaning_column)):
                if pd.isna(cleaning_column[i]):
                    cleaning_column[i]=0

                elif type(cleaning_column[i])==str:
                    temp=cleaning_column[i]
                    cleaning_column[i] = cleaning_column[i].replace(",", "")
                    cleaning_column[i] = cleaning_column[i].replace('"', "")

                cleaning_column[i]=int(cleaning_column[i])
            del df['Population']
            df.insert(index, "Population", cleaning_column , True)
            df.to_csv('..\..\..\data\\'+file)

