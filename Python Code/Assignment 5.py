#%% Question 1
def gridPlay(grid):
    #Assertion 1: A[i][j] represents the minimum penalty from the cell (m-i,n-j) to the last cell. So, we wish to calculate A[-1][-1] or A[m-1][n-1] which is equivalent to the least penalty from the cell (1,1) to the last cell.
    A = []
    #The following is our base case. 
    #A[0][0]=grid[-1][-1]
    A.append([grid[-1][-1]])
    #When we reach the last row of the grid, we can only move rightwards. So, we add the value of the current cell to A[0][i-1] to get the value of A[0][i].
    #For Loop 1
    for i in range(1,len(grid[0])):
        #Assertion 1 holds for all elements of A[0] till A[0][i-1].
        A[0].append(A[0][i-1]+grid[-1][-i-1])
    #Now, we have the first row of the matrix A.    
    #When we reach the last column of the grid, we can only move downwards. So, we add the value of the current cell to A[i-1][0] to get the value of A[i][0].
    #For Loop 2
    for i in range(1,len(grid)):
        #Assertion 1 holds for all elements A[k][0] till A[i-1][0].
        A.append([A[i-1][0]+grid[-i-1][-1]])
    #Now, we have the first column of the matrix A.   

    #Assertion 2
    #Now we know how to go the last cell from the last row and the last column. So, we fill A row-wise from the top, as the minimum of the elements above, to the left and to the top-left of the current element in A will tell us in which direction we should move (down, right, down-right respectively).
    #Outer For Loop
    for i in range(1,len(grid)):
        #First we fill the i-th row and then we fill the next row and so on. Assertion 1 holds for all rows till i-th row.
        #Inner For Loop
        for j in range(1,len(grid[0])):
            #Assertion 1 holds for all elements till the i-th row and all elements of i-th row till A[i][j-1].
            A[i].append(min(A[i-1][j-1],A[i-1][j],A[i][j-1])+grid[-i-1][-j-1])
        #We have the i-th row of the matrix A.
    #We have all the rows of the matrix A and A[-1][-1] represents the answer so we return it.
    return A[-1][-1]
#%% Question 2
vowels = ["a","e","i","o","u"]
def vowelcheck(x):
    for y in vowels:
        if x == y:
            return True
    return False
def stringProblem(A,B):
    c = []
    #Assertion 1
    #c[k] represents the required value if we consider the first k characters of the string B and the all the characters before the current character in consideration for the string A.
    #For Loop 1
    for i in range(len(B)+1):
        #Initially we have not considered any characters of the string A. So c[k] = k, as we just have to insert all the k characters in the correct order and that will take k steps.
        c.append(i)
    #Now we know the required output if we do not consider any character of the first string.
    #Assertion 2
    #d represents the list of minimum number of changes required if we take all the characters of the string A including the current character ii.
    #Outer For Loop
    for i,ii in enumerate(A):
        #Assertion 1 holds
        #d represents the list of minimum number of changes required if we take the first characters of the string A till the character ii and d[k] represents minimum number of changes required to convert this part of the string A to the first k characters of string B.
        #Initially, we do not consider any element of the second string. So, to convert A to B (empty string), we will have to delete all the characters and that would take i+1 steps. So, initially d[0]= i+1.
        d = [i+1]
        #Inner For Loop
        for j,jj in enumerate(B):
            #all elements of d, that is d[k] represents the minimum number of changes required if we take the first k characters of the second string B and all characters of A till the current character.
            if ii == jj:
                d.append(c[j])
            else:
                if vowelcheck(ii):
                    if vowelcheck(jj):
                        d.append(1 + min(d[j],c[j+1],c[j]))
                    else:
                        d.append(1 + min(d[j],c[j+1]))
                else:
                    d.append(1 + min(d[j],c[j+1],c[j]))
        #Assertion 2 holds.
        #Now, we are going to consider the next character of the string A as well, so we set c=d for the next character as i increases by 1.
        c = d
    #As we consider all elements of the string A, c[-1] represents the minimum number of changes required if we want to convert string A to the string made up by considering all the characters of the string B. So, we return c[-1] as the output.
    return c[-1]
#%% Question 3
def fr(i):
    if i == 0:
        return "   "
    elif i//10 == 0:
        return "  "+str(i)
    else:
        return " " + str(i)
