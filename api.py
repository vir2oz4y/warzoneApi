from flask import Flask, jsonify
from CodTracker import CodTracker
from WeaponInfo.Weapon import Weapon
from MatchInfo.Match import Match
from Stats import Stats

app = Flask(__name__)
API = 'https://api.tracker.gg/api/v2/warzone/standard/profile/battlenet/{name}%23{cod}'
codTrac = CodTracker()

def getUser(nickname):
    nickname = nickname.split('=')
    user = dict(wz_name=nickname[0], id=nickname[1])
    return user

@app.route('/warzone/api/v1.0/stats/<nickname>', methods=['GET'])  # to get profile stats
def get_stats(nickname):
    """return profile statistics """
    user = getUser(nickname)  # create user
    jsonWarzoneStats = codTrac.get_stats_profile(user)  # get json
    stats = Stats(jsonWarzoneStats)
    return jsonify(stats.toDict())  # return json object


@app.route('/warzone/api/v1.0/stats/<nickname>/weapons', methods=['GET'])
def get_stats_weapon(nickname):
    """return json of statistics weapons"""
    user = getUser(nickname)  # get user
    jsonWeapons = codTrac.get_stats_weapon(user)  # get json
    weapons = [Weapon(jsonWeapon).toJson() for jsonWeapon in jsonWeapons]  # create list of dict weapons
    return jsonify(weapons)  # return json object


@app.route('/warzone/api/v1.0/stats/<nickname>/matches', methods=['GET'])
def get_last_matches(nickname):
    """return json of 19 last matches"""
    user = getUser(nickname)  # get user
    jsonMatches = codTrac.get_last_matches(user)  # get json
    matches = [Match(match).toDict() for match in jsonMatches]
    matches = dict(matches=matches)
    return jsonify(matches)  # return json object


@app.route('/warzone/api/v1.0/stats/matches/<idMatch>', methods=['GET'])
def get_match(idMatch):
    """return json info match"""
    jsonMatch = codTrac.get_match(idMatch)
    match = Match(jsonMatch['data']).toDict()
    match = dict(match=match)
    return jsonify(match)


if __name__ == '__main__':
    app.run(debug=True)
