##  creates function for the chromosome/region visual

from graphics import *

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
    chrom_choice = input("Please Enter the Chromosome You Want to View Data For: ")
    while(chrom_choice.lower() != 'stop'):
        win = GraphWin("GeneMatchmaker: HTT Gene - Chromosome %s" % chrom_choice, 1100,700)
        win.setBackground("white")

        title = Text(Point(225,30),"Areas of Interest for the HTT Gene: Available Data")
        title.setStyle("bold")
        title.draw(win)

        exps1 = Text(Point(150,55),"Experiment 1")
        exps1.draw(win)
        l = Line(Point(50,80),Point(1050,80))
        l.draw(win)

        with open("chr%s_bed1.txt" % chrom_choice) as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win,line,80)
        testFile.close()

        exps1 = Text(Point(150,105),"Experiment 2")
        exps1.draw(win)
        l = Line(Point(50,130),Point(1050,130))
        l.draw(win)

        with open("chr%s_bed2.txt" % chrom_choice) as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win,line,130)
        testFile.close()

        exps1 = Text(Point(150,155),"Experiment 3")
        exps1.draw(win)
        l = Line(Point(50,180),Point(1050,180))
        l.draw(win)

        with open("chr%s_bed3.txt" % chrom_choice) as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win,line,180)
        testFile.close()
        
        overlaps = Text(Point(150,205),"Intersections of Experiments")
        overlaps.draw(win)
        l = Line(Point(50,230),Point(1050,230))
        l.draw(win)

##        heyo = Text(Point(150,305),"Regions of Interest")
##        heyo.setStyle('bold')
##        heyo.draw(win)
##       anchor = 320
##        xSpot = 150
##        ySpot = 320
##        watchOut = 650
        
        with open("out_onlychr%s.bed" % chrom_choice) as testFile:
            for line in testFile:
                if line != "\n":
                    drawChromosome(win,line,230)
##                    stuff = line.split("\t")
##                    if(int(ySpot)<int(watchOut)):
##                         text = Text(Point(xSpot,ySpot),stuff[1]+"\t"+stuff[2])
##                         text.draw(win)
##                         ySpot = ySpot+15
##                    else :
##                        ySpot = anchor
##                        xSpot = xSpot+100
##                        text = Text(Point(xSpot,ySpot),stuff[1]+"\t"+stuff[2])
##                        text.draw(win)
##                        ySpot = ySpot+15
##                    
##        
            chrom_choice = input("Please Enter the Chromosome You Want to View Data For: ")
 ## all intersections at once???   
    win.getMouse()
    win.close()

    


main()
