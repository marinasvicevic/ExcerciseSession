import os
import glob
import fileinput
import sys

def readfile():
     return glob.glob("cleandata/*.txt")



def ifN(file):
       for line in fileinput.input(file):
            if line =='Sex: N\n':
                     fileinput.close()
                     return True
            pass
       fileinput.close()
       return False

def replaceN(file):
       for line in fileinput.input(file, inplace=1):
            if line =='Sex: N\n':
                     line = 'Sex: M\n'        
            pass
            sys.stdout.write(line)

       fileinput.close() 

def main():
    list=readfile()
    #print list
    for file in list:  
                       print str(file) + ':' + str(ifN(file))
                       replaceN(file)



main()

