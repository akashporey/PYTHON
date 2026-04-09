class number:
    def __init__(self,num):
        self.num=num
    def is_positve(self):
        if(self.num>0):
            print("It's a positive number")
        elif(self.num==0):
            print("It's Neither positive nor negetive")
        else:
            print("It's a negetive number")

num= int(input("Enter a number: "))
n1=number(num)
n1.is_positve()