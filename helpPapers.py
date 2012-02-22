import numpy
import inputdata
from math import sqrt

data = inputdata.raw_scores
listPaper = []
listKof = []
listPaper1 = []
listHuman = data.keys()


class Papers(object):
   def __init__(self, n, p1, p2):
      self._numpyList = n
      self._pythonList1 = p1
      self._pythonList2 = p2
   def __2norm__(self, i1, i2):
      ist1 = self._numpyList[i1]
      ist2 = self._numpyList[i2]
      suma = 0;
      tt = False;   
      for j in range(0,lenl2):
          if ist1[j]!=0 and ist2[j]!=0:
               tt = True
               suma = suma + (ist1[j] - ist2[j]) * (ist1[j] - ist2[j])  
      if (not tt):
          return False
      else: 
          return sqrt(suma)

   def __personCor__(self, i1, i2):
      ist1 = self._numpyList[i1]
      ist2 = self._numpyList[i2]
      l1 = []
      l2 = []
      tt = False;   
      for j in range(0,lenl2):
          if ist1[j]!=0 and ist2[j]!=0:
               tt = True
               l1.insert(len(l1), ist1[j])
               l2.insert(len(l2), ist2[j])   
      if (not tt):
          return False
      else: 
          return numpy.cov(numpy.array(l1), numpy.array(l2))[1,0]
     
   def __tanDist__(self, i1, i2):
      ist1 = numpy.array(self._numpyList[i1])
      ist2 = numpy.array(self._numpyList[i2])
      l1 = ist1>0
      l2 = ist2>0
      b = 0.0
      i = 0.0
      for j in range(0,lenl2):
          if l1[j]==True and l2[j]==True:
             b = b + 1
          if l1[j]==True or l2[j]==True: 
             i = i + 1
      return b/i
            
      
                   

def listKey(diks):
   lst = diks.keys()
   for k in lst: 
      lst2 = diks[k].keys()
      for pp in lst2:
          listPaper.insert(len(listPaper),pp)
      for p in lst2:
          listKof.append(diks[k][p])
   
   pom = set(listPaper)
   lisss = list(pom)
   for pp in lisss:
         listPaper1.insert(len(listPaper1),pp)
  

def makeMatrix(mat):
   for i in range(0,lenl1):
      k = listHuman[i]
      lst2 = data[k].keys()
      for j in range(0,lenl2):
          p = listPaper1[j]
          if p in lst2:
             mat[i,j] = data[k][p]

            
listKey(data)
lenl1 = len(data.keys())
lenl2 = len(listPaper1)

def emptyMat():
   mat = numpy.zeros((lenl1,lenl2))
   return mat

mat = emptyMat()
makeMatrix(mat)

x = Papers(mat, listHuman, listPaper1)
print x._numpyList
print x._pythonList1
print x._pythonList2




def test1():
   assert x.__2norm__(0,1) == 2.5495097568

def test2():
   assert x.__personCor__(0.1) == 0.3125

def test3():
   assert x.__tanDist__(1,2) == 0.5



print x.__2norm__(0,1)
print x.__personCor__(0,1)
print x.__tanDist__(1,2)



  













