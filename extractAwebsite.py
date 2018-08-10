import json
import os
from html.parser import HTMLParser

visited=set()

class MyHTMLParser(HTMLParser):
    def __init__(self,temp):
        HTMLParser.__init__(self)
        self.text=''
        self.temp=temp
        if self.temp=='india.com':
            self.meetAside=False
        elif self.temp=='rekhta.org':
            self.meetDiv=False
        else:
            pass
        
    
    def handle_starttag(self, tag, attrs):
        if self.temp=='india.com':
            if tag=='aside':
                self.meetAside=True
        elif self.temp=='rekhta.org':
            if tag=='div':
                self.meetDiv=True
        else:
            pass
 
    def handle_endtag(self, tag):
        if self.temp=='india.com':
            if tag=='aside':
                self.meetAside=False
        elif self.temp=='rekhta.org':
            if tag=='div':
                self.meetDiv=False
        else:
            pass
    
    def handle_data(self, data):
        if self.temp=='india.com':
            if self.meetAside==True and self.lasttag == 'p':
                self.text+=data
        elif self.temp=='rekhta.org':
            if self.meetDiv==True and self.lasttag == 'p':
                self.text+=data
        else:
            pass

        

    

def processOneFileAtATime(f,fw,domWanted,visited,mp):
    r=f.readline()
    while r!='':
        print("running")
        hj=json.loads(r)
        if 'content' in hj:
            dom=hj['domain']
            if dom==domWanted and hj['url'] not in visited:
                visited.add(hj['url'])
                fw.write(hj['url']+'\n')
                mp.text=''
                mp.feed(hj['content'])
                fw.write(mp.text+'\n')
                fw.write('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'+'\n')
        r=f.readline()



dataset='./dataset/'
fileList=os.listdir(dataset)
print(fileList)
fw=open('./webPages','w')
domw=input('Input the domain name: ')
mp=MyHTMLParser(domw)
for i in range(0,len(fileList)):
    print(i)
    path=os.path.join(dataset,fileList[i])
    print(path)
    if os.path.isfile(path):
        f=open(path,"r")
        processOneFileAtATime(f,fw,domw,visited,mp)
        f.close()

fw.close()
print('num of webs: ',len(visited))
