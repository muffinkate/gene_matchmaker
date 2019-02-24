##  takes a BED file and splits it into chromosome files

def chromosomer(file, filename):
    with open(file) as testFile:
        for line in testFile:
            temp = line.split("\t")
            chrome = temp[0]
            if(chrome == 'chr1'):
                with open("chr1_%s.txt" % filename, "a+") as out:
                    out.write(line)
            elif(chrome == 'chr2'):
                with open("chr2_%s.txt" % filename, "a+") as out:
                    out.write(line)
            elif(chrome == 'chr3'):
                with open("chr3_%s.txt" % filename, "a+") as out:
                    out.write(line)
            elif(chrome == 'chr4'):
                with open("chr4_%s.txt" % filename, "a+") as out:
                    out.write(line)
            elif(chrome == 'chr5'):
                with open("chr5_%s.txt" % filename, "a+") as out:
                    out.write(line)
            elif(chrome == 'chr6'):
                with open("chr6_%s.txt" % filename, "a+") as out:
                    out.write(line)
            elif(chrome == 'chr7'):
                with open("chr7_%s.txt" % filename, "a+") as out:
                    out.write(line)
            elif(chrome == 'chr8'):
                with open("chr8_%s.txt" % filename, "a+") as out:
                    out.write(line)
            elif(chrome == 'chr9'):
                with open("chr9_%s.txt" % filename, "a+") as out:
                    out.write(line)
            elif(chrome == 'chr10'):
                with open("chr10_%s.txt" % filename, "a+") as out:
                    out.write(line)
            elif(chrome == 'chr11'):
                with open("chr11_%s.txt" % filename, "a+") as out:
                    out.write(line)
            elif(chrome == 'chr12'):
                with open("chr12_%s.txt" % filename, "a+") as out:
                    out.write(line)
            elif(chrome == 'chr13'):
                with open("chr13_%s.txt" % filename, "a+") as out:
                    out.write(line)
            elif(chrome == 'chr14'):
                with open("chr14_%s.txt" % filename, "a+") as out:
                    out.write(line)
            elif(chrome == 'chr15'):
               with open("chr15_%s.txt" % filename, "a+") as out:
                    out.write(line) 
            elif(chrome == 'chr16'):
                with open("chr16_%s.txt" % filename, "a+") as out:
                    out.write(line)
            elif(chrome == 'chr17'):
                with open("chr17_%s.txt" % filename, "a+") as out:
                    out.write(line)
            elif(chrome == 'chr18'):
                with open("chr18_%s.txt" % filename, "a+") as out:
                    out.write(line)
            elif(chrome == 'chr19'):
                with open("chr19_%s.txt" % filename, "a+") as out:
                    out.write(line)
            elif(chrome == 'chr20'):
                with open("chr20_%s.txt" % filename, "a+") as out:
                    out.write(line)
            elif(chrome == 'chr21'):
                with open("chr21_%s.txt" % filename, "a+") as out:
                    out.write(line)
            elif(chrome == 'chr22'):
                with open("chr22_%s.txt" % filename, "a+") as out:
                    out.write(line)
            elif(chrome == 'chrX'):
                with open("chrX_%s.txt" % filename, "a+") as out:
                    out.write(line)
            elif(chrome == 'chrY'):
                with open("chrY_%s.txt" % filename, "a+") as out:
                    out.write(line)
            elif(chrome == 'chrM'):
                with open("chrM_%s.txt" % filename, "a+") as out:
                    out.write(line)

chromosomer("out.BED","test1")
