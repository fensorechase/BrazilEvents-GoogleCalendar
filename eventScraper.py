#Integrate tag data with Google Calendar API script. Write event.
from bs4 import BeautifulSoup
from createGCalEvent import create_event
from googletrans import Translator
import requests
import re
import csv
import urllib3

#Call function to recieve URL
exampleURL = 'http://www.calendariodoagronegocio.com.br/Evento/visualizar/portugues/3226'


def process_URL(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data.decode('utf-8'), features="html.parser")
    return soup


#MAIN 
#soup is the pool of HTML we search from, given a URL
def main():

    url = input('Enter full event URL (n to quit): ')

    repeat = True
    while url != 'n':
        #soup = process_URL(url)
        http = urllib3.PoolManager()
        response = http.request('GET', url)
        soup = BeautifulSoup(response.data.decode('utf-8'), features="html.parser")
        startDate = str(soup.find("span", itemprop="startDate").text)
        startDay = startDate[0: 2]

        startYear = startDate[len(startDate)-4: len(startDate)]

    #FIND Title of event.
        eventTitle = str(soup.title.text)

    #FIND itemprop="endDate"
    #endDate = soup.find("span", itemprop="endDate").text
    #TRANSFORM into date/time
        #FIND itemprop="endDate"
        endDate = str(soup.find("span", itemprop="endDate").text)
        endYear = endDate[len(endDate)-4: len(endDate)]

       

    #FIND "Periodicidade" (FREQUENCY)
        frequency = str(soup.find(text=re.compile("Periodicidade: (.*)")))
        frequency = frequency[15: len(frequency)]

    #FIND ADDRESS
    #soup = BeautifulSoup(str(spanParent), features="html.parser")
        address = str(soup.find("span", itemprop="streetAddress").text)
    #FIND addressLocality
        addressLocality = str(soup.find("span", itemprop="addressLocality").text)
        addressLocality = addressLocality[1: len(addressLocality)]

    #FIND addressRegion
        addressRegion = str(soup.find("span", itemprop="addressRegion").text)

    #FIND "Pais" (Country)
        pais = str(soup.find(text=re.compile("País: (.*)")))
        pais = pais[6:len(pais)]

    #FIND postalCode
        postalCode = str(soup.find("span", itemprop="postalCode").text)
        postalCode = postalCode[1:]

    #FIND "Local" (Location/Venue)
        local = str(soup.find(text=re.compile("Local: (.*)")))
        local = local[7:len(local)]

    #FIND "Categoria" (Category)
        category = str(soup.find(text=re.compile("Categoria: (.*)")))
        category = category[11:len(category)]

    #FIND Segmento (Segment)
        segmento = str(soup.find(text=re.compile("Segmento: (.*)")))
        segmento = segmento[10:len(segmento)]

    #FIND Promoter (promotor)
        promotor = str(soup.find(text=re.compile("Promotor: (.*)")))
        promotor = promotor[10:len(promotor)]

    #FIND address of Promotor
        promotorAddress = str(soup.find(text=re.compile("do Promotor: (.*)")))
        promotorAddress = promotorAddress[22:len(promotorAddress)]

    #FIND telefone
        telefone = str(soup.find(text=re.compile("Telefone: (.*)")))
        telefone = telefone[10:len(telefone)]

        #------------------------------------------------------------------------#
        #Create event: Google Calendar API
        #Translate startDate into English
        translator = Translator()
        create_event('8 am '+str(translator.translate(startDate, dest='en')), eventTitle, local+' '+addressLocality+' '+addressRegion, 1, None)


      #Prompt: Create additional event from additional URL?
        url = input("Enter full event URL (n to quit): ")
        if url == 'n':
                repeat = False

        
if __name__ == "__main__":
    main()
