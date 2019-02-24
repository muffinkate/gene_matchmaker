##  creates visuals for each chromosome

from graphics import *

##  finds the x-coordinate of the box that represents the region
def findX(start, l):
##  length = length of total chromosome
    
    length = l
    perc = (int(start)*1000)/length
    return 50+perc

def main():
    win = GraphWin("GeneMatchmaker: HTT Gene", 1100,700)
    win.setBackground("white")
    l = Line(Point(50,80),Point(1050,80))
    l.draw(win)

    title = Text(Point(150,30),"Areas of Interest for the HTT Gene")
    title.setStyle("bold")
    title.draw(win)

##  chromosome 1

    chr1t = Text(Point(150,55),"Chromosome 1")
    chr1t.draw(win)

    with open("chr1TEST.txt") as testFile:
        for line in testFile:
            temp = line.split("\t")
            rTst = Rectangle(Point(findX(temp[1],248956422),70),Point(findX(temp[2],248956422),90))
            rTst.setFill("pink")
            rTst.draw(win)

    testFile.close()

## chromosome 2

    chr2t = Text(Point(150,105),"Chromosome 2")
    chr2t.draw(win)

    l2 = Line(Point(50,130),Point(1050,130))
    l2.draw(win)

    with open("chr2TEST.txt") as testFile:
        for line in testFile:
            temp = line.split("\t")
            rTst = Rectangle(Point(findX(temp[1],242193529),120),Point(findX(temp[2],242193529),140))
            rTst.setFill("pink")
            rTst.draw(win)
    testFile.close()

##  chromosome 3

    chr3t = Text(Point(150,155),"Chromosome 3")
    chr3t.draw(win)

    l3 = Line(Point(50,180),Point(1050,180))
    l3.draw(win)

    with open("chr3TEST.txt") as testFile:
        for line in testFile:
            temp = line.split("\t")
            rTst = Rectangle(Point(findX(temp[1],198295559),170),Point(findX(temp[2],198295559),190))
            rTst.setFill("pink")
            rTst.draw(win)
    testFile.close()
    
## chromosome 4
    chr4t = Text(Point(150,205),"Chromosome 4")
    chr4t.draw(win)

    l4 = Line(Point(50,230),Point(1050,230))
    l4.draw(win)

    with open("chr4TEST.txt") as testFile:
        for line in testFile:
            temp = line.split("\t")
            rTst = Rectangle(Point(findX(temp[1],190214555),220),Point(findX(temp[2],190214555),240))
            rTst.setFill("pink")
            rTst.draw(win)
    testFile.close()

##  chromosome 5
    chr5t = Text(Point(150,255),"Chromosome 5")
    chr5t.draw(win)

    l5 = Line(Point(50,280),Point(1050,280))
    l5.draw(win)

    with open("chr5TEST.txt") as testFile:
        for line in testFile:
            temp = line.split("\t")
            rTst = Rectangle(Point(findX(temp[1],181538259),270),Point(findX(temp[2],181538259),290))
            rTst.setFill("pink")
            rTst.draw(win)
    testFile.close()

## chromosome 6
    chr6t = Text(Point(150,305),"Chromosome 6")
    chr6t.draw(win)

    l6 = Line(Point(50,330),Point(1050,330))
    l6.draw(win)

    with open("chr6TEST.txt") as testFile:
        for line in testFile:
            temp = line.split("\t")
            rTst = Rectangle(Point(findX(temp[1],170805979),320),Point(findX(temp[2],170805979),340))
            rTst.setFill("pink")
            rTst.draw(win)
    testFile.close()

##  chromosome 7
    chr7t = Text(Point(150,355),"Chromosome 7")
    chr7t.draw(win)

    l7 = Line(Point(50,380),Point(1050,380))
    l7.draw(win)

    with open("chr7TEST.txt") as testFile:
        for line in testFile:
            temp = line.split("\t")
            rTst = Rectangle(Point(findX(temp[1],159345973),370),Point(findX(temp[2],159345973),390))
            rTst.setFill("pink")
            rTst.draw(win)
    testFile.close()

