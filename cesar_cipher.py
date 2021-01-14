def şifreleme(self,string,shift):
    liste=[]
    for i in range(len(string)):
        harf=string[i]
        if harf.isupper():
            y=chr((ord(harf)-65+shift)%26 +65)
            liste.append(y)
        elif harf.islower():
            x=chr((ord(harf)-97+shift)%26 +97)
            liste.append(x)
        
        i+=1

    print( "".join(liste))



