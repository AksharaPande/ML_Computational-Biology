import re
import os
from datetime import datetime
import pandas as pd

# Create an empty dictionary 
def count(words):
    d = dict() 

  
    # Iterate over each word in line 
    for word in words: 
        # Check if the word is already in dictionary 
        if word in d: 
            # Increment count of word by 1 
            d[word] = d[word] + 1
        else: 
            # Add the word to dictionary with count 1 
            d[word] = 1
  
# Print the contents of dictionary 
    for key in list(d.keys()): 
        print(key, ":", d[key]) 


def pdf_csv(input_file) :
    #input_file="text1-15-march-2020.pdf.txt"
    file_name = os.path.splitext(input_file)[0]
    #print(file_name)
    f1 = '-'.join(file_name.split("-")[1::])
    #print(date_string)
    file = open(input_file, "r", encoding="utf8")
    string = file.read()
    #print(string)

    #count("the cause of death is described as")
    r1 = re.findall(r"the cause of death is described as",string)
    #print(len(r1))
    pattern = "\d{2}[/-]\d{2}[/-]\d{4}" #date
    m00=[]
    m11=[]
    m22=[]

# Will return all the strings that are matched
    m0 = re.findall(pattern, string)
#m0 = datefinder.find_dates(string) 
    #print(m0)

 
    m1=  re.findall('(?:\S+\s)?\S*year', string)  
    #print(m1)
    #m2=  re.findall('(?<=due to)[^\.]*\.', string)  
    m2=  re.findall('old\S*(?:\s\S+)?', string) 
         
    m00.append(m0[0])
    
    
    m11.append(m1)
    m22.append(m2)

    
    df=pd.DataFrame()
    df["Date"]=m00
   
    df["year"]=m11
    df["Age"]=m22    
    #df.to_csv(file_name+"_age_gen.csv",index=None) 
    return df
    
#pdf_csv("text2-16-march-2020.pdf.txt")    

xx=os.listdir()
print(xx)
#k={}
dff=pd.DataFrame()
for i in xx:
    if os.path.splitext(i)[1]=='.txt' :
        #print(os.path.splitext(i))
        #print(i) 
        kk=pdf_csv(i) 
        dff=dff.append(kk.values.tolist())
        #print(kk)
        #k.update(kk)
    #dff["val"]=k[i]

#file=open("new","w")
#file.writelines(str(k))
#file.close()    
dff.to_csv("new_age_gen.csv",index=None)


             


