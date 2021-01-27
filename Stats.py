from  StatsElement import StatsElement

class Stats:
    """class to store statistic user"""
    def __init__(self, json_object):
        self.json = json_object
        self.lifetime_stats = self.json['data']['segments'][0]['stats']
        self.lifetime_info = self.set_type_info(self.lifetime_stats).toDict()  # stats for lifetime create to dict

        self.warzone_stats = self.json['data']['segments'][1]['stats']
        self.warzone_info = self.set_type_info(self.warzone_stats).toDict()  # stats for warzone create to dict

        #  self.plunder_stats = self.json['data']['segments'][2]['stats']
        #  self.plunder_info = self.set_type(self.plunder_stats)  # stats for plunder


    def set_type_info(self, type_stats):
        """return class StatsElement"""
        kills = type_stats['kills']['value']
        deaths = type_stats['deaths']['value']
        downs = type_stats['downs']['value']
        kda = type_stats['kdRatio']['value']
        wins = type_stats['wins']['value']
        top5 = type_stats['top5']['value']
        top10 = type_stats['top10']['value']
        top25 = type_stats['top25']['value']
        wr = type_stats['wlRatio']['displayValue']
        avgLife = type_stats['averageLife']['displayValue']
        return StatsElement(kills, deaths, downs, kda, wins, top5, top10, top25, wr, avgLife)

    def toDict(self):
        stats = dict(warzone=self.warzone_info, lifetime=self.lifetime_info)
        return dict(Stats=stats)
