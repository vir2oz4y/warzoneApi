import requests

class CodTracker:
    API = 'https://api.tracker.gg/api/v2/warzone/standard/profile/battlenet/{name}%23{cod}'


    def headers(self, link):
        header = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en',
            'Referer': link + '/overview',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.60 Mobile Safari/537.36'
        }
        return header

    # check account for exist
    def check_acc(self, user):
        link = self.API.format(name=user.wz_name, cod=user.id)  # create link
        response = requests.get(link, headers=self.headers(link))
        if response.status_code == 404:  # if account not exists
            return False
        return True

    def get_stats_profile(self, user):  # get stats from codTracker
        link = self.API.format(name=user['wz_name'], cod=user['id'])  # create link
        response = requests.get(link, headers=self.headers(link))
        json_object = response.json()
        return json_object

    def get_stats_weapon(self,user):
        link = self.API.format(name=user['wz_name'], cod=user['id']) + '/segments/weapon'
        response = requests.get(link, headers=self.headers(link))
        json_object = response.json()
        return  json_object['data']

    def get_last_matches(self, user):
        link = 'https://api.tracker.gg/api/v1/warzone/matches/battlenet/{name}%23{cod}?type=wz&next=null'.format(name=user['wz_name'], cod=user['id'])
        response = requests.get(link, headers=self.headers(link))
        json_object = response.json()
        return json_object['data']['matches']

    def get_match(self, idMatch):
        link = 'https://api.tracker.gg/api/v1/warzone/matches/{idMatch}'.format(idMatch=idMatch)
        response = requests.get(link, headers=self.headers(link))
        json_object = response.json()
        return json_object

if __name__=='__main__':
    pass

