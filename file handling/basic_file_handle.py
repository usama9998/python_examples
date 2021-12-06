
f=open("MyData.txt",'r')
# f1=open("abc.txt",'w')
# f1.write("Hello it's working")

######### I will read a file form MyData.txt and will write it in abc.txt  #######

with open("abc.txt", 'w') as f1:  ##### line as corresponding to f=open("abc.txt", 'w')
    for line in f:
        print("writing -> ", line)
        f1.write(line )

with open("MyData.txt","a") as f1:
    f1.write("It's appending again")

f4=open('image.png','wb')
with open("Capture.PNG", "rb") as f3:      #### to read image use rb
    for i in f3:
        f4.write(i)
   
