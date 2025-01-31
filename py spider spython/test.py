#strs=['flower','flow',"flight"]
def isMagic(num):
    sum=0
    while (num!=0):
        last=num%10
        sum+=last
        num//=10
    if 0>= sum <=9:
        if sum==1:
            print("Magic Number")
        else:
            print("not Magic Number")
    else:
        isMagic(sum)

num= int(input("enter the number :"))
isMagic(num)





