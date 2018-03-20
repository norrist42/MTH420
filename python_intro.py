
"""Python Essentials: Introduction to Python.
<Timothy Norris Jr.>
<MTH 420>
<01/12/2018>
"""

#Problem 1
if __name__ == "__main__":
    print("Hello, world!")

#Problem 2 
def sphere_volume(r):
    pi = 3.14159
    volume = (4/3)*pi*r**3
    return volume

print(sphere_volume(2))

#Problem 3
def isolate(a, b, c, d, e):
    print(a, b, sep = "     ")
    print(c,d,e, sep = "  ")

isolate(1, 3, 5, 6, 13)

#Problem 4
#The possible parameter is listed below  
# string = "longword"

def first_half(astring):
    num_letters = len(astring)//2
    print(astring[:num_letters])

def backward(thestring):
    back_string = thestring[-1::-1]
    print(back_string)


myword = "longestword"
first_half(myword)

backward(myword)


#Problem 5
#Lists

def list_ops(thelist):
    thelist.append("eagle")
    print(thelist)

    thelist[2] = "fox"
    print(thelist)

    thelist.remove(thelist[1])
    print(thelist)

    thelist.sort()
    thelist = thelist[-1::-1]
    print(thelist)

    thelist[3] = "hawk"
    print(thelist)

    thelist.append("hunter")
    print(thelist)

aList = ["bear", "ant", "cat", "dog"]
list_ops(aList)


#problem 6
#sets

def pig_latin(word):
    print(word)

    #if the word starts with a vowel
    if word[0] in "aeiou":
        return word +"hay"
    else:
    	return word[1:] + word[0] + "ay"  
    	   
print(pig_latin("example"))
'''        
#Problem 7
def palidrome():
	
    largest_prod = 0
    product = 0
    for i in range(100,1000):
        for j in range(100,1000):
            if str(i*j) == backward(str(i*j)):
                product = i*j
                
            if product > largest_prod:
               largest_prod = product
    
    return largest_prod

print(palidrome())
'''   
         
                
        
              
       
