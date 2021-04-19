#Class files
import json


class Beebox:
    def __init__(self,no,cita,durum,ilac):
        #Parameters
        self.no = no
        self.cita = cita
        self.durum = durum
        self.ilac = ilac
        #Loading File -- will give error if .json is empty also retriewing data there is to use it like a database kinda idk
        f = open("arilar.json","r+",encoding="utf-8")
        data = json.load(f)

        #The structure of the data json and sending it as a list to hold multiple items
        data.append(
            {"No" : self.no,
            "Cita" : self.cita,
            "Durum" : self.durum,
            "Ilac" : self.ilac }
            )
        
        with open("arilar.json","w",encoding="utf-8") as arilarjson:
            json.dump(data,arilarjson)
            f.close
            print("\nİşlem başarılı..\n")
    
        #file is opened and closed in init

        

def first_time(no,cita,durum,ilac,uwu):
    #If you get error from init you gotta use this func
    if uwu:
        x = input("Bu ilk kullanım içindir ve bilgilerinizi siler. İlk kullanımda oluşan bir hatadan dolayı\n bu method bulunmaktadır. \nDevam etmek için Y harfini girin: ")
    else:
        x = "Y"
    if x=="Y":
        data = [
            {"No" : no,
            "Cita" : cita,
            "Durum" : durum,
            "Ilac" : ilac }
        ]

        with open("arilar.json","w",encoding="utf-8") as arilarjson:
            json.dump(data,arilarjson)
            arilarjson.close
    
    else:
        pass
            
        
        
    
