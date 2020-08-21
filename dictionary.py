#Dictonary in python test  

ingredients = {
    "bread" : {0: "chapathi",1:"naan"},
    "fruits" : {0: "banana",1:"apple"}
}
#print(ingredients.get("bread"))

#Number of words of sentence
 
sentence = "i am going i am coming i was going"
words = sentence.split(" ")

thisdict = {}

for i in words:
    if( thisdict.get(i) == None ):
        thisdict[i] = 1
    else:
        thisdict[i]+=1

#using .items(), .keys(), .values()

#print( thisdict.items() ) 
#print( list(thisdict.items()) )

#print( thisdict.keys() ) 
#print( list(thisdict.keys()) )

#print(thisdict.values() ) 
#print( list(thisdict.values()) ) 

#updating of dictionary

#print ( thisdict.pop("going--> popping last tuple") )
#print(thisdict)

#pop last item
#print ( thisdict.popitem() )
#print(thisdict)

#clearing entire dictionary
#thisdict.clear()

list_21 = list(thisdict.values())
print(list_21)
list_21.sort()
print(list_21)