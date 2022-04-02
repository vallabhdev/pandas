import pandas as pd
import os

#Getting every file from the data folder
raw_files = os.listdir('..\..\..\data\\')

#taking one file at a time
for file in raw_files:
    #connecting that file with path and reading it
    df = pd.read_csv('..\..\..\data\\'+file)

    #taking column names from data
    columns=[]
    for i in df:
        columns.append(i)

    #iterating through columns
    for column_value in columns:
        #checking if column name is population
        if column_value=="Population":
            #taking index of population column
            index = columns.index('Population')
            #converting it into list
            cleaning_column = df['Population'].to_list()
            i=0
            for i in range(len(cleaning_column)):
                #if it has null value than it will be given 0
                if pd.isna(cleaning_column[i]):
                    cleaning_column[i]=0

                # if the type is string and has comma and inverted comma, it will remove that
                elif type(cleaning_column[i])==str:
                    temp=cleaning_column[i]
                    cleaning_column[i] = cleaning_column[i].replace(",", "")
                    cleaning_column[i] = cleaning_column[i].replace('"', "")

                #Making every value integer
                cleaning_column[i]=int(cleaning_column[i])
            #delete old population column
            del df['Population']

            #insert clened column at the same place as it was
            df.insert(index, "Population", cleaning_column , True)
            #saving the csv at same place
            df.to_csv('..\..\..\data\\'+file)

