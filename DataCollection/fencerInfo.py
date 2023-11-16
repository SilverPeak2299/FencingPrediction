class FencerData:
    def __init__(self, licenceNo):
        # Data Scraped From fencingdatabase.com
        self.licenceNo = licenceNo
        self.name = ""
        self.country = ""
        self.favouriteTarget = ""
        self.opponents = []

        # Data Scraped from fie.org
        self.BestYear = 0
        self.TotalPoints = 0
        self.CurrentRank = 0
        self.CurrentPoints = 0
        self.Handedness = ""
        self.Age = 0

    
if __name__ == "__main__":
    pass