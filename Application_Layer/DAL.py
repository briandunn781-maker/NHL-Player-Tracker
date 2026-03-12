import mysql.connector
import random

class DAL:
    def __init__(self):
        self.config = {
            "user": "username",
            "password": "password",   
            "database": "NHL_Top_100" #hardcoded for now for correct syntax
        }
        self.cnx = None 
        self.cursor = None
        self.players = Players(self)
        self.teams = Teams(self)
        self.stats = Stats(self)
        self.nations = OlympicTeam(self)
        self.contracts = Contracts(self)
        
    
    def set_credentials(self, user, password, database): 
        self.config.update({
            "user": user,
            "password": password,
            "database": database
        })


    def _get_connection(self):
        try:
            self.cnx = mysql.connector.connect(**self.config)
            print("Connection Established Successfuly!")
            return self.cnx
            
        except mysql.connector.Error as err:
            print(f"Connection failed: {err}")
            return None

    
    def get_cursor(self):
        self._get_connection()
        self.cursor = self.cnx.cursor()
        return self.cursor
    
    def commit(self):
        if self.cnx:
            try:
                self.cnx.commit()
            except mysql.connector.Error as err:
                print(f"Commit failed: {err}")
        else:
            print("No open connection to commit.")

    
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.cnx:
            self.cnx.close()

class Teams:

    def __init__(self, dal): 
        self.dal = dal
    
    def teamUSA(self):
        cursor = self.dal.get_cursor()
        try:
            cursor.execute("SELECT * FROM Team_USA")
            results = cursor.fetchall()
            return results 
        except Exception as e: 
            print(f"Error: {e}")
        finally:
            cursor.close() 
    
    def getTeamID(self, teamName): 
        cursor = self.dal.get_cursor()
        func = "SELECT getTeamID(%s);"
        try:
            cursor.execute(func, [teamName])
            results = cursor.fetchone()
            if -1 in results: 
                return 'Team ID not valid'
            else: 
             return results[0]
        finally:
            cursor.close() 
    
    def getTeamRoster(self, teamName): 
        cursor = self.dal.get_cursor()
        query = "CALL getTeamRoster(%s)" 
        try: 
            cursor.execute(query, [teamName])
            results = cursor.fetchall()                
            return results
        finally: 
            cursor.close()



class Players:

    def __init__(self, dal): 
        self.dal = dal

    def getPlayerID(self, playerName): 
        cursor = self.dal.get_cursor() 
        query = "SELECT getPlayerID(%s)" 
        try: 
            cursor.execute(query, [playerName])
            results = cursor.fetchone()
            if -1 in results: 
                return 'player ID not in our database'
            else: 
                return results[0]
        finally: 
            cursor.close()
    
    def addPlayer(self, playerName, playerPosition, playerTeam, nation):
        query = "CALL addPlayer(%s, %s, %s, %s)"
        cursor = self.dal.get_cursor()
        try:
            cursor.execute(query, (playerName, playerPosition, playerTeam, nation))
            result = cursor.fetchall()
            self.dal.commit()
            return f'Player {playerName} added'
        except Exception as e: 
            print(f"Add Failed: {e}")
        finally: 
            cursor.close()

    def deletePlayer(self, playerName): 
        query = "CALL deletePlayer(%s)"
        cursor = self.dal.get_cursor()
        try: 
            cursor.execute(query, (playerName,))
            self.dal.commit()
            return True
        except Exception as e: 
            return f'Add failed {e}'
        finally:
            cursor.close()

    def viewPlayer(self): 
        name = random.randint(0,49)
        cursor = self.dal.get_cursor()
        query = "SELECT Players.pName, Players.position, Teams.Team, Olympic_Team.Country FROM Players JOIN Teams ON Players.tID = Teams.Team_ID JOIN Olympic_Team ON Olympic_Team.Country_ID = Players.Country WHERE Players.player_ID = %s;"
        try: 
            cursor.execute(query, [name])
            result = cursor.fetchall()
            return result
        except Exception as e: 
            print(f"Error Fetching player {e}")
        finally: 
            cursor.close()
 
    def playerProfile(self): 
        cursor = self.dal.get_cursor() 
        query = "SELECT * FROM Player_Profile" 
        try: 
            cursor.execute(query,)
            results = cursor.fetchall()
            if -1 in results: 
                return 'player ID not in our database'
            else: 
                return results
        finally: 
            cursor.close()
        

    
    def rosterMove(self, playerName, newTeam): 
        cursor = self.dal.get_cursor()
        query = "CALL rosterMove(%s, %s)"
        try: 
            cursor.execute(query, (playerName, newTeam))
            self.dal.commit()
            print(f"Player {playerName} moved to new team: {newTeam}")
            return True
        except Exception as e: 
            print(f"Error moving player {e}")
        finally: 
            cursor.close()


class Stats:

    def __init__(self, dal): 
        self.dal = dal

    def addStats(self, playerName, playerGP, playerGoals, playerAssists, playerPoints): 
        cursor = self.dal.get_cursor()
        query = "CALL addStats(%s, %s, %s, %s, %s)"
        try: 
            cursor.execute(query, (playerName, playerGP, playerGoals, playerAssists, playerPoints))
            self.dal.commit()
            print(f"Stats added for {playerName}\nGames Played: {playerGP}\nGoals: {playerGoals}\nAssists: {playerAssists}\nPoints: {playerPoints}")
        except Exception as e: 
            print(f"Add Failed: {e}")
        finally: 
            cursor.close()
class OlympicTeam:

    def __init__(self, dal): 
        self.dal = dal
    
    def getCountryID(self, nation):
        cursor = self.dal.get_cursor()
        query = "SELECT getCountryID(%s)"
        try: 
            cursor.execute(query, [nation])
            result = cursor.fetchone()
            print("ID retrieved Sucessfully")
            return result[0]
        except Exception as e: 
            print(f"Error fetching country ID: {e}")
        finally: 
            cursor.close()

    


class Contracts:

    def __init__(self, dal): 
        self.dal = dal

    def getContractID(self, playerName): 
        cursor = self.dal.get_cursor()
        query = "SELECT getContractID(%s)"
        try:
            cursor.execute(query, [playerName]) 
            result = cursor.fetchone()
            print("'Contract ID reterieved sucessfully") 
            return result[0]
        except Exception as e: 
            print(f"Error fetching contract ID: {e}")
        finally: 
            cursor.close()
    
    def addContract(self, playerName, newAAV, newLength, newSign):
        query = "CALL addContract(%s, %s, %s, %s)"
        cursor = self.dal.get_cursor()
        try:
            cursor.execute(query, [playerName, newAAV, newLength, newSign])
            result = cursor.fetchall()
            if ('No Such Player Exists in our Database',) in result: 
                print("Contract NOT ADDED: No Such Player Exists in our Database ") 
            else:
              self.dal.commit()
              return result
        except Exception as e:
            print(f"Unknown error: {e}")
        finally:
            cursor.close()

