# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 19:42:35 2020

@author: Skynet
"""

import time
def komut(x):
    
    "Yapılacak işlemlerden gelen komutu sınıfa göndermektedir"
    
    if(x=="1"):
        
        yazılımcı1.bigileri_goster()
    elif(x=="2"):
        
        yazılımcı1.ad_degistir(input("Yeni ad giriniz : "))
    elif(x=="3"):
        yazılımcı1.soyad_degistir(input("Yeni soyad : "))
    elif(x=="4"):
        yazılımcı1.yas_degistir(input("YAŞ DEĞİŞTİR : "))
    elif(x=="5"):
        yazılımcı1.maas_degistir(int(input("Maaş zam yap : ")))
    elif(x=="6"):
        yazılımcı1.dil_ekle(input("Lütfen yeni dili giriniz : "))
    
    
    
class yazılımcı():
    
    
    "YAZILIMCI SINIFI YAPILARAK DATA ÜZERİNDE EKLEMELER VE DATAYI SAKLAMAYA ÇALIŞILMIŞTIR "
    
    
    def __init__(self,ad="BİLGİ YOK",soyad="BİLGİ YOK",yas="BİLGİ YOK",maas="BİLGİ YOK",diller=[]):
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        self.maas=maas
        self.diller=diller
    def bigileri_goster(self):
        print("""
             ******Yazılımcı Bilgileri****** 
             
             Ad : {}
             
             Soyad : {}
             
             Yaş : {}
             
             Maaş : {}
             
             Diller : {}
             
             
              """.format(self.ad, self.soyad,self.yas,self.maas,self.diller))
    def ad_degistir(self,ad_degistir):
        print("İşlem yapılıyor...")
        self.ad=ad_degistir
        time.sleep(1)
        print("Ad değiştirildi")
    def soyad_degistir(self,soyad_degistir):
        print("İşlem yapılıyor...")
        self.soyad=soyad_degistir
        time.sleep(1)
        print("Soyad değiştirildi")
    def yas_degistir(self,yas_degistir):
        print("İşlem yapılıyor...")
        self.yas=yas_degistir
        time.sleep(1)
        print("Yaş değiştirildi")
    def maas_degistir(self,maas_degistir):
        print("İşlem yapılıyor...")
        self.maas+=int(maas_degistir)
        time.sleep(1)
        print("Maaş değiştirildi")
    def dil_ekle(self,dil_ekle):
        print("İşlem yapılıyor...")
        self.diller.append(dil_ekle)
        time.sleep(1)
        print("Dil eklendi.")
        

while True:
    
    "Burada kullanıcı girişi sağlanmaktadır"
    
    
    kullanıcı_adı=input("Kullanıcı adı : ")
    kullanıcı_sifresi=input("Kullanıcı sifresi : ")
    if(kullanıcı_adı=="bahadır_alp" and kullanıcı_sifresi=="1352"):
        print("Bilgiler kontrol ediliyor...")
        time.sleep(1)
        print("Hoşgeldiniz Bahadır bey...")
        break
    else:
        print("Bilgiler kontrol ediliyor...")
        time.sleep(1)
        if(kullanıcı_adı=="bahadır_alp"):
            print("Kullanıcı şifreniz yanlıştır.")
        elif(kullanıcı_sifresi=="1352"):
            print("Kullanıcı adınız yanlıştır.")
        else:
              print("Bilgileriniz yanlıştır.")

ad=input("Lütfen ad giriniz : ")
soyad=input("Lütfen soyadı giriniz : ") 
yas=input("Lütfen yaşı giriniz : ")
maas=int(input("Lütfen maaşı giriniz : "))
diller=[input("Lütfen dilleri giriniz : ")]
yazılımcı1=yazılımcı(ad,soyad,yas,maas,diller)
while True:
    "Yapılacak işlemler"
   t=input("""
          
          
          ******Yapılacak bir işlem var mı******
          
          1-Bilgileri Kontrol et
          2-Ad değiştir
          3-Soyad değiştir
          4-yas değiştir
          5-zam yap
          6-dil ekle
        """)
   if(t=="q"):
       break
   komut(t)
   