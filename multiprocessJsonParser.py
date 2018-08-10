import json
import csv
from multiprocessing import Pool
import os


def thatProcess(id,path):
    f=open(path,'r')
    print('Running process %s, pid is %s' %(id,os.getpid()))
    stats={}
    processOneFileAtATime(f,stats)
    f.close()
    fw=open("./stats/stats%s.csv"%id,"w")
    w=csv.writer(fw)
    for (key,val) in stats.items():
        w.writerow([key,val])
    fw.close()
    print('Finished process %s, pid  %s' %(id,os.getpid()))

def processOneFileAtATime(f,stats):
    r=f.readline()
    while r!='':
        hj=json.loads(r)
        if 'content' in hj:
            dom=hj['domain']
            if dom in stats:
                stats[dom]=stats[dom]+1
            else:
                stats[dom]=1
        r=f.readline()

dataset='./ded/'
fileList=os.listdir(dataset)
p=Pool(16)
print(fileList)
for i in range(0+23,23+len(fileList)):
    print(i)
    path=os.path.join(dataset,fileList[i-23])
    print(path)
    if os.path.isfile(path):
        p.apply_async(thatProcess,args=(i,path))

p.close()
p.join()
print('All subprocess done.')
