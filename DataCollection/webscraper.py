import requests
from bs4 import BeautifulSoup as bs
from fencerInfo import FencerData as fd


class webscraper:
    def __init__(self):
        self.fencers = []

    def generateFencerList(self):
        #List of all male sabre fencers in the database
        url = "https://fencingdatabase.com/?firstname=&lastname=&weapon=sabre&gender=male&tournament=all&year=all&opposing-score=0&opposing-lastname=&submit-search=Search+Fencers"
        page = requests.get(url)
        soup = bs(page.content, "html.parser")
    
        
        links = soup.find_all("a")

        for link in links:
            linkStr = link.get("href")

            if not ( "/fencers/" in linkStr):
                continue

            self.fencers.append(fd(linkStr.removeprefix("/fencers/")))

    def collectFencerData(self):
        baseUrl = "https://www.fencingdatabase.com/fencers/"

        for fencer in self.fencers:
            fencerPage = requests.get(baseUrl + fencer.ID)
            soup = bs(fencerPage.content, "html.parser")

            fencer.name = soup.find("div", class_="fencer-name").removeprefix("Name: ")
            fencer.country = soup.find("div", class_="fencer-country").removeprefix("Country Code: ")
            fencer.totalTouches = int(soup.find("div", class_="fencer-touches").removeprefix("Total touches: "))
            fencer.favouriteTarget = soup.find("div", class_="fencer-hit-location").removeprefix("Favourite Place To Score: ")

            # finding opponents and hit delta

            for 


        

if __name__ == "__main__":
    test = webscraper()
    test.generateFencerList()
    test.collectFencerData()