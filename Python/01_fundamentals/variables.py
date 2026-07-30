import math
V_m = 220
f = 50
t = 0.005

omega = 2*3.1415*f
V_t = V_m * math.cos(omega * t)

print(V_t)


#-------------------------------

print(type(t)) #finding variables type

#str(string) data type
name = "Amir mohammad" #we can use ' ' instead of " "

#bool(boolian) data type
online = False #only 2 possible values : True or False

#other data types are list, Tuple , dict ,set etc.

