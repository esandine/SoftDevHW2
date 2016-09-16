#Angela Yu & Ely Sandine

def importation(filename):
    instream = open(filename, 'r') 
    content = instream.readlines() 
    instream.close()
    return content

data=importation("occupations.csv")
dict = {}

def split(L):
    for row in L:
        row=row.split(',')
        dict[row[0]]=row[1]
    

split(data)
print(dict.keys())
