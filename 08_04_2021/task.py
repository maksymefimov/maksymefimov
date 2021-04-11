## task 1
msg = "Maksym Efimov"
## task 2
print (msg)
##
msg = msg * 3
print (msg)
msg = msg + " Efimov"
print (msg)
## task 4
msg = "Maksym Efimov"
hello = "Hello"
print(hello + msg)
hello += " "
print(hello + msg)
## task 5 v1
msg = "Maksym Efimov"
msg = msg.replace(" "," Petrovych ")
print(msg)
## task 5 v2
msg = "Maksym Efimov"
msg = msg[0:6]
msg = msg + " Petrovych Efimov"
print(msg)
## task 6
s = "colorless"
s = s[0:4]
s += "urless"
print(s)
## task 7
a = "dish-es"
b = "run-ning"
c = "nation-ality"
d = "un-do"
e = "pre-heat"
a = a.replace('-','')
b = b.replace('-','')
c = c.replace('-','')
d = d.replace('-','')
e = e.replace('-','')
print(a," ",b," ",c," ",d," ",e," ")
##OR
a = "dish-es"
b = "run-ning"
c = "nation-ality"
d = "un-do"
e = "pre-heat"
a = a[0:4] + a[5:7]
b = b[0:3] + b[4:8]
c = c[0:6] + c[7:13]
d = d[0:2] + d[3:5]
e = e[0:3] + e[4:8]
print(a," ",b," ",c," ",d," ",e," ")
## task 8
python_zen = "Beautiful is better than ugly\n\
Explicit is better than implicit\n\
Simple is better than complex\n\
Complex is better than complicated\n\
Readability counts"
print("\n%s"%python_zen)
print("\n%s"%python_zen.lower())
print("\n%s"%python_zen.upper())
## task 9
num = str(input("Input 4-digits number: "))
dnum= int(num[0])*int(num[1])*int(num[2])*int(num[3])
print ("Product of a number: ",dnum)
num = num[::-1]
print ("Reverse number: ",num)
