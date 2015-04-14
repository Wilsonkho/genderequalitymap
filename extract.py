#!/usr/bin/python
import re
def percentDiff(men, women):
    diff = men - women
    avg = (men+women)/2
    return abs(diff/avg) * 100
def equality(pd):
    if (pd < 5):
        return "<5%"
    elif (5 <= pd < 20):
        return "5-20%"
    elif (20 <= pd < 50):
        return "20-50%"
    elif (50 <= pd < 75):
        return "50-75%"
    elif (75 <= pd < 100):
        return "75-100%"
    elif (100 <= pd < 150):
        return "100-150%"
    else:
        return "<150%"
    
#extract countries from datamaps file
#fin = open("world.min.js","r")
#fout = open("data2", "w")
#lines = fin.readlines();
#i = 0;
#for x in lines:
    #i = i + 1
    #if (i%2 == 0):
        #fout.write(x)
#fin.close()
#fout.close()

#move 3 character code to the front
#fin = open("data2","r")
#fout = open("data3","w")
#lines = fin.readlines()
#lines = ''.join(lines)
#lines = re.split(r'[\n]\s*', lines)
#lines = ''.join(lines)
#lines = lines.split(',')
#print lines
#i = 0;
#while (i < len(lines)-1):
    #fout.write(lines[i+1])
    #fout.write(" ")
    #fout.write(lines[i])
    #fout.write("\n")
    #i = i + 2
#fin.close()
#fout.close()
    
    

#extract compile data from 
#fout = open("MapUnemploymentColorCode","w")
#fin1 = open ("unemployment.csv","r")
#lines = fin1.readlines()
#temp = lines[0]
#temp = re.split(r'[\r,]\s*', temp)
##print temp
#fin2 = open("data3","r")
#lines = fin2.readlines()
#alist = []
#for line in lines:
    #line = line.split(None, 1)
    #line[1] = line[1].strip()
    #alist.append(line[0])
    #alist.append(line[1])
##print alist

#i = 1
#while (i < len(alist)):
    #if (alist[i] in temp):
        ##fout.write(alist[i-1]+","+alist[i]+","+ temp[temp.index(alist[i]) + 1] +","+ temp[temp.index(alist[i]) + 2]+'\n')
        ##print alist[i] + " " + str(percentDiff(float(temp[temp.index(alist[i]) + 1]), float(temp[temp.index(alist[i]) + 2])))
        #fout.write( alist[i-1]+":{\"fillKey\":\""+ equality(percentDiff(float(temp[temp.index(alist[i]) + 1]), float(temp[temp.index(alist[i]) + 2]))) + "\"}," + "\n")
    ##else:
        ##fout.write(alist[i-1]+","+alist[i]+","+ "-1" +","+ "-1\n")
    #else:
        #print alist[i] + "\t" + alist[i-1] 
    #i = i + 2
        
##print lines 

#fin1.close()
#fin2.close()
#fout.close()

fout = open("MapLiteracyColorCode","w")
fin1 = open("countries","r")
fin2 = open("litracy.csv","r")

fout.close()
fin1.close()
fin2.close()


