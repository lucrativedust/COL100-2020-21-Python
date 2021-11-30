# %% Question 1
operators = ["+","-","*","/"]
def brac(s):
    for i in range(len(s)):
    #a represents the index value for the rightmost left bracket "(" upto the index 'i' that appears before the right bracket ")" whenever a is defined.
        if s[i] == "(":
            a = i
        elif s[i] == ")":
            return (a,i)
    #(a,i) represents the indices of the first innermost bracket. Function returns none otherwise (when there are no brackets)
def oper(s):
    #there is no operator symbol for all indices less than m
    for m in range(len(s)):
        #checks for the 4 arithmetic operators
        for i in range(4):
            if s[m] == operators[i]:
                return (m,i)
    #returns (m,i)-the the index value and the type of the operator
    return False
    #returns False if there is no operator
def eval(s):
    #If there is no operator, return the string as it is after converting it to the appropriate float point number
    if not(oper(s)):
        return float(s)
    # y denotes the position (index) of the operator and i denotes the type of the operator
    (y,i) = oper(s)
    #a denotes the number present between the operator and the start of the string
    a = float(s[:y]) if y > 0 else 0
    #b denotes the number present between the operator and the end of the string
    b = float(s[y+1:])
    if i == 0:
        return a+b
    elif i == 1:
        return a-b
    elif i == 2:
        return a*b
    elif i == 3:
        return a / b
    # we return the value of the operation represented by the string
def evaluate(s):
    if brac(s):
        (a,b) = brac(s)
        return evaluate((s[:a])+str(eval(s[(a+1):b])) + s[(b+1):])
    else:
        return eval(s)
# %% Question 2
def sumSequence(n):
    a = [1,2]
    for i in range(2,n):
    #the required list has i items
        c = a[i-1] + 1
        #all values less than c can not be the i+1 th element of the required list so c is the minimum bound for the required answer. We check whether c can be expressed as a sum of the two elements of the list only once.
        while c < a[i-1]+a[i-2]:
            k = 0
            l = i-1
            e = 0
            #values of elements with indices less than k and greater than l cannot be involved in the required sum (c)
            while k<l:
                d = a[k]+a[l]
                if d == c:
                    if e == 0:
                        e = 1
                        k += 1
                        l -= 1
                    else:
                        c += 1
                        break
                elif d>c:
                    l -= 1
                elif d<c:
                    k += 1
            else:
                if e==1:
                    a.append(c)
                    break
                else:
                    c += 1
            #while loop above breaks and we append c if it appears only once else c increases by 1.   
        else:
            a.append(c)
        #last possible case and we append it (only after checking the other cases)  
    return a
    #required list has n items
# %% Question 3
def minLength(a,b):
    n = len(a)
    s = a[0]
    j = 1
    #First While Loop
    while s <= b and j < n:
    #s is less than required sum 'b' and the index of the element we are adding to s 'j' is still in the list.
        s += a[j]
        j += 1
    if s <= b:
        ans = -1
    else:
        ans = n
    i = 1
    #if s <= b then j must have become equal to n for the loop to break. In this case, we have checked all possible sums involving the first element. If s>b, the value of j <= n is stored and we check whether the other sums can exceed b while requiring less than j elements.

    #Second While Loop
    while i < n:
    #j > 1 represents the minimum number of elements required to exceed the required sum. We initialize 's' to the first element.
        s = a[i]
        if s > b:
            return 1
        for k in range(i+1,min(n,i+j)):
        #s<=b and the number of elements we have checked is less than j while also ensuring that these indices are not greater than n-1.
            s += a[k]
            if s > b:
                j = k-i + 1
                break
        #if we get s>b, then the value of j is updated and the for loop is broken. Otherwise, j remains the same as before.
        i += 1
    #the value of j has changed if it was possible to express the sum using less than j elements, otherwise it remains same. Now, we find this sum for the next element.
    if j==n:
        return ans
    else:
        return j
    #we checked the value of the sum s starting from all elements and return the output accordingly.
# %% Question 4
def merger(L,L2,i,block):
    n = len(L)
    j = i
    k = i + block
    l = i
    while k < min(n,i+(2*block)) and j<i+block:
    #all the elements occuring before k and j in their respective blocks have been added to the second list in a sorted manner.
        if L[j][0]<L[k][0]:
            L2[l]=L[j]
            l += 1
            j += 1
        else:
            L2[l]=L[k]
            l += 1
            k += 1
    #all the elements that have been added to the second list till we run out of elements in one of the blocks have been added in a sorted manner and the remaining elements are larger than these elements.
    else:
        while j < min(n,i+block):
        #elements remaining in the first block before j have been added in a sorted manner
            L2[l]=L[j]
            l += 1
            j += 1
        #elements of the first block have been placed in a sorted manner
        while k < min(n,i+2*block):
        #elements remaining in the second block before k have been added in a sorted manner
            L2[l]=L[k]
            l += 1
            k += 1
        #elements of the second block have been placed in a sorted manner
    return L2
