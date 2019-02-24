##  creates function for the chromosome/region visual

from graphics import *
from chromosomer import *

##  finds the x-coordinate of the box that represents the region
def findX(start, l):
    ##  length = length of total chromosome
    
    length = l
    perc = (int(start)*1000)/length
    return 50+perc


##  returns the length of the total chromosome, as given
##  by the line of the file
def findChrLength(chrome):
    if(chrome == 'chr1'):
        return 248956422
    elif(chrome == 'chr2'):
        return 242193529
    elif(chrome == 'chr3'):
        return 198295559
    elif(chrome == 'chr4'):
        return 190214555
    elif(chrome == 'chr5'):
        return 181538259
    elif(chrome == 'chr6'):
        return 170805979
    elif(chrome == 'chr7'):
        return 159345973
    elif(chrome == 'chr8'):
        return 145138636
    elif(chrome == 'chr9'):
        return 138394717
    elif(chrome == 'chr10'):
        return 133797422
    elif(chrome == 'chr11'):
        return 135086622
    elif(chrome == 'chr12'):
        return 133275309
    elif(chrome == 'chr13'):
        return 114364328
    elif(chrome == 'chr14'):
        return 107043718
    elif(chrome == 'chr15'):
        return 101991189
    elif(chrome == 'chr16'):
        return 90338345
    elif(chrome == 'chr17'):
        return 83257441
    elif(chrome == 'chr18'):
        return 80373285
    elif(chrome == 'chr19'):
        return 58617616
    elif(chrome == 'chr20'):
        return 64444167
    elif(chrome == 'chr21'):
        return 46709983
    elif(chrome == 'chr22'):
        return 50818468
    elif(chrome == 'chrX'):
        return 156040895
    elif(chrome == 'chrY'):
        return 57227415
    elif(chrome == 'chrM'):
        return 16569

##  will eventually draw all the rectangles for a chromosome
def drawChromosome(w,stuff,lineSpot):
    
        temp = stuff.split("\t")
        length = findChrLength(temp[0])
        rTst = Rectangle(Point(findX(temp[1],length),lineSpot-10),Point(findX(temp[2],length),lineSpot+10))
        rTst.setFill("pink")
        rTst.draw(w)

def main():
    win = GraphWin("GeneMatchmaker: HTT Gene", 1100,700)
    win.setBackground("white")

    title = Text(Point(150,30),"Areas of Interest for the HTT Gene")
    title.setStyle("bold")
    title.draw(win)

##  chromosome 1
    chr1t = Text(Point(150,55),"Chromosome 1")
    chr1t.draw(win)

    l = Line(Point(50,80),Point(1050,80))
    l.draw(win)
    try:
        with open("chr1_test1.txt") as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win,line,80)
        testFile.close()
    except:
        error = Text(Point(300,55),"No Intersecting Regions")
        error.draw(win)

## chromosome 2
    chr2t = Text(Point(150,105),"Chromosome 2")
    chr2t.draw(win)

    l2 = Line(Point(50,130),Point(1050,130))
    l2.draw(win)

    try:
        with open("chr2_test1.txt") as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win,line,130)
        testFile.close()
    except:
        error = Text(Point(300,105),"No Intersecting Regions")
        error.draw(win)

##  chromosome 3
    chr3t = Text(Point(150,155),"Chromosome 3")
    chr3t.draw(win)

    l3 = Line(Point(50,180),Point(1050,180))
    l3.draw(win)

    try:
        with open("chr3_test1.txt") as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win,line,180)
        testFile.close()
    except:
        error = Text(Point(300,155),"No Intersecting Regions")
        error.draw(win)

##  chromosome 4
    chr4t = Text(Point(150,205),"Chromosome 4")
    chr4t.draw(win)

    l4 = Line(Point(50,230),Point(1050,230))
    l4.draw(win)

    try:
        with open("chr4_test1.txt") as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win,line,230)
        testFile.close()
    except:
        error = Text(Point(300,205),"No Intersecting Regions")
        error.draw(win)

