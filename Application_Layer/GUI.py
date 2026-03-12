from tkinter import *
from tkinter import ttk
from BLL import BLL

class NHL_App: 
    def __init__(self):
        self.bll = BLL()
        self.online = False
    
        

    
NHLDB = NHL_App()

def main():
    #Login will precede main view 
    def login():
        user = username_entry.get()
        password = pass_entry.get()
        database = db_entry.get()
        NHLDB.bll.login(user, password, database)
        try:
       
            connected = NHLDB.bll.dal._get_connection()

            if connected:
                print('Login Successful')
                login_frame.grid_forget()
                build_main_screen()
        except Exception as e: 
            print(f"Error Logging In: {e}")
        

    def build_main_screen():
        #View Roster satisfies 1/2 Views able to access requirement
        def view_roster():
            def roster_view():
                
                teamName = roster_entry.get()
                teamtoView = NHLDB.bll.getTeamRoster(teamName)
                text_output = Text(roster_frame, width=100, height=100, font=('Franklin Gothic Book', 12))
                text_output.grid(row=5, column=0)
                text_output.insert(END, teamtoView)

            def back_button(): 
                roster_frame.grid_forget()
                main_frame.grid(row=0, column=0, padx=10, pady=10)


            main_frame.grid_forget()
            roster_frame = Frame(window)
            roster_frame.grid(row=0, column=0, padx=10, pady=10) 
            roster_type = Label(roster_frame, text="Enter a team you would like to view", font=('Franklin Gothic Book', 20))
            roster_type.grid(row=0, column=0, sticky='w', padx=10, pady=(10, 5))
            roster_entry = Entry(roster_frame, font=('Ink Free', 20), bg='#111111', fg='#00FF00', width=30)
            # roster_entry.insert(0, 'Boston Bruins')
            roster_entry.grid(row=2, column=0, sticky='w', padx=10)
            confirm_button = Button(roster_frame, text='Confirm', command=roster_view)
            confirm_button.grid(row=3, column=0, sticky='w', padx=10, pady=10)
            back = Button(roster_frame, text='Back', command=back_button)
            back.grid(row=4, column=0, sticky='w', padx=5, pady=5)
        #Find Player satisfies add to existing row requirement
        def find_player():


            def fetch_player(): 
                def newplayer(): 
                    newplayer = NHLDB.bll.newPlayer(playerName, playerPosition, playerTeam, playerNation)
                    if newplayer:
                        return newplayer
                    else: 
                        return 'ERROR'

                playerName = player_entry.get()
                playerPosition = position_entry.get()
                playerTeam = team_entry.get()
                playerNation = nation_entry.get()
                
                

    

                text_output = Text(player_frame, width=50, height=20, font=('Franklin Gothic Book', 12))
                text_output.grid(row=11, column=0)
                text_output.insert(END, newplayer())
                
            def back_button(): 
                player_frame.grid_forget()
                main_frame.grid(row=0, column=0, padx=10, pady=10)

            main_frame.grid_forget()
            player_frame = Frame(window)
            player_frame.grid(row=0,column=0, padx=10, pady=10)


            player_label = Label(player_frame, text="Player Name", font=('Franklin Gothic Book', 15))
            player_label.grid(row=1, column=0, sticky='w', padx=10, pady=(0, 20))

            player_entry = Entry(player_frame, font=('Ink Free', 20), bg='#111111', fg='#00FF00', width=30)
            #player_entry.insert(0, 'Connor McDavid')
            player_entry.grid(row=2, column=0, sticky='w', padx=10)

            position_label = Label(player_frame, text="Player Position", font=('Franklin Gothic Book', 15))
            position_label.grid(row=3, column=0, sticky='w', padx=10, pady=(0, 20))

            position_entry = Entry(player_frame, font=('Ink Free', 20), bg='#111111', fg='#00FF00', width=30)
            #position_entry.insert(0, 'C')
            position_entry.grid(row=4, column=0, sticky='w', padx=10)

            team_label = Label(player_frame, text="NHL Team", font=('Franklin Gothic Book', 15))
            team_label.grid(row=5, column=0, sticky='w', padx=10, pady=(0, 20))

            team_entry = Entry(player_frame, font=('Ink Free', 20), bg='#111111', fg='#00FF00', width=30)
            #team_entry.insert(0, 'Edmonton Oilers')
            team_entry.grid(row=6, column=0, sticky='w', padx=10)

            nation_label = Label(player_frame, text="Country of Origin", font=('Franklin Gothic Book', 15))
            nation_label.grid(row=7, column=0, sticky='w', padx=10, pady=(0, 20))

            nation_entry = Entry(player_frame, font=('Ink Free', 20), bg='#111111', fg='#00FF00', width=30)
            #nation_entry.insert(0, 'Canada')
            nation_entry.grid(row=8, column=0, sticky='w', padx=10)


            

            confirm_button = Button(player_frame, text='Confirm', command=fetch_player)
            confirm_button.grid(row=9, column=0, sticky='w', padx=10, pady=10)

            back = Button(player_frame, text='Back', command=back_button)
            back.grid(row=10, column=0, sticky='w', padx=5, pady=5)
        #Player Guesser satisfies advanced feature requirement
        def play_guesser():
            def redraw(): 
                redraw_player = NHLDB.bll.dal.players.viewPlayer()
                game(redraw_player)
            def back_button(): 
                guesser_frame.grid_forget()
                main_frame.grid(row=0, column=0, padx=10, pady=10)
            player_picked = NHLDB.bll.dal.players.viewPlayer()
            

            def game(player_picked):
                thinking = Label(guesser_frame, text='I’m thinking of a player...', font=('Franklin Gothic Book', 20))
                thinking.grid(row=0, column=0, pady=10)
                player_info =Label(guesser_frame, text=f'He is a {player_picked[0][1]} that currently plays for the {player_picked[0][2]} from {player_picked[0][3]}', font=('Franklin Gothic Book', 20))
                player_info.grid(row=1, column=0, padx=10, pady=10)

                guess = Entry(guesser_frame, font=('Ink Free', 20), bg='#111111', fg='#00FF00', width=30)
                guess.grid(row=2, column=0, padx=10, pady=10)

                text_output = Text(guesser_frame, width=50, height=2, font=('Franklin Gothic Book', 12))
                text_output.grid(row=4, column=0, pady=10)

                def official_guess():
                    text_output.insert(END, f'Your Guess: {guess.get()}\nCorrect Player: {player_picked[0][0]}')

                Button(guesser_frame, text='Submit Guess', command=official_guess, font=('Franklin Gothic Book', 16)).grid(row=3, column=0, pady=10)

                Button(guesser_frame, text='Redraw', command=redraw, font=('Franklin Gothic Book', 16)).grid(row=3, column=1, pady=10)
                Button(guesser_frame, text='Back', command=back_button, font=('Franklin Gothic Book', 16)).grid(row=4, column=1, pady=10)
            
            main_frame.grid_forget()
            guesser_frame = Frame(window)
            guesser_frame.grid(row=0, column=0)

            game(player_picked)

        #Team USA sastifies 2/2 Views able to acces requirement
        def teamUSA(): 

            def back_button(): 
                USA_frame.grid_forget()
                main_frame.grid(row=0, column=0, padx=10, pady=10)

            USA = NHLDB.bll.teamUSA()

            main_frame.grid_forget()
            USA_frame = Frame(window)
            USA_frame.grid(row=0, column=0)

            text_output = Text(USA_frame, width=100, height=20, font=('Franklin Gothic Book', 12))
            text_output.grid(row=1, column=0)
            text_output.insert(END, (USA))

            move_back = Button(USA_frame, text="Back", font=('Franklin Gothic Book', 15), command=back_button)
            move_back.grid(row=2, column=1, sticky='w', padx=10, pady=10)

            
        #Roster mover satisfies update existing row requirement
        def roster_mover(): 

            def back_button(): 
                mover_frame.grid_forget()
                main_frame.grid(row=0, column=0, padx=10, pady=10)

            def newroster():
                player = oldplayer_entry.get()
                newteam = newteam_entry.get()
                result = NHLDB.bll.rosterMove(player, newteam)
                text_output = Text(mover_frame, width=50, height=20, font=('Franklin Gothic Book', 12))
                text_output.grid(row=6, column=0)
                text_output.insert(END, result)

                move_back = Button(mover_frame, text="Back", font=('Franklin Gothic Book', 15), command=back_button)
                move_back.grid(row=7, column=1, sticky='w', padx=10, pady=10)

            main_frame.grid_forget()
            mover_frame = Frame(window)
            mover_frame.grid(row=0, column=0)

            oldplayer_label = Label(mover_frame, text="Enter a Player Name", font=('Franklin Gothic Book', 15))
            oldplayer_label.grid(row=1, column=0, sticky='w', padx=10, pady=(0, 20))

            oldplayer_entry = Entry(mover_frame, font=('Ink Free', 20), bg='#111111', fg='#00FF00', width=30)
            oldplayer_entry.insert(0, 'root')
            oldplayer_entry.grid(row=2, column=0, sticky='w', padx=10)

            oldteam_label = Label(mover_frame, text="Enter Player's Previous Team", font=('Franklin Gothic Book', 15))
            oldteam_label.grid(row=3, column=0, sticky='w', padx=10, pady=(0, 20))

            oldteam_entry = Entry(mover_frame, font=('Ink Free', 20), bg='#111111', fg='#00FF00', width=30)
            oldteam_entry.insert(0, 'root')
            oldteam_entry.grid(row=4, column=0, sticky='w', padx=10)

            newteam_label = Label(mover_frame, text="Enter Player's New Team", font=('Franklin Gothic Book', 15))
            newteam_label.grid(row=5, column=0, sticky='w', padx=10, pady=(0, 20))

            newteam_entry = Entry(mover_frame, font=('Ink Free', 20), bg='#111111', fg='#00FF00', width=30)
            newteam_entry.insert(0, 'root')
            newteam_entry.grid(row=6, column=0, sticky='w', padx=10)

            move_submit = Button(mover_frame, text="Submit", font=('Franklin Gothic Book', 15), command=newroster)
            move_submit.grid(row=7, column=0, sticky='w', padx=10, pady=10)
        #Delete Player updates delete existing row requirement
        def delete_player():
            def back_button(): 
                deleter_frame.grid_forget()
                main_frame.grid(row=0, column=0, padx=10, pady=10)

            def delete():
                playertoDelete = deleter_entry.get()
                player_deleted = NHLDB.bll.deletePlayer(playertoDelete)
                text_output = Text(deleter_frame, width=50, height=20, font=('Franklin Gothic Book', 12))
                text_output.grid(row=8, column=0)
                text_output.insert(END, player_deleted)

                move_back = Button(deleter_frame, text="Back", font=('Franklin Gothic Book', 15), command=back_button)
                move_back.grid(row=7, column=1, sticky='w', padx=10, pady=10)

            main_frame.grid_forget()
            deleter_frame = Frame(window)
            deleter_frame.grid(row=0, column=0)

            deleter_label = Label(deleter_frame, text="Enter a Player Name to delete", font=('Franklin Gothic Book', 15))
            deleter_label.grid(row=1, column=0, sticky='w', padx=10, pady=(0, 20))

            deleter_entry = Entry(deleter_frame, font=('Ink Free', 20), bg='#111111', fg='#00FF00', width=30)
            deleter_entry.insert(0, 'root')
            deleter_entry.grid(row=2, column=0, sticky='w', padx=10)

            move_submit = Button(deleter_frame, text="Submit", font=('Franklin Gothic Book', 15), command=delete)
            move_submit.grid(row=7, column=0, sticky='w', padx=10, pady=10)
        #Additional View satisfied
        def playerprofile(): 

            def back_button(): 
                playerList_frame.grid_forget()
                main_frame.grid(row=0, column=0, padx=10, pady=10)

            player_list = NHLDB.bll.playerProfile()

            main_frame.grid_forget()
            playerList_frame = Frame(window)
            playerList_frame.grid(row=0, column=0)

            text_output = Text(playerList_frame, width=200, height=20, font=('Franklin Gothic Book', 12))
            text_output.grid(row=1, column=0)
            text_output.insert(END, (player_list))

            move_back = Button(playerList_frame, text="Back", font=('Franklin Gothic Book', 15), command=back_button)
            move_back.grid(row=2, column=0, sticky='w', padx=10, pady=10)



        




        main_frame = Frame(window)
        main_frame.grid(row=0, column=0, padx=10, pady=10)

        greeting_label = Label(main_frame, text="NHL Player Databse", font=('Franklin Gothic Book', 20))
        greeting_label.grid(row=0, column=0, sticky='w', padx=10, pady=(10, 5))
        
        roster_button = Button(main_frame, text="View Roster", font=('Franklin Gothic Book', 15), command=view_roster)
        roster_button.grid(row=1, column=0, sticky='w', padx=10, pady=10)

        player_button = Button(main_frame, text="Add a Player", font=('Franklin Gothic Book', 15), command=find_player)
        player_button.grid(row=2, column=0, sticky='w', padx=10, pady=10)

        guesser_button = Button(main_frame, text="Play Player Guesser", font=('Franklin Gothic Book', 15), command=play_guesser)
        guesser_button.grid(row=3, column=0, sticky='w', padx=10, pady=10)

        USA_button = Button(main_frame, text="View Team USA", font=('Franklin Gothic Book', 15), command=teamUSA)
        USA_button.grid(row=4, column=0, sticky='w', padx=10, pady=10)

        Update_Roster = Button(main_frame, text="Move Player", font=('Franklin Gothic Book', 15), command=roster_mover)
        Update_Roster.grid(row=5, column=0, sticky='w', padx=10, pady=10)

        Update_Roster = Button(main_frame, text="Delete Player", font=('Franklin Gothic Book', 15), command=delete_player)
        Update_Roster.grid(row=6, column=0, sticky='w', padx=10, pady=10)

        PlayerProfile = Button(main_frame, text="View Player Info", font=('Franklin Gothic Book', 15), command=playerprofile)
        PlayerProfile.grid(row=7, column=0, sticky='w', padx=10, pady=10)


        


    window = Tk()
    window.title("NHL Database App")

    login_frame = Frame(window)
    login_frame.grid(row=0, column=0, padx=10, pady=10)

    welcome = Label(login_frame, text="Welcome to the MRC User App!", font=('Franklin Gothic Book', 20))
    welcome.grid(row=0, column=0, sticky='w', padx=10, pady=(10, 5))

    username_label = Label(login_frame, text="Enter your database username", font=('Franklin Gothic Book', 15))
    username_label.grid(row=1, column=0, sticky='w', padx=10, pady=(0, 20))

    username_entry = Entry(login_frame, font=('Ink Free', 20), bg='#111111', fg='#00FF00', width=30)
     # username_entry.insert(0, 'root')
    username_entry.grid(row=2, column=0, sticky='w', padx=10)

    pass_label = Label(login_frame, text="Enter your database password", font=('Franklin Gothic Book', 15))
    pass_label.grid(row=3, column=0, sticky='w', padx=10, pady=(0, 20))

    pass_entry = Entry(login_frame, font=('Ink Free', 20), bg='#111111', fg='#00FF00', width=30, show='*')
     # pass_entry.insert(0, 'Z7Lyq7qn#x4QRgMUR^Xm')
    pass_entry.grid(row=4, column=0, sticky='w', padx=10)

    db_label = Label(login_frame, text="Enter your database name", font=('Franklin Gothic Book', 15))
    db_label.grid(row=5, column=0, sticky='w', padx=10, pady=(0, 20))

    db_entry = Entry(login_frame, font=('Ink Free', 20), bg='#111111', fg='#00FF00', width=30)
     # db_entry.insert(0, 'nhl_top_100')
    db_entry.grid(row=6, column=0, sticky='w', padx=10)

    login_button = Button(login_frame, text="Login", font=('Franklin Gothic Book', 15), command=login)
    login_button.grid(row=12, column=0, sticky='w', padx=10, pady=20)

    window.mainloop()

main()
