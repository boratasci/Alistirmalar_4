import math

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



            
