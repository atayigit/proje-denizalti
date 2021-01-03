class SilahliKuvvetler(object):
    "This class represents Silahlı Kuvvetler and it's the super class."
    def __init__(self,name,yearOfStart,activity):
        self.name = name
        self.yearOfStart = yearOfStart
        self.activity = True                    # Here 

    def Retire(self):
        from datetime import datetime           # Anlık seneyi kullanabilmek için datetime modülünü import ettik.
        
        instanceTime = datetime.now()

        if (instanceTime.year - self.yearOfStart) > 40:
            self.activity = False
            print(self.name,"'s working: ", self.activity)
        else:
            print(self.name,"s working: ", self.activity)

        


class Denizaltı(SilahliKuvvetler):
    "Bu sınıf denizaltıları temsil eder, TSK envanterinde aktif faaliyette olan denizaltı sınıfları incelenmiştir -Ata"
    
    def __init__(self,name,yearOfStart,activity):                 
        SilahliKuvvetler.__init__(self, name, yearOfStart, activity)

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
            print("GÜR sınıfı denizaltıların menzili ,", seyir_menzili_nm ,"deniz milidir.""\n" "Bir deniz mili ",nm," metredir. Metreye çevirecek olursak ,",seyir_menzili_m,"metre eder.")

        if self.denizaltının_sınıfı=="PREVEZE":
            seyir_menzili_nm=8200
            seyir_menzili_m=8200*nm
            print("PREVEZE sınıfı denizaltıların menzili ,",seyir_menzili_nm, "deniz milidir.\n Bir deniz mili ",nm," metredir. Metreye çevirecek olursak ,",seyir_menzili_m,"metre eder.")

        if self.denizaltının_sınıfı=="AY":
            seyir_menzili_nm=7500
            seyir_menzili_m=7500*nm
            print("AY sınıfı denizaltıların menzili ,",seyir_menzili_nm, "deniz milidir.\n Bir deniz mili ",nm," metredir. Metreye çevirecek olursak ,",seyir_menzili_m,"metre eder.")

        elif self.denizaltının_sınıfı!="AY" and self.denizaltının_sınıfı!="PREVEZE" and self.denizaltının_sınıfı!="GÜR":            #yanlış girişlerde kullanıcıyı uyarır
            print("lütfen TSK envanterinde olan bir denizaltı sınıfı giriniz")


    def Operasyon_kabiliyeti(self,denizaltının_sınıfı,üs=0,operasyon_bölgesi=0):     #bu fonksiyonda girilen denizaltı sınıfına, denizaltı üs bölgesine ve 3 farklı denizde bulunan operasyon bölgelerine
                                                                                                      #kaç saatte gidileceği hesaplanmıştır.
        self.denizaltının_sınıfı=denizaltının_sınıfı
        self.üs=üs
        self.operasyon_bölgesi=operasyon_bölgesi
        seyir_hızı_satıh_gür=15                                                     #knot biriminde  dalmış ve su yüzeyi (satıh ) hızları verilmiştir, ay sınıfı denizaltılarının hızı su yüzeyinde ve dalmış olarak eşittir.
        seyir_hızı_satıh_preveze=11
        seyir_hızı_dalmış_gür=21.5
        seyir_hızı_dalmış_preveze=21
        seyir_hızı_ay=8

        foça_rodos=201.1                                                            #google haritalar kullanarak denizden en kısa mesafeleri hesapladım.
        foça_kırım=595
        foça_kıbrıs=520
        sinop_rodos=786.8
        sinop_kırım=234.6
        sinop_kıbrıs=1181.3
        
        if self.üs=="FOÇA":                                                         # burada girilen operasyon ve üs bilgisine göre if else bağıntısı kullanarak her  denizaltı sınıfına özgü gidiş sürelerini hesaladım
            
            if self.operasyon_bölgesi=="RODOS":
                if self.denizaltının_sınıfı=="GÜR":

                    süre_satıh=foça_rodos/seyir_hızı_satıh_gür
                    süre_dalmış=foça_rodos/seyir_hızı_dalmış_gür

                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_satıh,"saatte satıhta giderek",self.operasyon_bölgesi,"a ulaşır.")
                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_dalmış,"saatte dalmış giderek",self.operasyon_bölgesi,"a ulaşır.")                


                if self.denizaltının_sınıfı=="PREVEZE":
                    süre_satıh=foça_rodos/seyir_hızı_satıh_preveze
                    süre_dalmış=foça_rodos/seyir_hızı_dalmış_preveze

                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_satıh,"saatte satıhta giderek",self.operasyon_bölgesi,"a ulaşır.")
                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_dalmış,"saatte dalmış giderek",self.operasyon_bölgesi,"a ulaşır.")                
                    


                    
                if self.denizaltının_sınıfı=="AY":

                    süre=foça_rodos/seyir_hızı_ay


                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre,"saatte  giderek",self.operasyon_bölgesi,"a ulaşır.")
                        
                    



                    

                
            if self.operasyon_bölgesi=="KIRIM":
                if self.denizaltının_sınıfı=="GÜR":
                    süre_satıh=foça_kırım/seyir_hızı_satıh_gür
                    süre_dalmış=foça_kırım/seyir_hızı_dalmış_gür

                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_satıh,"saatte satıhta giderek",self.operasyon_bölgesi,"a ulaşır.")
                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_dalmış,"saatte dalmış giderek",self.operasyon_bölgesi,"a ulaşır.")       


                    
                if self.denizaltının_sınıfı=="PREVEZE":
                    süre_satıh=foça_kırım/seyir_hızı_satıh_preveze
                    süre_dalmış=foça_kırım/seyir_hızı_dalmış_preveze

                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_satıh,"saatte satıhta giderek",self.operasyon_bölgesi,"a ulaşır.")
                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_dalmış,"saatte dalmış giderek",self.operasyon_bölgesi,"a ulaşır.")    
                    

                    
                if self.denizaltının_sınıfı=="AY":
                    süre=foça_kırım/seyir_hızı_ay
                    
                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre,"saatte  giderek",self.operasyon_bölgesi,"a ulaşır.")



                    
                
            if self.operasyon_bölgesi=="KIBRIS":
                if self.denizaltının_sınıfı=="GÜR":
                    süre_satıh=foça_kıbrıs/seyir_hızı_satıh_gür
                    süre_dalmış=foça_kıbrıs/seyir_hızı_dalmış_gür

                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_satıh,"saatte satıhta giderek",self.operasyon_bölgesi,"a ulaşır.")
                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_dalmış,"saatte dalmış giderek",self.operasyon_bölgesi,"a ulaşır.")

                    
                if self.denizaltının_sınıfı=="PREVEZE":
                    süre_satıh=foça_kıbrıs/seyir_hızı_satıh_preveze
                    süre_dalmış=foça_kıbrıs/seyir_hızı_dalmış_preveze

                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_satıh,"saatte satıhta giderek",self.operasyon_bölgesi,"a ulaşır.")
                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_dalmış,"saatte dalmış giderek",self.operasyon_bölgesi,"a ulaşır.")    

                    
                if self.denizaltının_sınıfı=="AY":
                    süre=foça_kıbrıs/seyir_hızı_ay
                    
                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre,"saatte  giderek",self.operasyon_bölgesi,"a ulaşır.")

                            



        if self.üs=="SİNOP":
            if self.operasyon_bölgesi=="RODOS":
                if self.denizaltının_sınıfı=="GÜR":
                    süre_satıh=sinop_rodos/seyir_hızı_satıh_gür
                    süre_dalmış=sinop_rodos/seyir_hızı_dalmış_gür

                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_satıh,"saatte satıhta giderek",self.operasyon_bölgesi,"a ulaşır")
                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_dalmış,"saatte dalmış giderek",self.operasyon_bölgesi,"a ulaşır")



                    
                if self.denizaltının_sınıfı=="PREVEZE":
                    süre_satıh=sinop_rodos/seyir_hızı_satıh_preveze
                    süre_dalmış=sinop_rodos/seyir_hızı_dalmış_preveze

                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_satıh,"saatte satıhta giderek",self.operasyon_bölgesi,"a ulaşır")
                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_dalmış,"saatte dalmış giderek",self.operasyon_bölgesi,"a ulaşır")



                    
                if self.denizaltının_sınıfı=="AY":
                    süre_=sinop_rodos/seyir_hızı_ay

                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_dalmış,"saatte giderek",self.operasyon_bölgesi,"a ulaşır")




                    

            if self.operasyon_bölgesi=="KIRIM":
                
                if self.denizaltının_sınıfı=="GÜR":
                    süre_satıh=sinop_kırım/seyir_hızı_satıh_gür
                    süre_dalmış=sinop_kırım/seyir_hızı_dalmış_gür

                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_satıh,"saatte satıhta giderek",self.operasyon_bölgesi,"a ulaşır")
                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_dalmış,"saatte dalmış giderek",self.operasyon_bölgesi,"a ulaşır")



                    
                if self.denizaltının_sınıfı=="PREVEZE":
                    süre_satıh=sinop_kırım/seyir_hızı_satıh_preveze
                    süre_dalmış=sinop_kırım/seyir_hızı_dalmış_preveze

                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_satıh,"saatte satıhta giderek",self.operasyon_bölgesi,"a ulaşır")
                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_dalmış,"saatte dalmış giderek",self.operasyon_bölgesi,"a ulaşır")





                    
                if self.denizaltının_sınıfı=="AY":
                    süre_=sinop_kırım/seyir_hızı_ay

                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_dalmış,"saatte giderek",self.operasyon_bölgesi,"a ulaşır")


                    

            if self.operasyon_bölgesi=="KIBRIS":
                
                if self.denizaltının_sınıfı=="GÜR":
                    süre_satıh=sinop_kıbrıs/seyir_hızı_satıh_gür
                    süre_dalmış=sinop_kıbrıs/seyir_hızı_dalmış_gür

                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_satıh,"saatte satıhta giderek",self.operasyon_bölgesi,"a ulaşır")
                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_dalmış,"saatte dalmış giderek",self.operasyon_bölgesi,"a ulaşır")




                    
                if self.denizaltının_sınıfı=="PREVEZE":
                    süre_satıh=sinop_preveze/seyir_hızı_satıh_preveze
                    süre_dalmış=sinop_preveze/seyir_hızı_dalmış_preveze

                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_satıh,"saatte satıhta giderek",self.operasyon_bölgesi,"a ulaşır")
                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_dalmış,"saatte dalmış giderek",self.operasyon_bölgesi,"a ulaşır")



                    
                if self.denizaltının_sınıfı=="AY":
                    süre_=sinop_kıbrıs/seyir_hızı_ay

                    print(self.üs,"üssünden kalkan", self.denizaltının_sınıfı, "sınıf denizaltı",süre_dalmış,"saatte giderek",self.operasyon_bölgesi,"a ulaşır")






            elif self.operasyon_bölgesi !="KIBRIS" and self.operasyon_bölgesi !="KIRIM" and  self.operasyon_bölgesi !="RODOS" : #yanlış girişlerde kullanıcıyı uyarır
                print("lütfen operasyon bölgesi olarak RODOS KIRIM veya KIBRIS girin")
        


            
        elif self.üs!="SİNOP" and self.üs!="FOÇA":                                                                            #yanlış girişlerde kullanıcıyı uyarır                                                                          
            print("lütfen üs bölgesi olarak foça veya sinopu seçin")

                          
        
                                                                                        


TCG_GÜR = Denizaltı("tcg_gür",2004,True)
TCG_GÜR.Retire()
TCG_GÜR.sınıflar()
TCG_GÜR.slogan("GÜR")
TCG_GÜR.Deplasman_tonajı("GÜR")
TCG_GÜR.Seyir_menzili("GÜR")
TCG_GÜR.Operasyon_kabiliyeti("GÜR","FOÇA","KIRIM")


TCG_PREVEZE = Denizaltı("20binFersah",1989,False)
TCG_PREVEZE.Retire()
TCG_PREVEZE.slogan("PREVEZE")
TCG_PREVEZE.Deplasman_tonajı("PREVEZE")
TCG_PREVEZE.Seyir_menzili("PREVEZE")
TCG_PREVEZE.Operasyon_kabiliyeti("PREVEZE","SİNOP","RODOS")



