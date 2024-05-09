class FencerData:
    def __init__(self, licenceNo):
        # Data Scraped From fencingdatabase.com
        self.ID = int(licenceNo)
        self.name = ""
        self.country = ""
        self.totalTouches = 0
        self.favouriteTarget = ""
        self.opponents = {} # fencer id will be the key with point delta as the data

        # Data Scraped from fie.org
        self.BestYear = 0
        self.TotalPoints = 0
        self.CurrentRank = 0
        self.CurrentPoints = 0
        self.Handedness = ""
        self.Age = 0

class BoutInfo:
    def __init__(self, fencer1, fencer2, f1Touches, f2Touches):
        # ensuring the smallest number always goes first
        if fencer1 < fencer2:
            self.fencer1 = fencer1
            self.fencer2 = fencer2
        else:
            self.fencer1 = fencer2
            self.fencer2 = fencer1

        self.f1Touches = f1Touches
        self.f2Touches = f2Touches
        self.delta = f1Touches - f2Touches # f1 - f2

        self.winner = self.fencer1 if self.delta < 0 else self.fencer2


if __name__ == "__main__":
    pass