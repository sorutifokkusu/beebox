from beebox import Beebox
from beebox import first_time
import calculate
import time
import json
#module



while True:
    
    #ilk kez çalıştırma yapıp yapmadığını anlamak için bir try except block
    try:
        f = open("arilar.json","r+",encoding="utf-8")
        data = json.load(f)
        f.close
        uwu=True
    except:
        print("FIRST TIME MODU - OTOMATIK SEÇIM 6")
        secim = 6
        uwu=False
    # eğerki uwu=True gelirse 
    if uwu:
        secim = input("İşlem seçin:\n1- Kovan ekle\n2- Kovan seç\n3- Tüm kovan durumunu göster \n4- Kovan sil\n5- Kovan düzenle\n6- First Time Mode\n7- Çıkış\n\nSeçim: ")

    try:
        secim = int(secim)

    except ValueError:
        print("Yanlış bir değer girdiniz lütfen tekrar deneyiniz\n")
        time.sleep(1)

    if secim == 1:
        sira=calculate.kovansayi()
        print(f"Otomatik tanımlanmış kovan no = ",sira)
        time.sleep(1)

        try:
            cita = int(input("Çıta sayısı: "))

        except ValueError:
            print("Lütfen çıta sayıyla değeri girin\n")
            time.sleep(1)
            
        
        try:
            durum = str(input("Durum: "))

        except ValueError:
            print("Yanlış bir değer girdiniz lütfen tekrar deneyiniz\n")
            time.sleep(1)
            
        
        try:
            ilac = bool(input("İlaç(True veya False) : "))
        except ValueError:
            print("Sadece False veya True yazın. Büyük küçük harf duyarlıdır.\n")
            time.sleep(1)
        
        
        Beebox(sira,cita,durum,ilac)

    elif secim == 2:
        try:
            no = input("Kovan numarası girin: ")
            print("\n")
            calculate.durum_goster(no)
        except ValueError:
            print("Hatalı değer, lütfen sayı değeri giriniz..")
            time.sleep(1)
    
    elif secim == 3:
        calculate.tum_durum()
    elif secim == 4:
        no = input("değer: ")
        calculate.delete_kovan(no)

    elif secim == 5:
        no = input("değer: ")
        calculate.edit_kovan(no)

    elif secim == 6:
        sira = 1
        try:
            cita = int(input("Çıta sayısı: "))

        except ValueError:
            print("Lütfen çıta sayıyla değeri girin\n")
            time.sleep(1)
            
        
        try:
            durum = str(input("Durum: "))

        except ValueError:
            print("Yanlış bir değer girdiniz lütfen tekrar deneyiniz\n")
            time.sleep(1)
            
        
        try:
            ilac = bool(input("İlaç(True veya False) : "))
        except ValueError:
            print("Sadece False veya True yazın. Büyük küçük harf duyarlıdır.\n")
            time.sleep(1)
        
        first_time(sira,cita,durum,ilac,uwu)
        
    elif secim == 7:
        break


