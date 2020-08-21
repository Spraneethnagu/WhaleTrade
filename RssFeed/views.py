from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from .feedparser import parse

from datetime import date, datetime

today = date.today()


def index(request):
    NewsFeed1 = parse("https://cointelegraph.com/rss")
    NewsFeed2 = parse("https://news.bitcoin.com/feed/")
    NewsFeed3 = parse("https://www.reddit.com/r/CryptoCurrency/top/.rss?format=xml")
    
    cointelegraph,bitcoin,reddit=[],[],[]

    i=NewsFeed1.entries
    for a in i:
        datetime1= a.published[5:25]
        dict = {
            'title': a.title,
            'img': a.links[1].href,
            'link': a.link,
            'date': a.published[5:16],
            
            'datetime2': datetime.strptime(datetime1, '%d %b %Y %H:%M:%S'),
            'tag': a.tags[0].term,
            'name': "CoinTelegraph"
            }
        cointelegraph.append(dict)
    
    i=NewsFeed2.entries

    for a in i:
        b=a.summary
        c = parse(b)
        img = c.feed.img["src"]
        
        datetime1= a.published[5:25]
        
        dict={
            'title': a.title,
            'link': a.link,
            'date': a.published[5:16],
                
            'datetime2': datetime.strptime(datetime1, '%d %b %Y %H:%M:%S'),
            'tag': a.tags[0].term,
            'img': img,
            'name': "Bitcoin"
            }
        bitcoin.append(dict)
        

    i=NewsFeed3.entries
    for a in i:

        c= a.content[0].value
        b= parse(c)
        datetime1 = a.updated[0:10] + " " +a.updated[11:19]
        
        if b.feed.has_key('img'):
            img = b.feed.img["src"]
            
            dict = {
                'title': a.title,
                'link': a.link,
                'date': a.updated[0:10],
                
                'datetime2': datetime.strptime(datetime1, '%Y-%m-%d %H:%M:%S'),
                'tag': a.tags[0].term,
                'img': img,
                'name': "Reddit"
                }
            reddit.append(dict)
                
        else:
            pass
        


    
    l= cointelegraph+bitcoin+reddit
    lf = sorted(l, key = lambda i: i['datetime2'], reverse= True)
    l1 = lf[0:9]
    l2 = lf[9:27]

    a= l1[0]
    b= l1[1]
    c=l1[2]
    d=l1[3]
    e=l1[4]
    f=l1[5]
    g=l1[6]
    h=l1[7]
    i=l1[8]
    

    context= {
        'a': a,
        'b': b,
        'c': c,
        'd': d,
        'e': e,
        'f': f,
        'g': g,
        'h': h,
        'i': i,
        'l2': l2,
        'today': today
    }
    return render(request,'index.html',context)
