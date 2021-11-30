#%% Question 1
class Course:
    def __init__(self,a,b):
        self.courseCode = a
        self._quizlist = b
class Quiz:
    def __init__(self,a,b):
        self.title = a
        self._correctoptionslist = b
class Student:
    def __init__(self,a,b):
        self.entryNo = a
        self._courselist = b
        #stores the information about quizzes (no answer if not attempted and the answers of the first attempt if attempted)
        self._dict_quizzes = {}
        #stores the correct answer corresponding to the quiz
        self._dict_answers = {}
        for i in self._courselist:
            self._dict_quizzes[i.courseCode] = {}
            for j in i._quizlist:
                self._dict_quizzes[i.courseCode][j.title]= []
        for i in self._courselist:
            self._dict_answers[i.courseCode] = {}
            for j in i._quizlist:
                self._dict_answers[i.courseCode][j.title]= j._correctoptionslist
    def attempt(self,courseCode,quizTitle,attemptedAnswers):
        #ignore if attempt exists, if it does not then add it
        if self._dict_quizzes[courseCode][quizTitle]:
            pass
        else:
            self._dict_quizzes[courseCode][quizTitle] = attemptedAnswers
    def getUnattemptedQuizzes(self):
        output = []
        for i in self._courselist:
            for j in i._quizlist:
                #ignore if attempt exists, if it does not then return the details
                if self._dict_quizzes[i.courseCode][j.title]:
                    pass
                else:
                    output.append((i.courseCode,j.title))
        return output
    def getAverageScore(self, courseCode):
        sigma = 0
        n = 0
        for i in self._dict_quizzes[courseCode]:
            #check whether the quiz is attempted or not
            if self._dict_quizzes[courseCode][i]:
                n += 1
                score = 0
                for j,jj in enumerate(self._dict_quizzes[courseCode][i]):
                    #if the answer matches, increase the score by 1
                    if jj == self._dict_answers[courseCode][i][j]:
                        score += 1
                sigma += score
        if n == 0:
            return 0
        else:
            return sigma/n
#%% Question 2
class Matrix:
    def __init__(self,mt):
        self.mt = mt
    def __str__(self):
        o = ""
        for i in self.mt:
            for j in i:
                o += str(j)
                o += " "
            o += "\n"
        return o
    def __add__(self,mt2):
        #check whether dimensions match
        if len(self.mt) != len(mt2.mt) or len(self.mt[0]) != len(mt2.mt[0]):
            raise Exception('Matrix Dimensions do not match')
        z = []
        #make a list corresponding to each row of the resulting matrix
        for i,ii in enumerate(mt2.mt):
            z.append([])
            #add corresponding elements and then append them to the list
            for j,jj in enumerate(ii):
                z[-1].append(jj+mt2.mt[i][j])
        return Matrix(z)
    #similar to addition, just subtract the two elements
    def __sub__(self,mt2):
        if len(self.mt) != len(mt2.mt) or len(self.mt[0]) != len(mt2.mt[0]):
            raise Exception('Matrix Dimensions do not match')
        z = []
        for i,ii in enumerate(mt2.mt):
            z.append([])
            for j,jj in enumerate(ii):
                z[-1].append(jj-mt2.mt[i][j])
        return Matrix(z)
    def __mul__(self,mt2):
        a = self.mt
        #for scalar multiplication
        if not(isinstance(mt2,Matrix)): 
            c = self.mt.copy()
            for i in range(len(c)):
                for j in range(len(c[0])):
                    c[i][j] *= mt2
        #for matrix multiplication
        else:
            b = mt2.mt
            c = []
            if len(b) != len(a[0]):
                raise Exception('Matrix Dimensions do not match')
            #make a list corresponding to each row of the resulting matrix
            for i,ii in enumerate(a):
                c.append([])
                #calculate the value of each element of the resulting matrix's row and then append it
                for k in range(len(b[0])):
                    d = 0
                    #calculating value of the element
                    for j,jj in enumerate(ii):
                        d += jj*b[j][k]
                    c[-1].append(d)
        return Matrix(c)
    def toSparse(self):
        S = []
        #make a list corresponding to each row of the resulting matrix
        for i in self.mt:
            S.append([])
            for jj,j in enumerate(i):
                #if the element is non-zero, append the tuple corresponding to it
                if j != 0:
                    S[-1].append((jj,j))
        return SparseMatrix(S,len(self.mt),len(self.mt[0]))
