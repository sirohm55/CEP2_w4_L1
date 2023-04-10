#-------------------------------------------------------------------------------
# Name:        w4_lecture_1
# Purpose:
#
# Author:      STUDENT (tan jun yan)
#
# Created:     10/04/2023
# Copyright:   (c) STUDENT 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#name = "heloo"
#x = type (name)
#print (x)
#print ("""'Hi', my name  is "Jamme" """)


'''
Array_list = ['name', 12 , 17.2]
Array_Tuple = ("jason", 65, 225.3)

for x in range (0,3,1):
    print (Array_list [x])
    print (Array_Tuple [x])

Array_list [x] = "Tan"
#Array_Tuple [x] = 555
print ("\n")

for x in range (0,3,1):
    print (Array_list [x])
    print (Array_Tuple [x])
'''

#Exercise
#a)
'''
a="All"; b=" work"; c=" and"; d=" no"; e=" play"
f=' makes'; g=' Jack'; h=' a'; i=' dull'; j=' boy'

print (a+b+c+d+e+f+g+h+i+j)

#b)

print (6*(1-2))

#c)

#print (6*(1-2))

#d)
'''
'''
#e)

P = float (input ("Input the value of P:"))
r = float (input ("Input the value of r, %:"))
r = r/100
n = float(input ("Input the value of n:"))
n = int(n)
t = float(input ("Input the value of t:"))
t = int (t)
A = P*((1+(r/n))**(n*t))
print ("%.2f" % A)
'''
#h)

hours = int (input ("time now :"))
wait = float (input ("waiting hours? :"))
waitmin = (wait % 1)
wait -= waitmin
waitmin *= 60
alarm = hours + (wait*100) + waitmin
min = (alarm % 100)
if (min >= 60):
    alarm = (alarm - 60) + 100
while (alarm >= 2400):
    alarm = alarm - 2400

print ("Your alarm goes off at", int(alarm))

