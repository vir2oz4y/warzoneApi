from Statistics.Statictics import StatisticWarzone, BaseStats


class Match:
    """В этом классе хранятся данные о матче игрока"""
    def __init__(self, jsonObject):
        self.id = self.getId(jsonObject)  # id матча
        self.duration = self.getDuration(jsonObject)  # this duration
        self.mode = self.getMode(jsonObject)  # modeGame
        self.timeStart = self.getTimeStart(jsonObject)  # time start match
        self.segments = self.getSegments(jsonObject)  # segments


    def getId(self, jsonObject):  # get id from json
        return  jsonObject['attributes']['id']

    def getDuration(self, jsonObject):  # get duration from json
        return jsonObject['metadata']['duration']['displayValue']

    def getMode(self,jsonObject):  # get mode from json
        return jsonObject['metadata']['modeName']

    def getTimeStart(self, jsonObject):  # get start time match
        return jsonObject['metadata']['timestamp']

    def getSegments(self, jsonObject):  # get list of segments this match
        jsonObjects = jsonObject['segments']
        segments = [Segments(jsonObj, self.mode).toDict() for jsonObj in jsonObjects]  # create list dict of segments
        return segments


    def toDict(self):  # create dict this class
        return dict(id=self.id,
                    duration=self.duration,
                    mode=self.mode,
                    timeStart=self.timeStart,
                    segments=self.segments,
                    )

class Segments:
    """In this class we store data about user and stats"""
    def __init__(self, jsonObject, mode):
        self.team = self.getTeam(jsonObject)  # team alive
        self.clanTag = self.getClanTag(jsonObject)  # clan tag
        self.placement = self.getPlacement(jsonObject)  # placement of this game
        self.userName = self.getUserName(jsonObject)  # username user in game
        self.statistics = self.getStatistics(jsonObject, mode)  # statistics of gamer

    def getStatistics(self, jsonObject, mode):  # get stats with selected mode game
        modes = ['br_brtrios','br_brquads','br_brduos','br_brsolo']  # modes warzone
        if mode in modes:
            return StatisticWarzone(jsonObject['stats'])  # statistic warzone
        return BaseStats(jsonObject['stats'])  # another mode game

    def getTeam(self, jsonObject):  # get team from json
        return jsonObject['attributes']['team']

    def getClanTag(self, jsonObject):  # get clan tag from json
        return jsonObject['metadata']['clanTag']

    def getPlacement(self, jsonObject):  # get placement from json
        return jsonObject['metadata']['placement']

    def getUserName(self, jsonObject):  # get username from json
        return jsonObject['metadata']['platformUserHandle']

    def toDict(self):  # create dict this class
        return dict(team=self.team,
                    clanTag=self.clanTag,
                    placement=self.placement,
                    userName=self.userName,
                    statistics=self.statistics.toDict())