class SparseMatrix:
    def __init__(self,sparse_matrix,nrows,ncols):
        self.spmat = sparse_matrix
        self.ncols = ncols
        self.nrows = nrows
    def __str__(self):
        a = ""
        for i in range(self.nrows):
            j = 0
            k = 0
            for k in range(self.ncols):
                if j < len(self.spmat[i]) and self.spmat[i][j][0] == k:
                    a += str(self.spmat[i][j][1]) + " "
                    j +=1
                else:
                    a += "0 "
            a += "\n"
        return a
    def __add__(self,b):
        if self.nrows != b.nrows or self.ncols != b.ncols:
            raise Exception('Matrix Dimensions do not match')
        S = []
        for i in range(self.nrows):
            S.append([])
            j = 0
            k = 0
            for l in range(self.ncols):
                #check whether the index of the current element is equal to any of the elements in the two matrices and if one or more items have those index perform the corresponding action
                if j < len(self.spmat[i]) and k < len(b.spmat[i]) and self.spmat[i][j][0] == l and b.spmat[i][k][0] == l:  
                    if (self.spmat[i][j][1]+b.spmat[i][k][1]) != 0:
                        S[-1].append((l,self.spmat[i][j][1]+b.spmat[i][k][1]))
                    j+=1
                    k+=1
                elif j < len(self.spmat[i]) and self.spmat[i][j][0] == l:
                    S[i].append(self.spmat[i][j])
                    j +=1
                elif k < len(b.spmat[i]) and b.spmat[i][k][0] == l:
                    S[i].append(b.spmat[i][k])
                    k+=1
        return SparseMatrix(S,self.nrows,self.ncols)    
    #similar to addition
    def __sub__(self,b):
        if self.nrows != b.nrows or self.ncols != b.ncols:
            raise Exception('Matrix Dimensions do not match')
        S = []
        for i in range(self.nrows):
            S.append([])
            j = 0
            k = 0
            for l in range(self.ncols):
                if j < len(self.spmat[i]) and k < len(b.spmat[i]) and self.spmat[i][j][0] == l and b.spmat[i][k][0] == l:  
                    if (self.spmat[i][j][1]-b.spmat[i][k][1]) != 0:
                        S[-1].append((l,self.spmat[i][j][1]-b.spmat[i][k][1]))
                    j+=1
                    k+=1
                elif j < len(self.spmat[i]) and self.spmat[i][j][0] == l:
                    S[i].append(self.spmat[i][j])
                    j +=1
                elif k < len(b.spmat[i]) and b.spmat[i][k][0] == l:
                    S[i].append((l,0-b.spmat[i][k][1]))
                    k+=1
        return SparseMatrix(S,self.nrows,self.ncols)
    def __mul__(self,b):
        #for scalar multiplication
        if not(isinstance(b,SparseMatrix)):
            S = []
            for i in self.spmat:
                S.append([])
                for j in i:
                    S[-1].append((j[0],b*j[1]))
            return SparseMatrix(S,self.nrows,self.ncols)
        elif self.ncols != b.nrows:
            raise Exception('Matrix Dimensions do not match')
        #for matrix multiplcation
        else:
            S = []
            for i in self.spmat:
                S.append([])
                for j in range(b.ncols):
                    c = 0 
                    for k in i:
                        #finds the non-zero element and its index, then multiplies it by the corresponding element in the second list
                        for x in b.spmat[k[0]]:
                            if j == x[0] :
                                c += k[1]*x[1]
                    if c != 0:
                        S[-1].append((j,c))
            return SparseMatrix(S,self.nrows,b.ncols)    
    def toDense(self):
        #constructs a list of lists of all elements equal to zero
        S = [[0 for x in range(self.ncols)] for i in range(self.nrows)]
        for i,ii in enumerate(self.spmat):
            #change the corresponding non-zero elements to their value
            for j in ii:
                S[i][j[0]] = j[1]
        return Matrix(S)
#%% Question 3
#helper function to check whether we can go to the location (x,y) in Matrix or not.
def check(Matrix,x,y):
    if x < len(Matrix):
        if y < len(Matrix[x]):
            z = Matrix[x][y]
            if z != "X" and z != "Y":
                return True
    return False
#main function
def traverseMaze(MazeFile):
    slmtrx = []
    #recreating the matrix given in the MazeFile and also finding the starting and the ending points
    maze = []
    file = open(MazeFile)
    for line in file:
        maze.append(line.split())
    file.close()
    for i,ii in enumerate(maze):
        slmtrx.append([])
        for j,jj in enumerate(ii):
            if jj == "S":
                start = (i,j)
            elif jj == "E":
                end = (i,j)
            slmtrx[i].append(jj)
    #current location
    lcn = start
    #stack of steps, denoting the path
    pth = []
    #Main While Loop
    #while we do not reach the end point/ Exit
    while lcn != end:
    #At every point, we are removing one location that we cannot traverse in the maze.
        #checks whether we can go towards right, down, left and up in that order and then takes the first possible step.
        #marks the current cell as Y so that we can check later that the current cell has been visited.
        if check(slmtrx,lcn[0],lcn[1]+1):
            slmtrx[lcn[0]][lcn[1]] = "Y"
            pth.append("R")
            lcn = (lcn[0],lcn[1]+1)
        elif check(slmtrx,lcn[0]+1,lcn[1]):
            slmtrx[lcn[0]][lcn[1]] = "Y"
            pth.append("D")
            lcn = (lcn[0]+1,lcn[1])
        elif check(slmtrx,lcn[0],lcn[1]-1):
            slmtrx[lcn[0]][lcn[1]] = "Y"
            pth.append("L")
            lcn = (lcn[0],lcn[1]-1)
        elif check(slmtrx,lcn[0]-1,lcn[1]):
            slmtrx[lcn[0]][lcn[1]] = "Y"
            pth.append("U")
            lcn = (lcn[0]-1,lcn[1])
        #if we cannot move anywhere, we have reached a dead end.
        #In this case, we take a step back and move to the last location.
        #We do this by checking what was the last element in the path stack and then pop it out.
        else:
            #if there is an element in the path stack, we move backwards accordingly.
            if pth:
                z = pth.pop()
                slmtrx[lcn[0]][lcn[1]] = "X"
                if z == "D":
                    lcn = (lcn[0]-1,lcn[1])
                elif z == "R":
                    lcn = (lcn[0],lcn[1]-1)
                elif z == "U":
                    lcn = (lcn[0]+1,lcn[1])
                elif z == "L":
                    lcn = (lcn[0],lcn[1]+1)
            #if there is no element in the stack of paths,
            #we are at the starting point with no place to go to.
            #Hence we cannot move and thus there exists no path.
            else:
                return "No path"
        print(Matrix(slmtrx))
    #Since there are only finite locations in the maze, either we will find the exit or there will be no path out of the maze.
    return pth
traverseMaze("maze2.txt")
#%%