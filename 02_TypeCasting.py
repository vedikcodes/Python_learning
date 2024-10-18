 #TypeCasting = the process of converting a variable from one data type to another
#      str() , int() , float() , bool()

name= ""
age =22
gpa =8.9
is_student =True
 
 #to know the kind of datatype we using we use type() function

print(type(name)) #string
print(type(age)) #int
print(type(gpa))  #float
print(type(is_student)) #bool

gpa =int(gpa) #typecasting float to int
print(gpa)

age =str(age)
print(age) #result will remain the same
print(type(age))  #but the type changed to str

#age +=1
#print(age) #can only concatenate str (not "int") to str

age += "1" #  will give 221
print(age)

name = bool(name)
print(name) #True

name = ""
print(name) #false

