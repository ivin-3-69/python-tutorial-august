items = ['apple','Banana','Orange']
counts = [4,7,2]
price = [27,65,18]
sentence = []
zipped_list = list(zip(items,counts,price))
unzipped = list( zip(*zipped_list))

for x,y,z in zipped_list:
    a = " i bought "+str(y)+" "+str(x)+"s at Rp"+str(z)
    sentence.append(a)

print(sentence)
