#Update
This app will be rewritten with a gui interface.

# beebox
A python app for managing your bee hive information

-About the app-
The app is designed to be used barebone (without extra depencies ) 
It is written in python and uses JSON for storing data.

-Requirements-
Install Python
If not included you have to instal JSON with pip


-Windows-
You can run directly from run.bat 

-Usage-

1- Add hive: This will add a hive with its values and will auto save it.

2- Choose Hive: You can choose a hive and show its values.

3- Show all Hive: It will show every hive which has been stored.

4- Delete Hive: It will delete the hive with the matching number auto saved.

5- Edit Hive: It will edit the hive with the matching number auto saved.

6- First Time Setup: This will make the first data entry to JSON. Required because of every other module tries to get the data from JSON file, which when empty will result in error. ( Could be improved ) (There is a first time mode which activates when those situation applies - no json file , json file wrong format , json file empty - it will create or recreate the json file and will ask you for first entry)

7- Quit: Will quit.


-- Türkçe --
Python dilinde yazılmış minimal bir uygulama. Uygulama json kullanılarak en minimal kalmak için tasarlanmıştır.
Kayıtlar json dosyasına yazılır.

-Gereksinimler-
Python kurmanız gerekir.
Eğerki Python ile json modülü gelmiyorsa ayrıca pip ile json modülünü indirmeniz gerekir.

-Windows-
Direk olarak run.bat'ı çalıştırıp kullanabilirsiniz.

-Kullanım-

1- Kovan ekle: Kovan ekler. Şu anlık aldığı değerler Çıta sayısı(SAYI OLMAK ZORUNDA), durumu(istediğinizi girebilirsiniz),İlaç durumu(kesinlikle büyük küçük (True) veya (False) alabilir.

2- Kovan seç: Bu seçenek sizden bir numara değeri alıp o numaraya ait kovan durumunu gösterir seçili kalmaz!!

3- Tüm kovan durumunu göster: Tüm kayıtlı kovanların durumunu gösterir.

4- Kovanı sil: Kovan bilgisini siler, numara değerine göre seçer.

5- Kovanı düzenle: Kovanı düzenlemek için kullanılır, numara değerine göre seçer.

6- First Time Setup: Bu mod eğerki json yok veya hatalı ise otomatik başlar, dosyayı oluşturur ve ilk kaydı sizden ister

7- Çıkış: Uygulamadan çıkar.
