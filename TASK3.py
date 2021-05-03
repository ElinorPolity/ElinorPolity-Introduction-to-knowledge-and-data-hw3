import json
import os
# first function - get the text file, splits it into rows and uses the other function
def Read_Messages(path:str) -> str :
    Text=open(path,encoding=("utf8"))
    Text=Text.read()
    Text=Text.split("\n")
    return Organize_In_Derectory(Text)
    
#the function where we give code names to paricipens and converting the text file into json
def Organize_In_Derectory(Text:str): 
    phoneInfo=dict()
    All_directoris=[]
    phoneOrName=[]
    Id_list=[]
    ID=0
    counter=0
    for line in Text: 
        # finding the row with the information about the founder of the group
        if "הקבוצה" in line and "נוצרה על ידי" in line:
            date_Metadata=line[:line.find("-")]
            group_title=line[27:len(line)-35]
            creator=line[len(line)-21:]
            MetaData={"chat_name":group_title,"creation_data":date_Metadata,"creator":creator.strip()}
        #finding all phone numbers or names and checking if we allready converted them to ID
        if ": " in line:
            phone_num=line[18:line.find(": ")]
            if phone_num in phoneOrName:
                for phone in phoneOrName:
                    if phone==phone_num:
                        TheID=Id_list[counter]
                        phoneInfo={"date":line[:line.find("-")-1],"ID":TheID,"text":line[line.find(": ")+2:].strip()}
                        All_directoris+=[phoneInfo]
                        counter+=1
            #if we didnt convert them to ID allready then:
            else:
                ID=ID+1
                phoneInfo={"date":line[:line.find("-")-1],"ID":str(ID),"text":line[line.find(": ")+2:].strip()}
                All_directoris+=[phoneInfo]
                phoneOrName+=[phone_num]
                Id_list+=[str(ID)]
        
        counter=0
    #combin the two dict to one dict, conveting to json and saving as text file/
    MetaData["num_of_participants"]=ID
    combine_derectory={"messages":All_directoris,"metadata":MetaData}
    json_file=json.dumps(combine_derectory, ensure_ascii=False, indent=5)
    print(json_file)
    with open(os.path.join('C:\hw3',group_title+".txt") , 'w',encoding='utf-8') as f:
       f.write(json_file)
       
#calling the function
Read_Messages("C:\hw3\WhatsApp.txt")
                 
        
       
        
                   
    
