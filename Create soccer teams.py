# Name project [Create soccer teams]

import tkinter as tk
import random

class FootballTeamApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Football with boys")

        window_width = 700
        window_height = 300
        x_position = (root.winfo_screenwidth() - window_width) // 2
        y_position = (root.winfo_screenheight() - window_height) // 2
        root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        self.team1_frame = tk.Frame(root)
        self.team1_frame.pack(side=tk.LEFT, padx=10)

        self.team2_frame = tk.Frame(root)
        self.team2_frame.pack(side=tk.LEFT, padx=10)

        self.team3_frame = tk.Frame(root)
        self.team3_frame.pack(side=tk.LEFT, padx=10)

        self.team1_label = tk.Label(self.team1_frame, text="Team 1")
        self.team1_label.pack()

        self.team2_label = tk.Label(self.team2_frame, text="Team 2")
        self.team2_label.pack()

        self.team3_label = tk.Label(self.team3_frame, text="Team 3")
        self.team3_label.pack()

        self.team1_listbox = tk.Listbox(self.team1_frame, selectmode=tk.MULTIPLE)
        self.team1_listbox.pack()

        self.team2_listbox = tk.Listbox(self.team2_frame, selectmode=tk.MULTIPLE)
        self.team2_listbox.pack()

        self.team3_listbox = tk.Listbox(self.team3_frame, selectmode=tk.MULTIPLE)
        self.team3_listbox.pack()

        self.player_entry_label = tk.Label(root, text="Enter Player Name:")
        self.player_entry_label.pack()

        self.player_entry = tk.Entry(root)
        self.player_entry.pack()

        self.level_buttons_frame = tk.Frame(root)
        self.level_buttons_frame.pack()

        levels = ["ncepator", "mediu", "avansat", "expert"]
        self.level_buttons = []
        for level in levels:
            button = tk.Button(self.level_buttons_frame, text=level, command=lambda l=level: self.set_player_level(l))
            button.pack(side=tk.LEFT)
            self.level_buttons.append(button)

        self.add_player_button = tk.Button(root, text="Add Player", command=self.add_player)
        self.add_player_button.pack()

        self.remove_player_button = tk.Button(root, text="Remove Player", command=self.remove_player)
        self.remove_player_button.pack()

        self.display_teams_button = tk.Button(root, text="Display Teams", command=self.display_teams)
        self.display_teams_button.pack()

        self.generate_teams_button = tk.Button(root, text="Generate Teams", command=self.generate_teams)
        self.generate_teams_button.pack()

        self.players = []
        self.teams_generated = False

    def set_player_level(self, level):
        self.selected_level = level

    def add_player(self):
        player_name = self.player_entry.get()
        if player_name and hasattr(self, 'selected_level'):
            player_info = f"{player_name} (Level: {self.selected_level})"
            self.players.append((player_info, self.selected_level))
            self.team1_listbox.insert(tk.END, player_info)
            self.team2_listbox.insert(tk.END, player_info)
            self.team3_listbox.insert(tk.END, player_info)
            self.player_entry.delete(0, tk.END)

    def remove_player(self):
        selected_players = self.team1_listbox.curselection() + self.team2_listbox.curselection() + self.team3_listbox.curselection()
        selected_players = sorted(selected_players, reverse=True)

        for index in selected_players:
            self.team1_listbox.delete(index)
            self.team2_listbox.delete(index)
            self.team3_listbox.delete(index)
            del self.players[index]

    def calculate_total_level(self, team_players):
        return sum(1 if level == 'ncepator' else 2 if level == 'mediu' else 3 if level == 'avansat' else 4 for _, level in team_players)

    def display_teams(self):
        team1_players = self.team1_listbox.get(0, tk.END)
        team2_players = self.team2_listbox.get(0, tk.END)
        team3_players = self.team3_listbox.get(0, tk.END)

        team1_str = ", ".join(team1_players)
        team2_str = ", ".join(team2_players)
        team3_str = ", ".join(team3_players)

        result_text = f"Team 1: {team1_str}\nTeam 2: {team2_str}\nTeam 3: {team3_str}"

        result_label = tk.Label(self.root, text=result_text)
        result_label.pack()

    def generate_teams(self):
        if not self.teams_generated and len(self.players) >= 15: # Entering the number of players
            random.shuffle(self.players)


            teams = [self.players[i:i + 5] for i in range(0, len(self.players), 5)] # Dividing the players into teams of 5

            # Team sorting based on total strength
            teams.sort(key=lambda team: sum(1 if level == 'ncepator' else 2 if level == 'mediu' else 3 if level == 'avansat' else 4 for _, level in team))

            self.team1_listbox.delete(0, tk.END)
            self.team2_listbox.delete(0, tk.END)
            self.team3_listbox.delete(0, tk.END)

            # Adding players to teams
            for index, team_players in enumerate(teams, start=1):
                for player_info, _ in team_players:
                    if index == 1:
                        self.team1_listbox.insert(tk.END, player_info)
                    elif index == 2:
                        self.team2_listbox.insert(tk.END, player_info)
                    elif index == 3:
                        self.team3_listbox.insert(tk.END, player_info)

            self.teams_generated = True

        elif self.teams_generated:
            error_label = tk.Label(self.root, text="Teams already generated.")
            error_label.pack()

        else:
            error_label = tk.Label(self.root, text="Not enough players. Keep adding players.")
            error_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = FootballTeamApp(root)
    root.mainloop()
