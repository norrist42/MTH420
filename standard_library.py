
"""Python Essentials: The Standard Library.
<Timothy Norris>
<MTH420>
<02/12/2018>
"""


# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order).
    """

    maximum = max(L)
    minimum = min(L)
    average = sum(L)/ len(L)
    
    return maximum, minimum, average

list = [1,3,6,24,42,13]
print(list)
max, min, ave = prob1(list)
print(max)
print(min)
print(ave)
    



# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test numbers, strings, lists, tuples, and sets. Print your results.
    """

    myList = [13,17,22,38,46]
    myList2 = myList
    myList[0] = 0
    
    stringList = ["Solomon", "Josiah", "Isaiah"]
    stringList1 = stringList
    stringList[0] = "null"
    
    Tuple = (87,45,42)
    Tuple1 = Tuple
    Tuple += (1,)
	
    franzList = ['C Major', 'F Minor', 'Crescendo', 'Octavius']
    list = franzList
    franzList[len(franzList):] = 'random'

    if myList== myList2:
        print("mutable")
    else:
        print("no")
    
    if stringList1== stringList:
        print("mutable")
    else:
        print("no")
	
    if Tuple == Tuple1:
        print("mutable")
    else:
        print("no")
    
    if list == franzList:
        print("mutable")
    else:
        print("no")
	
prob2()   

# Problem 3
def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than those that are imported from your
    'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    import math
    hyp = math.sqrt(a**2+b**2)
   
    print("The hypotenuse is: ", hyp)
    return hyp

hypot(5,5)

# Problem 4
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.
        
    

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    
    import itertools
    from itertools import combinations, permutations
    
    PowerA = []
    
    A3 = combinations(A,3)
    A2 = combinations(A,2)
    A1 = combinations(A,1)
    A0 = combinations(A,0)    
    PowerA.append(set(A3))
    PowerA.append(set(A2))
    PowerA.append(set(A1))
    PowerA.append(set(A0))

    
    print(PowerA)
    

setA = "abc"
power_set(setA) 
    
    



# Problem 5: Implement shut the box.