## chromosome 5
    chr5t = Text(Point(150,255),"Chromosome 5")
    chr5t.draw(win)

    l5 = Line(Point(50,280),Point(1050,280))
    l5.draw(win)

    try:
        with open("chr5_test1.txt") as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win,line,280)
        testFile.close()
    except:
        error = Text(Point(300,255),"No Intersecting Regions")
        error.draw(win)

## chromosome 6
    chr6t = Text(Point(150,305),"Chromosome 6")
    chr6t.draw(win)

    l6 = Line(Point(50,330),Point(1050,330))
    l6.draw(win)

    try:
        with open("chr6_test1.txt") as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win,line,330)
        testFile.close()
    except:
        error = Text(Point(300,305),"No Intersecting Regions")
        error.draw(win)

##  chromosome 7
    chr7t = Text(Point(150,355),"Chromosome 7")
    chr7t.draw(win)

    l7 = Line(Point(50,380),Point(1050,380))
    l7.draw(win)

    try:
        with open("chr7_test1.txt") as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win,line,380)
        testFile.close()
    except:
        error = Text(Point(300,355),"No Intersecting Regions")
        error.draw(win)

## chromosome 8
    chr8t = Text(Point(150,405),"Chromosome 8")
    chr8t.draw(win)

    l8 = Line(Point(50,430),Point(1050,430))
    l8.draw(win)

    try:
        with open("chr8_test1.txt") as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win,line,430)
        testFile.close()
    except:
        error = Text(Point(300,405),"No Intersecting Regions")
        error.draw(win)

##  chromosome 9
    chr9t = Text(Point(150,455),"Chromosome 9")
    chr9t.draw(win)

    l9 = Line(Point(50,480),Point(1050,480))
    l9.draw(win)

    try:
        with open("chr9_test1.txt") as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win,line,480)
        testFile.close()
    except:
        error = Text(Point(300,455),"No Intersecting Regions")
        error.draw(win)

##  chromosome 10
    chr10t = Text(Point(150,505),"Chromosome 10")
    chr10t.draw(win)

    l10 = Line(Point(50,530),Point(1050,530))
    l10.draw(win)

    try:
        with open("chr10_test1.txt") as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win,line,530)
        testFile.close()
    except:
        error = Text(Point(300,505),"No Intersecting Regions")
        error.draw(win)

##  chromosome 11
    chr11t = Text(Point(150,555),"Chromosome 11")
    chr11t.draw(win)

    l11 = Line(Point(50,580),Point(1050,580))
    l11.draw(win)

    try:
        with open("chr11_test1.txt") as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win,line,580)
        testFile.close()
    except:
        error = Text(Point(300,555),"No Intersecting Regions")
        error.draw(win)

## chromosome 12
    chr12t = Text(Point(150,605),"Chromosome 12")
    chr12t.draw(win)

    l12 = Line(Point(50,630),Point(1050,630))
    l12.draw(win)

    try:
        with open("chr12_test1.txt") as testFile:
            for line in testFile:
               if line != "\n":
                   drawChromosome(win,line,630)
        testFile.close()
    except:
        error = Text(Point(300,605),"No Intersecting Regions")
        error.draw(win)

    win2 = GraphWin("GeneMatchmaker: HTT Gene pg. 2", 1100,700)
    win2.setBackground("white")

##  chromosome 13
    chr13t = Text(Point(150,55),"Chromosome 13")
    chr13t.draw(win2)

    l13 = Line(Point(50,80),Point(1050,80))
    l13.draw(win2)

    try:
        with open("chr13_test1.txt") as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win2,line,80)
        testFile.close()
    except:
        error = Text(Point(300,55),"No Intersecting Regions")
        error.draw(win2)

## chromosome 14
    chr14t = Text(Point(150,105),"Chromosome 14")
    chr14t.draw(win2)

    l14 = Line(Point(50,130),Point(1050,130))
    l14.draw(win2)

    try:
        with open("chr14_test1.txt") as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win2,line,130)
        testFile.close()
    except:
        error = Text(Point(300,105),"No Intersecting Regions")
        error.draw(win2)


## chromosome 15
    chr15t = Text(Point(150,155),"Chromosome 15")
    chr15t.draw(win2)

    l15 = Line(Point(50,180),Point(1050,180))
    l15.draw(win2)

    try:
        with open("chr15_test1.txt") as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win2,line,180)
        testFile.close()
    except:
        error = Text(Point(300,155),"No Intersecting Regions")
        error.draw(win2)