## chromosome 8
    chr8t = Text(Point(150,405),"Chromosome 8")
    chr8t.draw(win)

    l8 = Line(Point(50,430),Point(1050,430))
    l8.draw(win)

    with open("chr8TEST.txt") as testFile:
        for line in testFile:
            temp = line.split("\t")
            rTst = Rectangle(Point(findX(temp[1],145138636),420),Point(findX(temp[2],145138636),440))
            rTst.setFill("pink")
            rTst.draw(win)
    testFile.close()

##  chromosome 9
    chr9t = Text(Point(150,455),"Chromosome 9")
    chr9t.draw(win)

    l9 = Line(Point(50,480),Point(1050,480))
    l9.draw(win)

    with open("chr9TEST.txt") as testFile:
        for line in testFile:
            temp = line.split("\t")
            rTst = Rectangle(Point(findX(temp[1],138394717),470),Point(findX(temp[2],138394717),490))
            rTst.setFill("pink")
            rTst.draw(win)
    testFile.close()

##  chromosome 10
    chr10t = Text(Point(150,505),"Chromosome 10")
    chr10t.draw(win)

    l10 = Line(Point(50,530),Point(1050,530))
    l10.draw(win)

    with open("chr10TEST.txt") as testFile:
        for line in testFile:
            temp = line.split("\t")
            rTst = Rectangle(Point(findX(temp[1],133797422),520),Point(findX(temp[2],133797422),540))
            rTst.setFill("pink")
            rTst.draw(win)
    testFile.close()

##  chromosome 11
    chr11t = Text(Point(150,555),"Chromosome 11")
    chr11t.draw(win)

    l11 = Line(Point(50,580),Point(1050,580))
    l11.draw(win)

    with open("chr11TEST.txt") as testFile:
        for line in testFile:
            temp = line.split("\t")
            rTst = Rectangle(Point(findX(temp[1],135086622),570),Point(findX(temp[2],135086622),590))
            rTst.setFill("pink")
            rTst.draw(win)
    testFile.close()

## chromosome 12
    chr12t = Text(Point(150,605),"Chromosome 12")
    chr12t.draw(win)

    l12 = Line(Point(50,630),Point(1050,630))
    l12.draw(win)

    with open("chr12TEST.txt") as testFile:
        for line in testFile:
            temp = line.split("\t")
            rTst = Rectangle(Point(findX(temp[1],133275309),620),Point(findX(temp[2],133275309),640))
            rTst.setFill("pink")
            rTst.draw(win)
    testFile.close()

    win2 = GraphWin("GeneMatchmaker: HTT Gene pg. 2", 1100,700)
    win2.setBackground("white")

##  chromosome 13
    chr13t = Text(Point(150,55),"Chromosome 13")
    chr13t.draw(win2)

    l13 = Line(Point(50,80),Point(1050,80))
    l13.draw(win2)

    with open("chr13TEST.txt") as testFile:
        for line in testFile:
            temp = line.split("\t")
            rTst = Rectangle(Point(findX(temp[1],114364328),70),Point(findX(temp[2],114364328),90))
            rTst.setFill("pink")
            rTst.draw(win2)
    testFile.close()

## chromosome 14
    chr14t = Text(Point(150,105),"Chromosome 14")
    chr14t.draw(win2)

    l14 = Line(Point(50,130),Point(1050,130))
    l14.draw(win2)

    with open("chr14TEST.txt") as testFile:
        for line in testFile:
            temp = line.split("\t")
            rTst = Rectangle(Point(findX(temp[1],107043718),120),Point(findX(temp[2],107043718),140))
            rTst.setFill("pink")
            rTst.draw(win2)
    testFile.close()

## chromosome 15
    chr15t = Text(Point(150,155),"Chromosome 15")
    chr15t.draw(win2)

    l15 = Line(Point(50,180),Point(1050,180))
    l15.draw(win2)

    with open("chr15TEST.txt") as testFile:
        for line in testFile:
            temp = line.split("\t")
            rTst = Rectangle(Point(findX(temp[1],101991189),170),Point(findX(temp[2],101991189),190))
            rTst.setFill("pink")
            rTst.draw(win2)
    testFile.close()

##  chromosome 16
    chr16t = Text(Point(150,205),"Chromosome 16")
    chr16t.draw(win2)

    l16 = Line(Point(50,230),Point(1050,230))
    l16.draw(win2)

    with open("chr16TEST.txt") as testFile:
        for line in testFile:
            temp = line.split("\t")
            rTst = Rectangle(Point(findX(temp[1],90338345),220),Point(findX(temp[2],90338345),240))
            rTst.setFill("pink")
            rTst.draw(win2)
    testFile.close()

