from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
from roster.models import Student, Course

#import two lines below only if from URL not local file.
import urllib2
import re



class Command(BaseCommand):
    args = '<url>'
    help = 'Parses and imports players from Goheels.com'
    
    def handle(self, *args, **options):
        try:
            print ("trying to scrape")



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
            player_numbers = []
            player_links = []
            player_position = []
            countPlayers = 0;
            

            for link in tabledata.find_all('a'):
                player_links.append(link.get('href'))
                player_names.append(link.get('title'))
                
            for position in tabledata.find_all("td", {"class" : "position"}):
                player_position.append(position.text.strip())
    

            #print player_names
            print player_position
            #player_name = (soup.find_all)
            print player_links
            
            for player_link, val in enumerate(player_links):
                
                print(player_link, val, countPlayers)
                response = urllib2.urlopen("http://goheels.com", val)
                html = response.read()
                soup = BeautifulSoup(html)
                print(player_names[countPlayers])
                player_data = Student.objects.create(name= player_names[countPlayers])
                player_data.save()
                countPlayers += 1;

            
        except Student.DoesNotExist:
            raise CommandError('didn\'t work')
        
        
        #echo ("start of scrape.py")
        self.stdout.write("end of scrape.py")
