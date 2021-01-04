class SilahliKuvvetler(object):  
    "This class represents Silahlı Kuvvetler and it's the parent class.-Oğuz-"  
    def __init__(self,name,yearOfStart):  
        self.name = name  
        self.yearOfStart = yearOfStart     
  
    def IsRetired(self):  
        from datetime import datetime           # Anlık seneyi kullanabilmek için datetime modülünü import ettik.  
        instanceTime = datetime.now()           # (init’e almadık ki sürekli import etmeyip,  
                                                # gerektiği zamanlarda import etsin, performansta düşüklük yaşamayalım.)  
         
        if (instanceTime.year - self.yearOfStart) > 40:  
            return True                                          # If it's achieved to condition we retire them   
              
        else:  
            return False  
        

class Denizaltı(SilahliKuvvetler):
    "Bu sınıf denizaltıları temsil eder, TSK envanterinde aktif faaliyette olan denizaltı sınıfları incelenmiştir -Ata" #silahlı kuvvetler classına override yapılmıştır
    
    def __init__(self,name,yearOfStart):                 
        SilahliKuvvetler.__init__(self, name, yearOfStart)
        print("ETKİN , CAYDIRICI , SAYGIN")                                    #Türk Deniz Kuvvetleri'nin sloganıdır.Denizaltı sınıfı çağrıldığında yansıtılacaktır.                                      

    def sınıflar(self):
        print("GÜR , PREVEZE , AY ")                                          #Türk Silahlı Kuvvetlerinde 3 çeşit denizaltı sınıfı vardır
                                                                                                
                                                                                            
    def slogan(self,denizaltının_sınıfı):
        self.denizaltının_sınıfı=denizaltının_sınıfı          #Her denizaltının kendine has bir sloganı olur. Her sınıf denizaltından birer örnek slogan yazdırdım


        if self.denizaltının_sınıfı=="GÜR":
            print("DENİZLER ONUNLA HÜR")
        if self.denizaltının_sınıfı=="PREVEZE":
            print("DERİNLİKLERİN EFSANESİ")
        if self.denizaltının_sınıfı=="AY":
            print("DERİNLİKlERİN CESUR OKU")
    
    def Deplasman_tonajı(self,denizaltının_sınıfı):
        self.denizaltının_sınıfı=denizaltının_sınıfı

        if self.denizaltının_sınıfı=="GÜR":
            print("Satıhta 1454 ton, dalmış halde 1586 ton taşır" )                         #deplasman tonajı bir denizaltının hareket kabiliyetini kaybetmeyeceği maksimum ağırlıktır.
                                                                                            #kaynakça : https://www.dzkk.tsk.tr/Destek/icerik/gür-sinifi         
        if self.denizaltının_sınıfı=="PREVEZE":
            print("Satıhta 1454 ton, dalmış halde 1586 ton taşır" )                         #kaynakça : https://www.dzkk.tsk.tr/Destek/icerik/preveze-sinifi
                
        if self.denizaltının_sınıfı=="AY":
            print("Satıhta 980 ton, dalmış halde 1185 ton taşır" )                          #kaynakça : https://www.dzkk.tsk.tr/Destek/icerik/ay-sinifi 

        elif self.denizaltının_sınıfı!="AY" and self.denizaltının_sınıfı!="PREVEZE" and self.denizaltının_sınıfı!="GÜR":         #yanlış girişlerde kullanıcıyı uyarır
            print("lütfen TSK envanterinde olan bir denizaltı sınıfı giriniz")
            

    def Seyir_menzili(self,denizaltının_sınıfı):
        self.denizaltının_sınıfı=denizaltının_sınıfı #Denizaltı sınıflarına göre menzillerini gösterir, metreye çevirir.
        nm=1852                                                                         #bir deniz mili (nautical mile) 1852 metredir hesaplamalarımızda kullanacağız

        if self.denizaltının_sınıfı=="GÜR":
            seyir_menzili_nm=7500
            seyir_menzili_m=7500*nm
            print("GÜR sınıfı denizaltıların menzili ,", seyir_menzili_nm ,"deniz milidir.""\n" "Bir deniz mili ",nm,"  metre olduğuna göre seyir menzili ,",seyir_menzili_m,"metre eder.")

        if self.denizaltının_sınıfı=="PREVEZE":
            seyir_menzili_nm=8200
            seyir_menzili_m=8200*nm
            print("PREVEZE sınıfı denizaltıların menzili ,",seyir_menzili_nm, "deniz milidir.\n Bir deniz mili ",nm," metre olduğuna göre seyir menzili ,",seyir_menzili_m,"metre eder.")

        if self.denizaltının_sınıfı=="AY":
            seyir_menzili_nm=7500
            seyir_menzili_m=7500*nm
            print("AY sınıfı denizaltıların menzili ,",seyir_menzili_nm, "deniz milidir.\n Bir deniz mili ",nm," metredir. Metreye çevirecek olursak ,",seyir_menzili_m,"metre eder.")

        elif self.denizaltının_sınıfı!="AY" and self.denizaltının_sınıfı!="PREVEZE" and self.denizaltının_sınıfı!="GÜR":            #yanlış girişlerde kullanıcıyı uyarır
            print("lütfen TSK envanterinde olan bir denizaltı sınıfı giriniz")
    def IsRetired(self):                                         # Silahlı kuvvetlerdeki   IsRetired fonksiyonunun (override) üzerine yazacağız
                                                                 # Gemiler silahlı kuvvetlerde en uzun süre kullanılabilen araçlardır , bunun sebebi ise her sene periyodik bakımları olmasıdır.
        from datetime import datetime
        instanceTime = datetime.now()

        if (instanceTime.year - self.yearOfStart) > 60:  
            return True                                         # En eski denizaltılar ay sınıfı denizaltılardır ve 1975 te alınmıştır,hala aktif servistedir.  
        else:  
            return False
            
                                                                                        
TCG_GÜR = Denizaltı("TCG_GÜR",2004)
TCG_GÜR.sınıflar()
print(TCG_GÜR.name,"emekli edilmiştir: ",TCG_GÜR.IsRetired())
TCG_GÜR.slogan("GÜR")
TCG_GÜR.Deplasman_tonajı("GÜR")
TCG_GÜR.Seyir_menzili("GÜR")
print("\n")
TCG_PREVEZE = Denizaltı("TCG_PREVEZE",1989)
print(TCG_PREVEZE.name,"emekli edilmiştir: ",TCG_PREVEZE.IsRetired())
TCG_PREVEZE.slogan("PREVEZE")
TCG_PREVEZE.Deplasman_tonajı("PREVEZE")
TCG_PREVEZE.Seyir_menzili("PREVEZE")
print("\n")                                                                                    #çağırırken karmaşa olmaması için boşluk ekledim
TCG_AY=Denizaltı("TCG_AY",1975)
print(TCG_AY.name,"emekli edilmiştir: ",TCG_AY.IsRetired())
TCG_AY.slogan("AY")
TCG_AY.Deplasman_tonajı("AY")
TCG_GÜR.Seyir_menzili("AY")



