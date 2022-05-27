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
    m111=[]
    m22=[]
    m33=[]
    m44=[]    
    m55=[]
    m66=[]
    m77=[] 
    m88=[]
    m99=[]
    m100=[]
    m101=[]
    m102=[]
    m103=[]
    m104=[]
# Will return all the strings that are matched
    m0 = re.findall(pattern, string)
#m0 = datefinder.find_dates(string) 
    #print(m0)

    m1 = re.search('(?<=Almora )\s*([^\n\r]*)', string)
    m2 = re.search('(?<=Bageshwar )\s*([^\n\r]*)', string)
    m3 = re.search('(?<=Chamoli )\s*([^\n\r]*)', string)    
    m4 = re.search('(?<=Champawat )\s*([^\n\r]*)', string)
    m5 = re.search('(?<=Dehradun )\s*([^\n\r]*)', string)
    m6 = re.search('(?<=Haridwar )\s*([^\n\r]*)', string)  
   
    m7=  re.search('(?<=Nainital )\s*([^\n\r]*)', string)    
    m8=  re.search('(?<=Pauri Garhwal )\s*([^\n\r]*)', string)  
    m9=  re.search('(?<=Pithoragarh )\s*([^\n\r]*)', string)  
    m10=  re.search('(?<=Rudraprayag )\s*([^\n\r]*)', string) 
    m11=  re.search('(?<=Tehri Garhwal )\s*([^\n\r]*)', string) 
    m12=  re.search('(?<=US Nagar )\s*([^\n\r]*)', string)
    m13=  re.search('(?<=Uttarkashi )\s*([^\n\r]*)', string)    
    m14=  re.search('(?<=Total )\s*([^\n\r]*)', string)
         
    m00.append(m0[0])
    #print(m71)
    #x=m71

   

      
    str1=(m1.group(1)).replace(" ",",")
    l1=[s for s in str1.split(',')]
    str2=(m2.group(1)).replace(" ",",")
    l2=[s for s in str2.split(',')]
    str3=(m3.group(1)).replace(" ",",")
    l3=[s for s in str3.split(',')]
    str4=(m4.group(1)).replace(" ",",")
    l4=[s for s in str4.split(',')]    
    str5=(m5.group(1)).replace(" ",",")
    l5=[s for s in str5.split(',')]
    str6=(m6.group(1)).replace(" ",",")
    l6=[s for s in str6.split(',')]
    str7=(m7.group(1)).replace(" ",",")
    l7=[s for s in str7.split(',')]
    str8=(m8.group(1)).replace(" ",",")
    l8=[s for s in str8.split(',')]
    str9=(m9.group(1)).replace(" ",",")
    l9=[s for s in str9.split(',')]
    str10=(m10.group(1)).replace(" ",",")
    l10=[s for s in str10.split(',')]
    str11=(m11.group(1)).replace(" ",",")
    l11=[s for s in str11.split(',')]
    str12=(m12.group(1)).replace(" ",",")
    l12=[s for s in str12.split(',')]
    str13=(m13.group(1)).replace(" ",",")
    l13=[s for s in str13.split(',')]
    str14=(m14.group(1)).replace(" ",",")
    l14=[s for s in str14.split(',')]
    xxx=pd.Series(l1)
    xxx1=pd.Series(l2)
    xxx2=pd.Series(l3)
    xxx3=pd.Series(l4)
    xxx4=pd.Series(l5)
    xxx5=pd.Series(l6)
    xxx6=pd.Series(l7)
    xxx7=pd.Series(l8)
    xxx8=pd.Series(l9)
    xxx9=pd.Series(l10)
    xxx10=pd.Series(l11)
    xxx11=pd.Series(l12)
    xxx12=pd.Series(l13)
    xxx13=pd.Series(l14)
    #print(xxx7)
    

    
    df=pd.DataFrame()
    df["Date"]=m00
    df["Almora1"]=xxx[0] 
    df["Almora2"]=xxx[1]
    df["Almora3"]=xxx[2]
    df["Almora4"]=xxx[3]
    df["Almora5"]=xxx[4]
    df["Almora6"]=xxx[5]
    df["Almora7"]=xxx[6]
    df["Almora8"]=xxx[7]
    df["Almora9"]=xxx[8]
    df["Almora10"]=xxx[9]
    df["Almora11"]=xxx[10]
    
    df["Bageshwar1"]=xxx1[0]
    df["Bageshwar2"]=xxx1[1]
    df["Bageshwar3"]=xxx1[2]
    df["Bageshwar4"]=xxx1[3]
    df["Bageshwar5"]=xxx1[4]
    df["Bageshwar6"]=xxx1[5]
    df["Bageshwar7"]=xxx1[6]
    df["Bageshwar8"]=xxx1[7]
    df["Bageshwar9"]=xxx1[8]
    df["Bageshwar10"]=xxx1[9]
    df["Bageshwar11"]=xxx1[10]
    
    df["Chamoli1"]=xxx2[0]    
    df["Chamoli2"]=xxx2[1]
    df["Chamoli3"]=xxx2[2]
    df["Chamoli4"]=xxx2[3]
    df["Chamoli5"]=xxx2[4]
    df["Chamoli6"]=xxx2[5]
    df["Chamoli7"]=xxx2[6]
    df["Chamoli8"]=xxx2[7]
    df["Chamoli9"]=xxx2[8]
    df["Chamoli10"]=xxx2[9]
    df["Chamoli11"]=xxx2[10]
    
    df["Champawat1"]=xxx3[0]
    df["Champawat2"]=xxx3[1]
    df["Champawat3"]=xxx3[2]
    df["Champawat4"]=xxx3[3]
    df["Champawat5"]=xxx3[4]
    df["Champawat6"]=xxx3[5]
    df["Champawat7"]=xxx3[6]
    df["Champawat8"]=xxx3[7]
    df["Champawat9"]=xxx3[8]
    df["Champawat10"]=xxx3[9]
    df["Champawat11"]=xxx3[10]
    
    df["Dehradun1"]=xxx4[0]
    df["Dehradun2"]=xxx4[1]
    df["Dehradun3"]=xxx4[2]
    df["Dehradun4"]=xxx4[3]
    df["Dehradun5"]=xxx4[4]
    df["Dehradun6"]=xxx4[5]
    df["Dehradun7"]=xxx4[6]
    df["Dehradun8"]=xxx4[7]
    df["Dehradun9"]=xxx4[8]
    df["Dehradun10"]=xxx4[9]
    df["Dehradun11"]=xxx4[10]
    
    df["Haridwar1"]=xxx5[0]
    df["Haridwar2"]=xxx5[1]
    df["Haridwar3"]=xxx5[2]
    df["Haridwar4"]=xxx5[3]
    df["Haridwar5"]=xxx5[4]
    df["Haridwar6"]=xxx5[5]
    df["Haridwar7"]=xxx5[6]
    df["Haridwar8"]=xxx5[7]
    df["Haridwar9"]=xxx5[8]
    df["Haridwar10"]=xxx5[9]    
    df["Haridwar11"]=xxx5[10] 
    
    df["Nainital1"]=xxx6[0]
    df["Nainital2"]=xxx6[1]
    df["Nainital3"]=xxx6[2]
    df["Nainital4"]=xxx6[3]
    df["Nainital5"]=xxx6[4]
    df["Nainital6"]=xxx6[5]
    df["Nainital7"]=xxx6[6]
    df["Nainital8"]=xxx6[7]
    df["Nainital9"]=xxx6[8]
    df["Nainital10"]=xxx6[9]    
    df["Nainital11"]=xxx6[10]
    
 
    df["Pauri Garhwal1"]=xxx7[0]
    df["Pauri Garhwal2"]=xxx7[1]
    df["Pauri Garhwal3"]=xxx7[2]
    df["Pauri Garhwal4"]=xxx7[3]
    df["Pauri Garhwal5"]=xxx7[4]
    df["Pauri Garhwal6"]=xxx7[5]
    df["Pauri Garhwal7"]=xxx7[6]
    df["Pauri Garhwal8"]=xxx7[7]
    df["Pauri Garhwal9"]=xxx7[8]
    df["Pauri Garhwal10"]=xxx7[9]
    df["Pauri Garhwal11"]=xxx7[10]    
    
    df["Pithoragarh1"]=xxx8[0]
    df["Pithoragarh2"]=xxx8[1]
    df["Pithoragarh3"]=xxx8[2]
    df["Pithoragarh4"]=xxx8[3]
    df["Pithoragarh5"]=xxx8[4]
    df["Pithoragarh6"]=xxx8[5]
    df["Pithoragarh7"]=xxx8[6]
    df["Pithoragarh8"]=xxx8[7]
    df["Pithoragarh9"]=xxx8[8]
    df["Pithoragarh10"]=xxx8[9]
    df["Pithoragarh11"]=xxx8[10]
    
    df["Rudraprayag1"]=xxx9[0]
    df["Rudraprayag2"]=xxx9[1]
    df["Rudraprayag3"]=xxx9[2]
    df["Rudraprayag4"]=xxx9[3]
    df["Rudraprayag5"]=xxx9[4]
    df["Rudraprayag6"]=xxx9[5]
    df["Rudraprayag7"]=xxx9[6]
    df["Rudraprayag8"]=xxx9[7]
    df["Rudraprayag9"]=xxx9[8]
    df["Rudraprayag10"]=xxx9[9] 
    df["Rudraprayag11"]=xxx9[10]     
    
    df["Tehri Garhwal1"]=xxx10[0]
    df["Tehri Garhwal2"]=xxx10[1]
    df["Tehri Garhwal3"]=xxx10[2]
    df["Tehri Garhwal4"]=xxx10[3]
    df["Tehri Garhwal5"]=xxx10[4]
    df["Tehri Garhwal6"]=xxx10[5]
    df["Tehri Garhwal7"]=xxx10[6]
    df["Tehri Garhwal8"]=xxx10[7]
    df["Tehri Garhwal9"]=xxx10[8]
    df["Tehri Garhwal10"]=xxx10[9]    
    df["Tehri Garhwal11"]=xxx10[10]
    
    
    df["US Nagar1"]=xxx11[0]
    df["US Nagar2"]=xxx11[1]
    df["US Nagar3"]=xxx11[2]
    df["US Nagar4"]=xxx11[3]
    df["US Nagar5"]=xxx11[4]
    df["US Nagar6"]=xxx11[5]
    df["US Nagar7"]=xxx11[6]
    df["US Nagar8"]=xxx11[7]
    df["US Nagar9"]=xxx11[8]
    df["US Nagar10"]=xxx11[9]
    df["US Nagar11"]=xxx11[10]    
    
    
    
    df["Uttarkashi1"]=xxx12[0]    
    df["Uttarkashi2"]=xxx12[1]    
    df["Uttarkashi3"]=xxx12[2]    
    df["Uttarkashi4"]=xxx12[3]    
    df["Uttarkashi5"]=xxx12[4]    
    df["Uttarkashi6"]=xxx12[5]    
    df["Uttarkashi7"]=xxx12[6]    
    df["Uttarkashi8"]=xxx12[7]    
    df["Uttarkashi9"]=xxx12[8]    
    df["Uttarkashi10"]=xxx12[9]  
    df["Uttarkashi11"]=xxx12[10]      
    
    
    #df["Total"]=pd.Series(l14)     
    df.to_csv(file_name+".csv",index=None) 
    return df
    
#pdf_csv("text2-16-march-2020.pdf.txt")    

xx=os.listdir()
print(xx)
#k={}
dff=pd.DataFrame()
for i in xx:
    if os.path.splitext(i)[1]=='.txt' :
        #print(os.path.splitext(i))
        print(i) 
        kk=pdf_csv(i) 
        dff=dff.append(kk.values.tolist())
        #print(kk)
        #k.update(kk)
    #dff["val"]=k[i]

#file=open("new","w")
#file.writelines(str(k))
#file.close()    
dff.to_csv("new_dist.csv",index=None)

             