##  chromosome 16
    chr16t = Text(Point(150,205),"Chromosome 16")
    chr16t.draw(win2)

    l16 = Line(Point(50,230),Point(1050,230))
    l16.draw(win2)

    try:
        with open("chr16_test1.txt") as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win2,line,230)
        testFile.close()
    except:
        error = Text(Point(300,205),"No Intersecting Regions")
        error.draw(win2)

##  chromosome 17
    chr17t = Text(Point(150,255),"Chromosome 17")
    chr17t.draw(win2)

    l17 = Line(Point(50,280),Point(1050,280))
    l17.draw(win2)

    try:
        with open("chr17_test1.txt") as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win2,line,280)
        testFile.close()
    except:
        error = Text(Point(300,255),"No Intersecting Regions")
        error.draw(win2)

##  chromosome 18
    chr18t = Text(Point(150,305),"Chromosome 18")
    chr18t.draw(win2)

    l18 = Line(Point(50,330),Point(1050,330))
    l18.draw(win2)

    try:
        with open("chr18_test1.txt") as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win2,line,330)
        testFile.close()
    except:
        error = Text(Point(300,305),"No Intersecting Regions")
        error.draw(win2)

##  chromosome 19
    chr19t = Text(Point(150,355),"Chromosome 19")
    chr19t.draw(win2)

    l19 = Line(Point(50,380),Point(1050,380))
    l19.draw(win2)

    try:
        with open("chr19_test1.txt") as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win2,line,380)
        testFile.close()
    except:
        error = Text(Point(300,355),"No Intersecting Regions")
        error.draw(win2)

##  chromosome 20
    chr20t = Text(Point(150,405),"Chromosome 20")
    chr20t.draw(win2)

    l20 = Line(Point(50,430),Point(1050,430))
    l20.draw(win2)

    try:
        with open("chr20_test1.txt") as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win2,line,430)
        testFile.close()
    except:
        error = Text(Point(300,405),"No Intersecting Regions")
        error.draw(win2)

##  chromosme 21
    chr21t = Text(Point(150,455),"Chromosome 21")
    chr21t.draw(win2)

    l21 = Line(Point(50,480),Point(1050,480))
    l21.draw(win2)

    try:
        with open("chr21_test1.txt") as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win2,line,480)
        testFile.close()
    except:
        error = Text(Point(300,455),"No Intersecting Regions")
        error.draw(win2)

##  chromosome 22
    chr22t = Text(Point(150,505),"Chromosome 22")
    chr22t.draw(win2)

    l22 = Line(Point(50,530),Point(1050,530))
    l22.draw(win2)

    try:
        with open("chr22_test1.txt") as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win2,line,530)
        testFile.close()
    except:
        error = Text(Point(300,505),"No Intersecting Regions")
        error.draw(win2)
##  chromosome x
    chrxt = Text(Point(150,555),"Chromosome X")
    chrxt.draw(win2)

    lx = Line(Point(50,580),Point(1050,580))
    lx.draw(win2)
    try:
        with open("chrX_test1.txt") as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win2,line,580)
        testFile.close()
    except:
        error = Text(Point(300,555),"No Intersecting Regions")
        error.draw(win2)

##  chromosome y
    chryt = Text(Point(150,605),"Chromosome Y")
    chryt.draw(win2)

    ly = Line(Point(50,630),Point(1050,630))
    ly.draw(win2)
    try: 
        with open("chrY_test1.txt") as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win2,line,630)
        testFile.close()
    except:
        error = Text(Point(300,605),"No Intersecting Regions")
        error.draw(win2)

##  chromosome m
    chrmt = Text(Point(150,655),"Chromosome M")
    chrmt.draw(win2)

    lz = Line(Point(50,680),Point(1050,680))
    lz.draw(win2)
    try: 
        with open("chrM_test1.txt") as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win2,line,680)
        testFile.close()
    except:
        error = Text(Point(300,655),"No Intersecting Regions")
        error.draw(win2)

    win.getMouse()
    win.close()

    


main()
