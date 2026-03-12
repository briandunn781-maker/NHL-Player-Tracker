from DAL import * 


class BLL: 
    def __init__(self): 
        self.dal = DAL()
        self.player_profile = Player()
    def addPlayer(self):
        name = self.player_profile.get_pName()
        position = self.player_profile.get_position()
        team = self.player_profile.get_team()
        nation = self.player_profile.get_nation()
        gp = self.player_profile.get_gp()
        goals = self.player_profile.get_goals()
        assists = self.player_profile.get_assists()
        points = self.player_profile.get_points()
        AAV = self.player_profile.get_AAV()
        length = self.player_profile.get_Length()
        date = self.player_profile.get_date()
        player_info = self.dal.players.addPlayer(name, position, team, nation)
        player_stats = self.dal.stats.addStats(name, gp, goals, assists, points)
        player_contract = self.dal.contracts.addContract(name, AAV, length, date) 

        return player_info, player_stats, player_contract
        

    
class Player:
    def __init__(self):
        self.pName = None
        self.position = None
        self.team = None
        self.nation = None
        self.gp = None
        self.goals = None
        self.assists = None
        self.points = None
        self.AAV = None
        self.Length = None
        self.date = None

    def set_pName(self, name):
        self.pName = name

    def set_position(self, position):
        self.position = position

    def set_team(self, team):
        self.team = team

    def set_nation(self, nation):
        self.nation = nation

    def set_gp(self, gp):
        self.gp = int(gp) if gp is not None else None

    def set_goals(self, goals):
        self.goals = int(goals) if goals is not None else None

    def set_assists(self, assists):
        self.assists = int(assists) if assists is not None else None

    def set_points(self, points):
        self.points = int(points) if points is not None else None

    def set_AAV(self, aav):
        self.AAV = float(aav) if aav is not None else None

    def set_Length(self, length):
        self.Length = int(length) if length is not None else None

    def set_date(self, date_str):
        from datetime import datetime
        try:
            self.date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except (ValueError, TypeError):
            self.date = None
    
    def get_pName(self):
        return self.pName

    def get_position(self):
        return self.position

    def get_team(self):
        return self.team

    def get_nation(self):
        return self.nation

    def get_gp(self):
        return self.gp

    def get_goals(self):
        return self.goals

    def get_assists(self):
        return self.assists

    def get_points(self):
        return self.points

    def get_AAV(self):
        return self.AAV

    def get_Length(self):
        return self.Length

    def get_date(self):
        return self.date



