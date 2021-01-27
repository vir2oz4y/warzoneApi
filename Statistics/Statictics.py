class BaseStats:
    """Base class to statistics"""
    def __init__(self, jsonObject):
        self.assists = jsonObject['stats']['assists']['value']
        self.damageDone = jsonObject['stats']['damageDone']['value']
        self.damageDonePerMinute = jsonObject['stats']['damageDonePerMinute']['value']
        self.damageTaken = jsonObject['stats']['damageTaken']['value']
        self.deaths = jsonObject['stats']['deaths']['value']
        self.headshots = jsonObject['stats']['headshots']['value']
        self.kdRatio = jsonObject['stats']['kdRatio']['value']
        self.kills = jsonObject['stats']['kills']['value']
        self.longestStreak = jsonObject['stats']['longestStreak']['value']
        self.matchXp = jsonObject['stats']['matchXp']['value']
        self.percentTimeMoving = jsonObject['stats']['percentTimeMoving']['value']
        self.score = jsonObject['stats']['score']['value']
        self.scorePerMinute = jsonObject['stats']['scorePerMinute']['value']
        self.scoreXp = jsonObject['stats']['scoreXp']['value']

    def toDict(self):
        return dict(assists=self.assists,
                    damageDone=self.damageDone,
                    damageDonePerMinute=self.damageDonePerMinute,
                    damageTaken=self.damageTaken,
                    deaths=self.deaths,
                    headshots=self.headshots,
                    kdRatio=self.kdRatio,
                    kills=self.kills,
                    longestStreak=self.longestStreak,
                    matchXp=self.matchXp,
                    percentTimeMoving=self.percentTimeMoving,
                    score=self.score,
                    scorePerMinute=self.scorePerMinute,
                    scoreXp=self.scoreXp)


class StatisticWarzone(BaseStats):
    """Class to statistic warzone"""
    def __init__(self,jsonObject):
        super().__init__(jsonObject)
        self.gulagKills = jsonObject['stats']['gulagKills']['value']
        self.teamPlacement = jsonObject['stats']['teamPlacement']['value']
        self.teamSurvivalTime = jsonObject['stats']['teamSurvivalTime']['value']
        self.placement = self.getPlacement(jsonObject)

    def getPlacement(self, jsonObject):
        try:
            return jsonObject['stats']['placement']['value']
        except KeyError:
            return jsonObject['metadata']['placement']['value']


    def toDict(self):
        newDict = super(StatisticWarzone, self).toDict()
        newDict['teamPlacement']=self.teamPlacement
        newDict['teamSurvivalTime'] = self.teamSurvivalTime
        newDict['gulagKills'] = self.gulagKills
        newDict['placement'] = self.placement
        return  newDict


