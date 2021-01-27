class StatsElement:
    """class elements of statistics"""
    def __init__(self, kills, deaths, downs, kda, wins, top5, top10, top25, wr, avgLife):
        self.kills = kills
        self.deaths = deaths
        self.downs = downs
        self.kda = kda
        self.wins = wins
        self.top5 = top5
        self.top10 = top10
        self.top25 = top25
        self.wr = wr
        self.avgLife = avgLife

    def toDict(self):
        return dict(kills=self.kills,
                    deaths=self.deaths,
                    downs=self.downs,
                    kda=self.kda,
                    wins=self.wins,
                    top5=self.top5,
                    top10=self.top10,
                    top25=self.top25,
                    winrate=self.wr,
                    avgLife=self.avgLife)
