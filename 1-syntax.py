print("Hello World!")

# no explicit variable types
a=2
b=3
name = "Ruben"

print("name type: {}".format(type(name)))
print("Hello {}!\n".format(name))

# identation! 
if a+b == 0:
    print("a+b is zero value")
elif a+b > 0:
    print("a+b is positive value")
else:
    print("a+b is negative value")
    
    
a_list = [a, b, 2, 7]
print("\n a_list:")
print(a_list)
print(a_list[1:3]) # without number is same as first/last index, check negative values

print("\n Using while:")
i=0
while i < len(a_list):
    print("index: {}, value: {}".format(i, a_list[i]))
    i+=1
    
print("\n Using for:")
for j in range(4):
    print("index: {}, value: {}".format(j, a_list[j]))
    
print("\n Using for in a smart way:")
for value in a_list:
    print("value: {}".format(value))
