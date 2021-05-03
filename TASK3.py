import json
import os
def Read_Messages(path:str) -> str :
    Text=open(path,encoding=("utf8"))
    Text=Text.read()
    Text=Text.split("\n")
    return Organize_In_Derectory(Text)
    

def Organize_In_Derectory(Text:str): 
    phoneInfo=dict()
    All_directoris=[]
    phoneOrName=[]
    Id_list=[]
    ID=0
    counter=0
    for line in Text: 
        if "הקבוצה" in line and "נוצרה על ידי" in line:
            date_Metadata=line[:line.find("-")]
            group_title=line[27:len(line)-35]
            creator=line[len(line)-21:]
            MetaData={"chat_name":group_title,"creation_data":date_Metadata,"creator":creator.strip()}
        if ": " in line:
            phone_num=line[18:line.find(": ")]
            if phone_num in phoneOrName:
                for phone in phoneOrName:
                    if phone==phone_num:
                        TheID=Id_list[counter]
                        phoneInfo={"date":line[:line.find("-")-1],"ID":TheID,"text":line[line.find(": ")+2:].strip()}
                        All_directoris+=[phoneInfo]
                        counter+=1
            else:
                ID=ID+1
                phoneInfo=phoneInfo={"date":line[:line.find("-")-1],"ID":str(ID),"text":line[line.find(": ")+2:].strip()}
                All_directoris+=[phoneInfo]
                phoneOrName+=[phone_num]
                Id_list+=[str(ID)]
        
        counter=0
    MetaData["num_of_participants"]=ID
    combine_derectory={"messages":All_directoris,"metadata":MetaData}
    json_file=json.dumps(combine_derectory, ensure_ascii=False, indent=5)
    print(json_file)
    with open(os.path.join('C:\hw3',group_title+".txt") , 'w',encoding='utf-8') as f:
       f.write(json_file)      
Read_Messages("C:\hw3\WhatsApp.txt")
                 
        
                   
    
