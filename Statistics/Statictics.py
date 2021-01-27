class BaseStats:
    """Base class to statistics"""
    def __init__(self, jsonObject):
        self.assists = jsonObject['assists']['value']
        self.damageDone = jsonObject['damageDone']['value']
        self.damageDonePerMinute = jsonObject['damageDonePerMinute']['value']
        self.damageTaken = jsonObject['damageTaken']['value']
        self.deaths = jsonObject['deaths']['value']
        self.headshots = jsonObject['headshots']['value']
        self.kdRatio = jsonObject['kdRatio']['value']
        self.kills = jsonObject['kills']['value']
        self.longestStreak = jsonObject['longestStreak']['value']
        self.matchXp = jsonObject['matchXp']['value']
        self.percentTimeMoving = jsonObject['percentTimeMoving']['value']
        self.placement = jsonObject['placement']['value']
        self.score = jsonObject['score']['value']
        self.scorePerMinute = jsonObject['scorePerMinute']['value']
        self.scoreXp = jsonObject['scoreXp']['value']

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
                    placement=self.placement,
                    score=self.score,
                    scorePerMinute=self.scorePerMinute,
                    scoreXp=self.scoreXp)


class StatisticWarzone(BaseStats):
    """Class to statistic warzone"""
    def __init__(self,jsonObject):
        super().__init__(jsonObject)
        self.gulagKills = jsonObject['gulagKills']['value']
        self.teamPlacement = jsonObject['teamPlacement']['value']
        self.teamSurvivalTime = jsonObject['teamSurvivalTime']['value']

    def toDict(self):
        newDict = super(StatisticWarzone, self).toDict()
        newDict['teamPlacement']=self.teamPlacement
        newDict['teamSurvivalTime'] = self.teamSurvivalTime
        newDict['gulagKills'] = self.gulagKills



class StatisticBloodMoney(BaseStats):
    def __init__(self,jsonObject):
        super().__init__(jsonObject)