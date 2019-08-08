'''
Dictionary:
           1.class of dictionary : dict
           2.Indexing is not supported in Dictionary.
           3. Dictionary is mutable i.e. we can add,delete,modify in dictionary using key.
           
           Syntax:
                  a={key:value,key:value}
                  eg. student={"Name":"Shrikant","Roll":10}
'''

a={"Name":"Saurabh","Roll":20}
print(type(a))
print(a)        #output: {'Name': 'Saurabh', 'Roll': 20}
#To print specific value
print(a["Name"])

#To change any value
a["Name"]="Akki" 

#To add any value
a["Age"]=20  

#we can also add by update fuction
a.update({"city":"talegoan"})

#To print only keys in dictionary
print(a.keys())

#To print only values in dictionary
print(a.values())

#To print keys and values both in dictionary
print(a.items())    #output: dict_items([('Name', 'Saurabh'), ('Roll', 20)])
