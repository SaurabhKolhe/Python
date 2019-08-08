'''       
Tuple:       
      It contain collection data which having different datatype(can contain same datatype)
      i.e we can add number,string,float,boolean,complex in Tuple.
      Tuple is immutable i.e we cannot change any specific value in Tuple.
      Indexing is not supported in tuple.
       
       Syntax:
              Tuple_name=(...data seperated with comma...)
              eg: a=(10,"String",10.45,True,False,1+4j)
'''
a=(10,20,30,40,50,30,30,10)
print(type(a))
print(a)

#There is count() function To check how many times specific value come in tuple:
a.count(20)   #output: 1
a.count(30)   #output: 3

#Indexing is not supported in tuple so we cannot add,delete,modify any value in tuple.

