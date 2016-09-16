#Angela Yu & Ely Sandine
#Work 1
#Dyrland-Weaver pd 6

def importation(filename):
    instream = open(filename, 'r') 
    content = instream.readlines() 
    instream.close()
    return content

data=importation("occupations.csv")
dict = {}

def split(L):
    del L[0]
    del L[len(L)-1]
    for row in L:
        row=row.strip('\n').rsplit(',',1)
        dict[row[0]]=(float)(row[1])

split(data)
print(dict.keys())
print(dict.values())
