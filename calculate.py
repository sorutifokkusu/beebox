from beebox import Beebox
import json
import time
#Gerekli kütüphaneler

#Kovan çıta sayısını geri döndürür
def cita_durum(no):

    no = int(no)
    with open("arilar.json","r",encoding="utf-8") as y:
        data = json.load(y)
        for i in data:
            if i["No"] == no:
                return (i["Cita"])
            
            
 

        
#Kovan durumunu geri döndürür
def durum_durum(no):

    no = int(no)
    with open("arilar.json","r",encoding="utf-8") as y:
        data = json.load(y)
        for i in data:
            if i["No"] == no:
                return(i["Durum"])
            
                
        
#Kovan ilaç durumunu geri döndürür
def ilac_durum(no):
    no = int(no)
    with open("arilar.json","r",encoding="utf-8") as y:
        data = json.load(y)
        for i in data:
            if i["No"] == no:
                return(i["Ilac"])
            
#Kovan sayısını geri döndürür eğer dosya ilk açılış yapıyorsa x=1 verir
#Bu kod otomatik sıralama yapar

def kovansayi():

    try:
        with open("arilar.json","r",encoding="utf-8") as y:
            data = json.load(y)
            x=1
            for i in data:
                x+=1
    except:
        x=1
        return x
        
    return x
# Burada uyarı vermesinin sebebi İ nin kullanılmamış olması burada i = n eleman sayısı 

#Bir Kovanın tüm durumunu gösterir no parametresi alır
def durum_goster(no):
    x=str(ilac_durum(no))
    y=str(cita_durum(no))
    v=str(durum_durum(no))

    print(f"No: "+no+" Çıta: "+y+ " Durum:  "+v+ " İlaç: " + x+"\n")
    time.sleep(2)

#Tüm kovanların durumunu gösterir
def tum_durum():
    with open("arilar.json","r",encoding="utf-8") as y:
        data = json.load(y)
        x=str(kovansayi()-1)
        print("No - Çıta - Durum - İlaç\n")
        time.sleep(1)
        for i in data:
            print(i["No"],"-",i["Cita"],"-",i["Durum"],"-",i["Ilac"])
        
        print(f"\nToplam kovan sayısı: "+x+"\n")
        time.sleep(3)

def edit_kovan(no):
    with open("arilar.json","r+",encoding="utf-8") as y:
        data = json.load(y)
        no = int(no)
        for i in data:
            x = int(i["No"])
            if x == no:
                print("Method works")

def delete_kovan(no):
    f = open("arilar.json","r+",encoding="utf-8")
    data = json.load(f)
    no = int(no)
    for i in data:
            x = int(i["No"])
            if x == no:
                no = no -1
                del data[no]
                print("Method works check if deleted correctly")
    renumber = input("Yeniden numaralandır?")
    if renumber =="Y":
        x = 1
        for i in data:
            i["No"] = x
            x+=1

    
    with open("arilar.json","w",encoding="utf-8") as y:
        json.dump(data,y)
        print("\nİşlem başarılı..\n")
        f.close
