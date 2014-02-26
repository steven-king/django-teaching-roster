from bs4 import BeautifulSoup

print ("starting to scrape")


#Use code below when file to import is on web server :
response = urllib2.urlopen("http://www.goheels.com/SportSelect.dbml?DB_OEM_ID=3350&SPID=12960&SPSID=668154&SITE=UNC&DB_OEM_ID=3350")
html = response.read()

#end server version         

#Use this code when file is local:
#with open ("transcript.html", "r") as tempFile:
#html=tempFile.read();


#end local version
#print html;

soup = BeautifulSoup(html)

tabledata = soup.find("table", {"id" : "roster-table"})  #find the proper table
player_names = [] #list to stor every player in the table
player_links = []



for link in tabledata.find_all('a'):
    player_links.append(link.get('href'))
    player_names.append(link.get('title'))
    
for position in tabledata.find_all("td", {"class" : "position"}):
    player_position.append(position.text.strip())


#print player_names
print player_position
#player_name = (soup.find_all)
print player_links
