# kısıtlı özelliklere sahip çakma e-devlet 

from pickle import TRUE


print ("1-üye ol")
print ("2-giriş yap")

while TRUE: 

    secenek = int(input("seçiminizi yapın: "))   

    if secenek >2 or secenek <0:       
        print ("işleminiz geçersizdir. Tekrar deneyin")
        break

    elif secenek ==1:

        kullanıcılar = {}
        name = input ("adınız: ")
        surname = input ("soyadınız: ")
        Tc = input ("tc: ")
        şifre = input ("şifre girin: ")

        kullanıcılar.update ({Tc and şifre:
                              {"adı": name,
                               "soyadı": surname}})
        print ("tebrikler kaydınız oluşturuldu.", kullanıcılar)
        
    else:
        Tc = int(input ("tc: "))
        şifre = int(input ("şifre girin: "))

        kullanıcılar = {Tc: 1111, şifre: 1111, "adı": "emre"}               
        
        if (Tc==kullanıcılar[Tc]) and (şifre==kullanıcılar[şifre]):
                
                print("Merhaba", kullanıcılar["adı"])
                dogumyili = int(input("doğum yılınızı girin: "))

                def yashesapla(dogumyili):

                    
                    import datetime
                    yıl = int(datetime.date.today().year)

                                   
                    return (yıl-dogumyili) 
                              
                age = yashesapla(dogumyili)
                def emeklilikkaldi(age):
                    return (47-age)
                    
                kalan = emeklilikkaldi(age)

                if kalan > 0:                                                             
                    print ("emekliliğinize" ,kalan, "yıl kaldı")
                else:                      
                    print ("emeklisiniz")
        else:
            print ("yanlış kullanıcı bilgileri. Anasayfaya aktarılıyorsunuz...")

