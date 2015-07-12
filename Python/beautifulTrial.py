from bs4 import BeautifulSoup
import urllib.request
url="http://www.utexas.edu/world/univ/alpha/"
page= urllib.request.urlopen(url)
soup = BeautifulSoup(page.read())
universities=soup.findAll('a',{'class':'institution'})
for eachuniversity in universities:
   print(eachuniversity['href']+","+eachuniversity.string)