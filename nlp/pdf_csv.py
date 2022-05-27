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
    m33=[]
    m44=[]    
    m55=[]
    m66=[]
    m77=[] 
# Will return all the strings that are matched
    m0 = re.findall(pattern, string)
#m0 = datefinder.find_dates(string) 
    #print(m0)

    m3 = re.search('(?<=Total number of samples found negative) {0,4}(\w+)', string)
    m1 = re.search('(?<=Total number of samples result awaited) {0,4}(\w+)', string)
    m2 = re.search('(?<=Total Positive: ) {0,4}(\w+)', string)    
    m4 = re.search('(?<=Total Death: ) {0,4}(\w+)', string)
    m5 = re.search('(?<=Total Recovered: ) {0,4}(\w+)', string)
    m6 = re.search('(?<=Total Active Cases: ) {0,4}(\w+)', string)  
   
    #m7=  re.search(r'The cause of death is (.*).*', string)    
    #m7=  re.search(r'Cause of death may be (.*).', string)  
    m71=  re.findall('(?<=due to)[^\.]*\.', string)  
         
    m00.append(m0[0])
    print(m71)
    x=m71

   
    y=[]
    for i in range(0,len(x)) :
        y.append(x[i].replace("\n"," "))
      
    #print(y) 
    
    m22.append(m2.group(1))
    m33.append(m3.group(1)) 
    m11.append(m1.group(1))
    m44.append(m4.group(1))
    m55.append(m5.group(1)) 
    m66.append(m6.group(1))
    m77.append(y)  
    #m77.append(m71[0])  
    #m77.append(m71[1])
    
    df=pd.DataFrame()
    df["Date"]=m00


    df["Total number of samples found negative"]=m33  
    df["Total number of samples result awaited"]=m11
    df["Total Positive"]=m22    
    df["Total Death"]=m44
    df["Total Recoverd"]=m55
    df["Total Active Cases"]=m66      
    df["Cause of death"]=m77   
    df.to_csv(file_name+".csv",index=None) 
    
#pdf_csv("text2-16-march-2020.pdf.txt")    

xx=os.listdir()
print(xx)
for i in xx:
    if os.path.splitext(i)[1]=='.txt' :
        print(os.path.splitext(i))
        print(i) 
        pdf_csv(i) 
             


