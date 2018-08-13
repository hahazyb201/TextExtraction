import os

print('Now start merging documents!')

statsPath='./webPages/'
fileList=os.listdir(statsPath)
print(fileList)

fw=open('./mergedCorpus','w')
for i in range(1,len(fileList)):
	path=os.path.join(statsPath,fileList[i])
	if os.path.isfile(path):
        fr=open(path,'r')
        r=fr.readline()
        while r!='':
        	if r=='\n' or r=='\r' or r=='\n\r' or r=='\r\n':
        		continue
        	if r[:4]=='http':
        		continue
        	if r[:4]=='^^^^':
        		continue
        	fw.write(r+'\n')
        	r=fr.readline()
        fr.close()


fw.close()