##  chromosome 17
    chr17t = Text(Point(150,255),"Chromosome 17")
    chr17t.draw(win2)

    l17 = Line(Point(50,280),Point(1050,280))
    l17.draw(win2)

    with open("chr17TEST.txt") as testFile:
        for line in testFile:
            temp = line.split("\t")
            rTst = Rectangle(Point(findX(temp[1],83257441),270),Point(findX(temp[2],83257441),290))
            rTst.setFill("pink")
            rTst.draw(win2)
    testFile.close()

##  chromosome 18
    chr18t = Text(Point(150,305),"Chromosome 18")
    chr18t.draw(win2)

    l18 = Line(Point(50,330),Point(1050,330))
    l18.draw(win2)

    with open("chr18TEST.txt") as testFile:
        for line in testFile:
            temp = line.split("\t")
            rTst = Rectangle(Point(findX(temp[1],80373285),320),Point(findX(temp[2],80373285),340))
            rTst.setFill("pink")
            rTst.draw(win2)
    testFile.close()

##  chromosome 19
    chr19t = Text(Point(150,355),"Chromosome 19")
    chr19t.draw(win2)

    l19 = Line(Point(50,380),Point(1050,380))
    l19.draw(win2)

    with open("chr19TEST.txt") as testFile:
        for line in testFile:
            temp = line.split("\t")
            rTst = Rectangle(Point(findX(temp[1],58617616),370),Point(findX(temp[2],58617616),390))
            rTst.setFill("pink")
            rTst.draw(win2)
    testFile.close()

##  chromosome 20
    chr20t = Text(Point(150,405),"Chromosome 20")
    chr20t.draw(win2)

    l20 = Line(Point(50,430),Point(1050,430))
    l20.draw(win2)

    with open("chr20TEST.txt") as testFile:
        for line in testFile:
            temp = line.split("\t")
            rTst = Rectangle(Point(findX(temp[1],64444167),420),Point(findX(temp[2],64444167),440))
            rTst.setFill("pink")
            rTst.draw(win2)
    testFile.close()

##  chromosme 21
    chr21t = Text(Point(150,455),"Chromosome 21")
    chr21t.draw(win2)

    l21 = Line(Point(50,480),Point(1050,480))
    l21.draw(win2)

    with open("chr21TEST.txt") as testFile:
        for line in testFile:
            temp = line.split("\t")
            rTst = Rectangle(Point(findX(temp[1],46709983),470),Point(findX(temp[2],46709983),490))
            rTst.setFill("pink")
            rTst.draw(win2)
    testFile.close()

##  chromosome 22
    chr22t = Text(Point(150,505),"Chromosome 22")
    chr22t.draw(win2)

    l22 = Line(Point(50,530),Point(1050,530))
    l22.draw(win2)

    with open("chr22TEST.txt") as testFile:
        for line in testFile:
            temp = line.split("\t")
            rTst = Rectangle(Point(findX(temp[1],50818468),520),Point(findX(temp[2],50818468),540))
            rTst.setFill("pink")
            rTst.draw(win2)
    testFile.close()

##  chromosome x
    chrxt = Text(Point(150,555),"Chromosome X")
    chrxt.draw(win2)

    lx = Line(Point(50,580),Point(1050,580))
    lx.draw(win2)

    with open("chrxTEST.txt") as testFile:
        for line in testFile:
            temp = line.split("\t")
            rTst = Rectangle(Point(findX(temp[1],156040895),570),Point(findX(temp[2],156040895),590))
            rTst.setFill("pink")
            rTst.draw(win2)
    testFile.close()

##  chromosome y
    chryt = Text(Point(150,605),"Chromosome Y")
    chryt.draw(win2)

    ly = Line(Point(50,630),Point(1050,630))
    ly.draw(win2)

    with open("chryTEST.txt") as testFile:
        for line in testFile:
            temp = line.split("\t")
            rTst = Rectangle(Point(findX(temp[1],57227415),620),Point(findX(temp[2],57227415),640))
            rTst.setFill("pink")
            rTst.draw(win2)
    testFile.close()

    win.getMouse()
    win.close()
    win2.close()

    


main()