def sorter(L):
    block=1
    drn = 0
    n = len(L)
    L2 = [0]*n
    while block<n:
    #elements in a block of length 'block' are sorted
        for i in range(0,n,2*block):
        #all elements with indices less than i are sorted in blocks of length '2*block'
            if drn%2 == 0:
                L2 = merger(L,L2,i,block)
            else:
                L = merger(L2,L,i,block)
        #all elements in are sorted in blocks of length '2*block'
        drn += 1
        block *= 2
    #the full list is sorted          
    else:
        if drn %2 == 0:
            return L
        else:
            return L2
def mergeContacts(A):
    A = sorter(A)
    i = 0
    B = []
    while i < len(A):
    #all the emails appearing before the index i have been associated to a name
        c = []
        if i+1 > len(A)-1 or A[i][0] != A[i+1][0]:
            c.append(A[i][1])
            B.append((A[i][0],c))
            i += 1
        else:
            temp = A[i][0]
            c.append(A[i][1])
            j = i+1
            while j < len(A):
            #all the emails corresponding to the first occurence of the current name 'temp' till the index j in the sorted list A have been appended to the list c
                if A[j][0]==temp:
                    c.append(A[j][1])
                    j+=1
                else:
                    i=j
                    B.append((temp,c))
                    break
            #either we run out of list items (j==len(A)) or we find an item with a different name. In this case, we break the while loop and append the tuple (name,c) to the output list B.
            if j==len(A):
                B.append((temp,c))
                break
            #we append the tuple (name,c) to the output list B.
    #each email has been associated with the appropriate name. 
    return B

#%%
print("Test cases\n")

# 1
print("\n Q1...")
print(evaluate("((2.78+0.003)/(4+5))")) #0.30922222222222223 
print(evaluate("(((10.78+789.003)/(4478-5))*(3.478-0.88))")) #0.46452855667337367 
print(evaluate("(((7.789-0.124)*(2.233/10.011))-((.003+1.1001)/(0.455+1.1)))")) #1.0003247472796004 
print(evaluate("(((1.77*97.00001)+(1.001/0.178))-191.111)"))#-13.797386794382021 
print(evaluate("(1.478+(1.0001-0.1789))/(1.455/(.1789/.000147))")) #1923.121677536994 
print(evaluate("1.563-(0.178*(7.8999/(1+(0.007+1.4888))))"))#0.9995805753666159 
print(evaluate("(2*(3*(5*7)))*9"))#1890.0
print(evaluate("(9/(1*(5+(4*4))))*10"))#4.285714285714286
 

# 2
print("\n Q2...")
print(sumSequence(45)); '''[1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, 57, 62, 69, 72, 77, 82, 87, 97, 99, 102, 106, 114, 126, 131, 138, 145, 148, 155, 175, 177, 180, 182, 189, 197, 206, 209, 219, 221]''' 
print(sumSequence(105)[-1]) #734 
print(sumSequence(256)[-1])  #2552 
print(sumSequence(512)[-1]) #5856 
 

# 3
print("\n Q3...")
print(minLength([4,5,-9,0,4],10)) #-1 
print(minLength([4,5,-9,0,-1,7,-3,10],13)) #3 
print(minLength([-4,5,-1,7,-3,10,-4,15,-7],25)) #7 
print(minLength([3,-1,4,-5,-10,11,-4,-17,3,45,11,-23],50)) #2 
print(minLength([1,0,0,1,0,0,-1,0,0,1,0,1,0,1],4)) #-1 
print(minLength([1,0,0,1,0,0,-1,0,0,1,0,1,0,1],2)) #5 
 
# 4
print("\n Q4...")
print(mergeContacts([("A","a@xyz.com"),("A","a1@xyz.com"),("B","b@xyz.com"),("A","a2@xyz.com")])) 
# [('A', ['a1@xyz.com', 'a2@xyz.com', 'a@xyz.com']), ('B', ['b@xyz.com'])]

print(mergeContacts([("A","a@xyz.com"),("B","b@xyz.com"),("C","c@xyz.com"),("D","d@xyz.com"),("E","e@xyz.com"),("A","a1@xyz.com")])) 
# [('A', ['a1@xyz.com', 'a@xyz.com']), ('B', ['b@xyz.com']), ('C', ['c@xyz.com']), ('D', ['d@xyz.com']), ('E', ['e@xyz.com'])]

print(mergeContacts([("AN","anu@gmail.com"),("PS","paraskangra3@gmail.com"),("RN","narain@cse"), ("HS","saran@cse"),("AN","anu5@gmail.com"),("AN","anu3@gmail.com"), ("RN","Rahul.Narain@iitd"), ("RN","Rahul.Narain2@iitd"),("PS","paraskangra1@gmail.com"),("PS","paras2@gmail.com"),("PS","paras10@gmail.com")])) 
#[('AN', ['anu3@gmail.com', 'anu5@gmail.com', 'anu@gmail.com']), ('HS', ['saran@cse']), ('PS', ['paras10@gmail.com', 'paras2@gmail.com', 'paraskangra1@gmail.com', 'paraskangra3@gmail.com']), ('RN', ['Rahul.Narain2@iitd', 'Rahul.Narain@iitd', 'narain@cse'])]
 
#%%