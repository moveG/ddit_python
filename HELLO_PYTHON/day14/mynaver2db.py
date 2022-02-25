import os
import sys
import urllib.request
from bs4 import BeautifulSoup
from day14.dao_movie import DaoMovie

dm = DaoMovie()

client_id = "OA5mkGKFhcftueaegPWl"
client_secret = "e4OzE9xDLZ"
encText = urllib.parse.quote("해리포터")
url = "    https://openapi.naver.com/v1/search/movie.xml?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    
    moviexml = response_body.decode('utf-8')
    
    soup = BeautifulSoup(moviexml, "xml")
    items = soup.select('item')
    
    for i in items:
        title = i.title.text.replace("<b>", "").replace("</b>", "")
        link = i.link.text
        image = i.image.text
        subtitle = i.subtitle.text.replace("'", "")
        pubdate = i.pubDate.text
        director = i.director.text.replace("|", ", ")
        actor = i.actor.text.replace("|", ", ")
        userrating = i.userRating.text
        print(title, link, image, subtitle, pubdate, director, actor, userrating)
        
        result = "ng"
        cnt = dm.insert(title, link, image, subtitle, pubdate, director, actor, userrating)
        if cnt == 1:
            result = "ok"
        
        print(result)
    
else:
    print("Error Code:" + rescode)