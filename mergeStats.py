import csv
import os

print('Now start merging statistics')


statsPath='./stats/'
fileList=os.listdir(statsPath)
print(fileList)
stats={}
for i in range(0,len(fileList)):
    path=os.path.join(statsPath,fileList[i])
    if os.path.isfile(path):
        fr=open(path,'r')
        csv_reader=csv.reader(fr)
        for row in csv_reader:
            if row[0] in stats:
                stats[row[0]]+=int(row[1])
            else:
                stats[row[0]]=int(row[1])
        fr.close()


sortedDic=sorted(stats.items(),key=lambda d:d[1],reverse=True);
fw=open("./statsSorted.csv","w")
w=csv.writer(fw)
for (key,val) in sortedDic:
    w.writerow([key,val])

for i in range(10):
    print(sortedDic[i][0])

fw.close()
