from DAL import * 


class BLL: 
    def __init__(self): 
        self.dal = DAL()

    def login(self, user, password, database): 
        self.dal.config = {
            "user": user,
            "password": password,   
            "database": database    
        }


    def newPlayer(self, name, position, team, nation):
        test = self.dal.players.addPlayer(name, position, team, nation) 
        return test
        
    
    def getTeamRoster(self, teamName):
         
        result = self.dal.teams.getTeamRoster(teamName) 
        return "\n".join(f"{player[0]} | {player[1]} | {player[2]}" for player in result)

    def teamUSA(self): 
        result = self.dal.teams.teamUSA() 
        if result:
         return "\n".join(f"{player[0]} | {player[1]}" for player in result)
        else: 
            return f"Team USA Could not be generated"
    
    def playerProfile(self): 
        result = self.dal.players.playerProfile()
        return "\n".join(f"{player[0]} | {player[1]} | {player[2]}" for player in result)
        
    
    def rosterMove(self, player, newteam): 
        result = self.dal.players.rosterMove(player, newteam)
        if result:

            return f"Move Completed:\n{player} has been moved to the {newteam}"
        else: 
            return f"MOVE FAILED"
        
    def deletePlayer(self, pName):
        result = self.dal.players.deletePlayer(pName)
        if result: 
            return f'Player {pName} has been removed from our database'
        else: 
            return f'Failed to delete {pName}'
        
    
 
