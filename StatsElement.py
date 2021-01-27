class StatsElement:
    """class elements of statistics"""
    def __init__(self, type_stats):
        self.kills = type_stats['kills']['value']
        self.deaths = type_stats['deaths']['value']
        self.downs = type_stats['downs']['value']
        self.kda = type_stats['kdRatio']['value']
        self.wins = type_stats['wins']['value']
        self.top5 = type_stats['top5']['value']
        self.top10 = type_stats['top10']['value']
        self.top25 = type_stats['top25']['value']
        self.wr = type_stats['wlRatio']['displayValue']
        self.avgLife = type_stats['averageLife']['displayValue']
        self.contracts = type_stats['contracts']['value']
        self.gamesPlayed = type_stats['gamesPlayed']['value']
        self.scorePerGame = type_stats['scorePerGame']['value']
        self.scorePerMinute = type_stats['scorePerMinute']['value']
        self.timePlayed = type_stats['timePlayed']['value']
        self.weeklyDamagePerMatch = type_stats['weeklyDamagePerMatch']['value']


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
                    avgLife=self.avgLife,
                    contracts=self.contracts,
                    gamesPlayed=self.gamesPlayed,
                    scorePerGame=self.scorePerGame,
                    scorePerMinute=self.scorePerMinute,
                    timePlayed=self.timePlayed,
                    weeklyDamagePerMatch=self.weeklyDamagePerMatch)