def g(i):
    l = len(i)
    x = ""
    if l%2 == 0:
        x += " "
    x += " "*((19-l)//2) + "-" + i + "-" + " "*((19-l)//2)
    return x
def printCalendar(year):
    C = (year-1)//100
    D = (year-1)%100
    x = (29 +D+ (D//4) +(C//4)-(2*C))%7
    y = False
    if year%4 == 0:
        if year%100 != 0 or year%400 == 0:
            y = True
    monthstart = []
    monthstart.append(x)
    monthstart.append((monthstart[-1]+31)%7)
    if y:
        monthstart.append((monthstart[-1]+29)%7)
    else:
        monthstart.append((monthstart[-1]+28)%7)
    monthstart.append((monthstart[-1]+31)%7)
    monthstart.append((monthstart[-1]+30)%7)
    monthstart.append((monthstart[-1]+31)%7)
    monthstart.append((monthstart[-1]+30)%7)
    monthstart.append((monthstart[-1]+31)%7)
    monthstart.append((monthstart[-1]+31)%7)
    monthstart.append((monthstart[-1]+30)%7)
    monthstart.append((monthstart[-1]+31)%7)
    monthstart.append((monthstart[-1]+30)%7)
    monthlen = []
    monthlen.append(("January",31))
    if y:
        monthlen.append(("February",29))
    else:
        monthlen.append(("February",28))
    monthlen.append(("March",31))
    monthlen.append(("April",30))
    monthlen.append(("May",31))
    monthlen.append(("June",30))
    monthlen.append(("July",31))
    monthlen.append(("August",31))
    monthlen.append(("September",30))
    monthlen.append(("October",31))
    monthlen.append(("November",30))
    monthlen.append(("December",31))
    z = " "*34 + str(year) + " "*35 + "\n"*2
    #def block(z):
    i = 0
    k = 0
    start = [0,0,0]
    while i < 12:
        for j in range(i,i+3):
            if k == 0:
                z += g(monthlen[j][0])
            elif k == 1:
                z += "  S  M  T  W  T  F  S"
            elif k == 2:
                for starter in range(7):
                    if starter == monthstart[j] or start[j-i]>0:
                        start[j-i] += 1
                    z += fr(start[j-i])
            elif start != [0,0,0]:
                for _ in range(7):
                    if start[j-i] < monthlen[j][1] and start[j-i]>0:
                        start[j-i] += 1
                    z += fr(start[j-i])
                    if start[j-i] == monthlen[j][1]:
                        start[j-i] = 0
            else:
                k = -1
                i += 3
                z += "\n"
                break
            if j-i != 2:
                z += " "*5
        k += 1
        z += "\n"
        if k == 1:
            z += "\n"
    f = open("calendar.txt", "w")
    f.write(z)
    f.close()
    return z

#%%
#3.1 Testcases
#printCalendar(1780) 
#printCalendar(1900)
#printCalendar(2000)
#printCalendar(2145)
# %%
#1.1 Testcases 
grid1 = [[4, 8, 2, 4, 7, 1, 6, 2, 10]]

grid2 = [[2],[8],[9],[12],[2],[4],[1],[3]]

grid3 = [[2,4],[8,1],[9,2],[12,8],[2,1],[4,5],[1,6],[3,1]]

grid4 = [[2,4,3,1,4,2,7,8],[5,1,4,6,1,2,3,1]]

grid5 = [[8,6,2,1],[40,2,1,4],[2,3,70,5],[60,1,2,4],[7,7,75,2],[2,6,9,100],[22,2,3,1],[2,3,3,30],[2,1,2,4],[1,22,1,1]]

print(gridPlay(grid1))#44
print(gridPlay(grid2))#41
print(gridPlay(grid3))#26
print(gridPlay(grid4))#17
print(gridPlay(grid5))#35


# 2.1 Testcases
A0 = "delhi"
B0 = "mumbai"
print(stringProblem(A0, B0))#5

A1 = "samsung"
B1 = "apple"
print(stringProblem(A1, B1))#6

A2 = "brontosaurus"
B2 = "tyrannosaurus"
print(stringProblem(A2, B2))#4

A3 = "test"
B3 = "thisdoesnothavetobeoneword"
print(stringProblem(A3, B3))#22

A4 = "supercalifragilisticexpialidocious"
B4 = "computers"
print(stringProblem(A4, B4))#30





#%%