import os
'''
65-90 A-Z
97-122 a-z
192-253 letters with tones
'''
print('Now start merging documents!')

def isHinglish(s):
	checkLen=int(0.2*len(s))
	cs=s[:checkLen]
	cnt=0
    for c in cs:
	    asci=ord(c)
        if (asci>=65 and asci<=90) or (asci>=97 and asci<=122) or (asci>=192 and asci<=253):
            cnt+=1
    return True if cnt>=0.4*checkLen else False


		
statsPath='./webPages/'
fileList=os.listdir(statsPath)
print(fileList)

fw=open('./mergedCorpusHinglish','w')
for i in range(0,len(fileList)):
	path=os.path.join(statsPath,fileList[i])
	if os.path.isfile(path):
        fr=open(path,'r')
        r=fr.readline()
        while r!='':
        	if r=='\n' or r=='\r' or r=='\n\r' or r=='\r\n':
        		r=fr.readline()
        		continue
        	if r[:4]=='http':
        		r=fr.readline()
        		continue
        	if r[:4]=='^^^^':
        		r=fr.readline()
        		continue
        	if isHinglish(r):	
        	    fw.write(r+'\n')
        	r=fr.readline()
        fr.close()


fw.close()