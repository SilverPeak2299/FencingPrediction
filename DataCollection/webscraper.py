import requests
from bs4 import BeautifulSoup as bs
from fencerInfo import FencerData as fd


class webscraper:
    def __init__(self):
        self.fencers = []

    def fencingDBSearch(self):
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
            



if __name__ == "__main__":
    test = webscraper()
    test.fencingDBSearch()