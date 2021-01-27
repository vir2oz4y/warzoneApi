class Weapon:
    """Gets stats weapon from json response"""

    def __init__(self, jsonObject):
        self.category = self.getCategory(jsonObject)
        self.name = self.getName(jsonObject)
        self.stats = self.getStats(jsonObject)
        self.imgUrl = self.getImgUrl(jsonObject)

    def getCategory(self, json):
        return json['metadata']['category']

    def getName(self, json):
        return json['metadata']['name']

    def getImgUrl(self, json):
        return json['metadata']['imageUrl']

    def getStats(self, json):
        return Stats(json['stats'])

    def toJson(self):
        dictObject = dict(category=self.category,
                          name=self.name,
                          imgUrl=self.imgUrl,
                          stats=self.stats.toDict()
                          )
        return dictObject


class Stats:
    """This object to stats weapon"""

    def __init__(self, stats):
        self.death = stats['deaths']['value']
        self.kills = stats['kills']['value']
        self.headShots = stats['headShots']['value']
        self.headShotsAccuracy = stats['headShotsAccuracy']['value']
        self.hits = stats['hits']['value']
        self.kDRatio = stats['kDRatio']['value']
        self.shots = stats['shots']['value']
        self.shotsAccuracy = stats['shotsAccuracy']['value']

    def toDict(self):
        dictObject = dict(death=self.death,
                          kills=self.kills,
                          headShots=self.headShots,
                          headShotsAccuracy=self.headShotsAccuracy,
                          hits=self.hits,
                          kDRatio=self.kDRatio,
                          shots=self.shots,
                          shotsAccuracy=self.shotsAccuracy)
        return dictObject
