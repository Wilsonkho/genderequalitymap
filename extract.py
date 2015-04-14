#!/usr/bin/python
import re
def percentDiff(men, women):
    diff = men - women
    avg = (men+women)/2
    pd = (diff/avg)*100
    
    print(pd)
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
        return ">150%"
    
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

#Compile Literacy 
fout = open("MapLiteracyColorCode","w")
fout2 = open("LiteracyData","w")
fin1 = open("countries","r")
fin2 = open("literacy.csv","r")

fout2.write("CountryCode,CountryName,Men,Women\n")

#convert contries to array 
lines= fin1.readlines()
for x in range (0, len(lines)):
    lines[x] = lines[x].rstrip()
lines = ",".join(lines);
countries = lines.split(',')

#convert csv to array
lines= fin2.readlines()
lines= "\r\n".join(lines)
lines = lines.split('\r\n')
stat = []
for x in range (0, len(lines)):
    if (x%2 == 0):
        stat.append(lines[x])
stat = ",".join(stat)
stat = stat.split(",")
#print (stat)

#compile color code 
for x in range (0, len(countries)):
    if (x%2 != 0):
        if(countries[x] in stat):
            match = stat.index(countries[x])
            fout.write(countries[x-1]+":{\"fillKey\":\"" + percentDiff(float(stat[match+1]),float(stat[match+2])) + "\"},\n")
            fout2.write(countries[x-1]+","+countries[x]+","+stat[match+1]+","+stat[match+2]+"\n")  
        else:
            fout.write(countries[x-1]+":{\"fillKey\":\"No Data\"},\n")
            fout2.write(countries[x-1]+","+countries[x]+",0,0\n")         
        

fout.close()
fout2.close()
fin1.close()
fin2.close()

#compile unemployment
fout = open("MapUnemploymentColorCode","w")
fout2 = open("UnemploymentData","w")
fin1 = open("countries","r")
fin2 = open("unemployment.csv","r")
fout2.write("CountryCode,CountryName,Men,Women\n")

#convert contries to array 
lines= fin1.readlines()
for x in range (0, len(lines)):
    lines[x] = lines[x].rstrip()
lines = ",".join(lines);
countries = lines.split(',')

#convert csv to array
lines= fin2.readlines()
lines= "\r".join(lines)
lines = lines.split('\r')
stat = []
for x in range (0, len(lines)):
    if (x%2 == 0):
        stat.append(lines[x])
stat = ",".join(stat)
stat = stat.split(",")

#compile color code 
for x in range (0, len(countries)):
    if (x%2 != 0):
        if(countries[x] in stat):
            match = stat.index(countries[x])
            fout.write(countries[x-1]+":{\"fillKey\":\"" + percentDiff(float(stat[match+1]),float(stat[match+2])) + "\"},\n")
            fout2.write(countries[x-1]+","+countries[x]+","+stat[match+1]+","+stat[match+2]+"\n") 
        else:
            fout.write(countries[x-1]+":{\"fillKey\":\"No Data\"},\n")
            fout2.write(countries[x-1]+","+countries[x]+",0,0\n")            


fout.close()
fout2.close()
fin1.close()
fin2.close()

#compile unemployment
fout = open("ParlimentColorCode","w")
fout2 = open("ParlimentData","w")
fin1 = open("countries","r")
fin2 = open("parliment.csv","r")
fout2.write("CountryCode,CountryName,Men,Women\n")

#convert contries to array 
lines= fin1.readlines()
for x in range (0, len(lines)):
    lines[x] = lines[x].rstrip()
lines = ",".join(lines);
countries = lines.split(',')

#convert csv to array
lines= fin2.readlines()
lines= "\r".join(lines)
lines = lines.split('\r')
stat = []
for x in range (0, len(lines)):
    if (x%2 == 0):
        stat.append(lines[x])
stat = ",".join(stat)
stat = stat.split(",")

#compile color code 
for x in range (0, len(countries)):
    if (x%2 != 0):
        if(countries[x] in stat):
            match = stat.index(countries[x])
            fout.write(countries[x-1]+":{\"fillKey\":\"" + percentDiff((100-float(stat[match+1])),float(stat[match+1])) + "\"},\n")
            fout2.write(countries[x-1]+","+countries[x]+","+str(100-float(stat[match+1]))+","+(stat[match+1])+"\n") 
        else:
            fout.write(countries[x-1]+":{\"fillKey\":\"No Data\"},\n")
            fout2.write(countries[x-1]+","+countries[x]+",0,0\n")            


fout.close()
fout2.close()
fin1.close()
fin2.close()