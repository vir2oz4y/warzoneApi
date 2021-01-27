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
        return StatsElement(type_stats)

    def toDict(self):
        stats = dict(warzone=self.warzone_info, lifetime=self.lifetime_info)
        return dict(Stats=stats)
