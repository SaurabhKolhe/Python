'''
Set:
    It contain collection data which having different datatype(can contain same datatype)
    i.e we can add number,string,float,boolean,complex in set.
    set is mutable as by add() fuction we can add any value.
    Indexing is not supported in set.
     #it contain only unique value i.e. it will not print duplicate value i.e it will print any value only one time.
       
    Syntax:
           set_name={...data seperated with comma...}
           eg: a={10,"String",10.45,True,False,1+4j}
'''
a={10,20,30,10,"saurabh"}
print(type(a))
print(a)      #it contain only unique value i.e. it will print 10 only one time i.e {20,10,"saurabh",30}

#There is add() function to add value in set 
a.add(50)
