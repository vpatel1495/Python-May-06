#Assignement 3
#PROBLEM 1
    # Create a program to do the following tasks. Note: Without using inbuild functions like sort, min, sorted, reverse, split
        # A) Split a given sentence into a list of words.
        # B) Sort that list accordingly to the letters alphabetically.
        # C) Sort that list alphabetically.

sentence =input("Type any sentence, end sentence with a space: ")
listA=[]
lowsent=sentence.lower()
def sent_split (self, y=0):
    n=len(self)
    while y < n :
        x=self.index(' ', y, n)
        listA.append(self[y:x])
        y = x+1
    print(listA)


sent_split(lowsent)
#This will take the sentence and make a list of each word

listB = listA[:]
def assort_sent(self):
    n=len(self)
    x=0
    for i in range(0, n):
        m=len(self[i])
        for j in range (0, m):
            while x< (n-1):
                if ord(self[x][0])>ord(self[x+1][0]):
                    listB.append(listB[x])
                    del(listB[x])
                    x=x+1
                else:
                    x=x+1
            x=0
    print(listB)

assort_sent(listB)

#This prints a list of the words in alphabetical order



listC=listB[:]
list1=[]
def list_word(self):
    n=len(self)
    list2=[]
    for i in range(0, n):
        m=len(self[i])
        list2=[]
        for j in range(0, m):
            list2.append(self[i][j])
        list1.append(list2)
    print(list1)

list_word(listC)

list2=list1[:]
def assrt(self):
    def assort_word(self):
        n = len(self)
        for i in range(0, n):
            m = len(self[i])
            for j in range(0, m-1):
                if ord(self[i][j]) > ord(self[i][j + 1]):
                    list2[i].append(self[i][j])
                    del list2[i][j]
    n=len(self)
    for i in range(0, n):
        m =len(self[i])
        for j in range(0, m):
            assort_word(self)
    print(list2)

assrt(list1)

#This will sort the list of words alphabetically
