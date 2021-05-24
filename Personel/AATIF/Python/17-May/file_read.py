# file = open('demo.txt','r')
# for each in file:
#     print (each)

with open("demo.txt","r") as file:
    data= file.readline()
    for line in data:
        word = line.split()
        print(word)