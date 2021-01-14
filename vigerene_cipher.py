class Vigerene():

    def şifre_sıralama(self,girdi,şifre):
        liste=[]
        girdi.upper()
        şifre.upper()
        for i in range(0,len(girdi)):
            sıralanmış_şifre=şifre[i%len(şifre)]
            liste.append(sıralanmış_şifre)
            i+=1
            "".join(sıralanmış_şifre)
            print(sıralanmış_şifre,end="")


    def kodlama(self,girdi,şifre):
        liste=[]
        girdi.upper()
        şifre.upper()
        for i in range(0,len(girdi)):
            x=chr((((ord(girdi[i])-65)+ (ord(şifre[i%len(şifre)])-65))%26)+65)
            liste.append(x)
            i+=1
        print ("".join(liste))
    
    def kod_çözme(self,girdi,şifre):
        liste=[]
        girdi.upper()
        şifre.upper()
        for i in range(0,len(girdi)):
            x=chr((((ord(girdi[i])-65)- (ord(şifre[i%len(şifre)])-65))%26)+65)
            liste.append(x)
            i+=1
        print ("".join(liste))


    


#print(generateKey("BORATASCİ","KALE"))

x=Vigerene()
#x.şifre_sıralama("BORATASCI","KALE")
x.kod_çözme("LOCEDADGS","KALE")
x.kodlama("BORATASCI","KALE")


