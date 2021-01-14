import math
"""class Ceasar_box_cipher():

    def coding(self,string):
        liste=[]
        string=string.replace(" ","")
        line_length=len(string)
        y=math.sqrt(len(string))
        if y==float:
            y=int(y+1)
        
        i=int()
        z=int()

        while i<y:
            while z<line_length:
                liste.append(string[z])
                z+=y
            i+=1
        
        print("".join(liste))
                



x=Ceasar_box_cipher()
x.coding("bugün saat ikide saldırıyoruz")
"""
class Ceasar_box_cipher():

    def coding(self,string):
        string=string.replace(" ","")
        result=""
        y=math.sqrt(len(string))
        if y==float:
            y=int(y+1)
        for i in range (0,int(y)):
            b=i
            while b<len(string):
                result+=string[int(b)]
                b+=y
        print(result)
x=Ceasar_box_cipher()
x.coding("greatjobyougotit")
x.coding("gtyorjoteouiabgt")


            
