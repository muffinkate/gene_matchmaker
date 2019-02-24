class Region(object):
    def __init__(self, chromo, start, stop, s):
        self.chromo = chromo
        self.start = start
        self.stop = stop
        self.otherStuff = s
    def overlap(self, other):
        if self.start+1<other.start+1 and self.stop>other.start+1:
            return True
        if self.start+1<other.stop and self.stop>other.stop:
            return True
        if self.start+1>other.start+1 and self.stop<other.stop:
            return True
        return False
    def __eq__(self, other):
        return self.start==other.start and self.stop == other.stop
    def __lt__(self, other):
        return self.start < other.start
    def __hash__(self):
        return hash((self.chromo, self.start, self.stop))
    def __str__(self):
        return str(self.start)+" "+str(self.stop)
    

def getInt(f, reg) :
    firstRun = True
    fin = []
    with open(f) as file2:
        #gets line one out of file2
        temp = file2.readline().replace('\n','')
        temp = temp.split("\t")
        #makes an empty region(this doesn't make an empty region again)
        reg2 = Region(temp[0],int(temp[1]),int(temp[2]),temp[3:])
        #makes an empty list to put the works in
        #goes through all the regions that could possibly intersect
        while reg.stop>reg2.start+1 and temp[0]!="":
            #makes a region out of the line data
            if not firstRun:
                reg2 = Region(temp[0],int(temp[1]), int(temp[2]),temp[3:])
            #checks to see if they intersect and if they do, adds it to fin
            if reg.overlap(reg2):
                fin.append(reg2)
            #goes to the next line
            temp= file2.readline().replace('\n','')
            temp = temp.split("\t")
            firstRun = False
    if len(fin) >0:
        fin.append(reg)
    return fin
    


#This method adds the intersects to the bed file.
def intersect(reg, files):
    fin = []
    for bed in files:
        t = getInt(bed, reg)
        for r in t:
            fin.append(r)
    for r in fin:
        print(str(r), end = '')
    print()
    return fin
##    fin = getInt("ex2.txt", reg)
##    fin.extend(getInt("ex3.txt", reg))
##    if len(fin)>0:
##        fin.append(reg)
##    print(len(fin))
##    with open(bed, "a+") as --out:
##        for r in fin:
##            print("Writing out:" +r.chromo+"\t"+str(r.start)+"\t"+str(r.stop))
##            out.write(r.chromo+"\t"+str(r.start)+"\t"+str(r.stop)+'\n')


#files = input("What files do you need to compare?/n Please put full file names seperated by spaces")
#files = files.split(" ")
import sys
files = sys.argv[1:]
fin = set()
for i in range(len(files)-1):
    print("We are doing file {} now".format(i))
    with open(files[i]) as f:
        for line in f:
            temp = line.replace('\n','')
            temp = temp.split("\t")
            reg = Region(temp[0],int(temp[1]), int(temp[2]), temp[3:])
            if len(files)-i-1==1:
                t = getInt(files[i+1], reg)
                for j in t:
                    fin.add(j)
            else:
                t = intersect(reg, files[i+1:])
                for j in t:
                    fin.add(j)
                for r in fin:
                    print(str(r), end = '')
                print()
with open("out.bed", "a+") as out:
    for r in fin:
        print("Writing out:" +r.chromo+"\t"+str(r.start)+"\t"+str(r.stop))
        out.write(r.chromo+"\t"+str(r.start)+"\t"+str(r.stop)+'\t'+'\t'.join(r.otherStuff)+'\n')
        
            
            
#Orginal Code
##with open("ex1.txt") as file1:
##    for line in file1:
##        temp = line.replace('\n','')
##        temp = temp.split("\t")
##        print(temp)
##        reg = Region(temp[0],int(temp[1]), int(temp[2]))
##        intersect(reg,"out.bed")




