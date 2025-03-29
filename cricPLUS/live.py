# # from tkinter import *
# #
# # from main import w
# #
# #
# # class live:
# #     w = Tk()
# #     w.config(bg="light blue")
# #     w.geometry("1000x800")
# #
# #     Label(w, text='Live ScoreCard', font=("Arial", 30), background='light blue', foreground='orange', bd=2,
# #           relief="solid").pack(pady=30)
# #
# #     s = 'shryes'
# #     n_s = 'rohit'
# #
# #     batter_name1 = Label(w,text='Batter Name: ', font=("Arial", 18),background='light blue', foreground='brown',width=10,height=2).place(x=50,y=200)
# #     Label(w,text=f"     {s}        runs: 0      4/6: 0/0      SR: 0", font=("Arial", 18),background='light blue', foreground='black',width=35,height=2).place(x=220, y=200)
# #     batter_name2 = Label(w, text='Batter Name: ', font=("Arial", 18), background='light blue', foreground='brown',width=10, height=2).place(x=50, y=240)
# #     Label(w,text=f"       {n_s}          runs: 0      4/6: 0/0      SR: 0", font=("Arial", 18),background='light blue', foreground='black',width=35,height=2).place(x=220, y=240)
# #
# #
# #     def batter_1(self):
# #         dot_b = Button(w, text='Dot', bg='grey', height=1, width=3, font=("Arial", 18)).place(x=50, y=650)
# #         one_b = Button(w, text='1', bg='grey', height=1, width=3, font=("Arial", 18)).place(x=110, y=650)
# #         two_b = Button(w, text='2', bg='grey', height=1, width=3, font=("Arial", 18)).place(x=170, y=650)
# #         three_b = Button(w, text='3', bg='grey', height=1, width=3, font=("Arial", 18)).place(x=230, y=650)
# #         four_b = Button(w, text='4', bg='green', height=1, width=3, font=("Arial", 18)).place(x=290, y=650)
# #         five_b = Button(w, text='5', bg='grey', height=1, width=3, font=("Arial", 18)).place(x=350, y=650)
# #         six_b = Button(w, text='6', bg='green', height=1, width=3, font=("Arial", 18)).place(x=410, y=650)
# #         seven_b = Button(w, text='7', bg='grey', height=1, width=3, font=("Arial", 18)).place(x=470, y=650)
# #         wicket_b = Button(w, text='Out', bg='red', height=1, width=7, font=("Arial", 18)).place(x=550, y=650)
# #         wide_b = Button(w, text='Wide', bg='grey', height=1, width=7, font=("Arial", 18)).place(x=670, y=650)
# #         no_ball_b = Button(w, text='No Ball', bg='grey', height=1, width=7, font=("Arial", 18)).place(x=790, y=650)
# #
# #
# #     def __init__(self):
# #         pass
# #
# #     w.mainloop()
#
#
# import tkinter as tk
# from tkinter import ttk, messagebox, scrolledtext
#
# # ==== Data Classes for Batter and Bowler ====
#
# class Batter:
#     def __init__(self, name):
#         self.name = name
#         self.runs = 0
#         self.balls = 0
#         self.fours = 0
#         self.sixes = 0
#
#     @property
#     def strike_rate(self):
#         return round((self.runs / self.balls * 100) if self.balls > 0 else 0, 2)
#
# class Bowler:
#     def __init__(self, name):
#         self.name = name
#         self.overs = 0  # Complete overs bowled
#         self.balls_in_current_over = 0  # 0 to 5
#         self.runs_conceded = 0
#         self.wickets = 0
#
#     def add_ball(self):
#         self.balls_in_current_over += 1
#         if self.balls_in_current_over == 6:
#             self.overs += 1
#             self.balls_in_current_over = 0
#
#     def add_run(self, runs):
#         self.runs_conceded += runs
#
#     def add_wicket(self):
#         self.wickets += 1
#
#     @property
#     def overs_display(self):
#         return f"{self.overs}.{self.balls_in_current_over}"
#
# # ==== Main Application Class ====
#
# class CricketScoringApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Advanced Cricket Scoring App")
#         self.geometry("2000x2000")
#         self.resizable(False, False)
#
#         # Use a ttk theme for a modern look.
#         self.style = ttk.Style(self)
#         self.style.theme_use("clam")  # try 'clam', 'alt', 'default', or 'vista'
#
#         # Create a container frame for switching screens
#         self.container = ttk.Frame(self)
#         self.container.pack(side="top", fill="both", expand=True)
#
#         # Data for match state (to be filled from setup)
#         self.match_data = {}
#
#         # Dictionary to hold different frames
#         self.frames = {}
#         for F in (SetupFrame, ScoreFrame):
#             frame = F(parent=self.container, controller=self)
#             self.frames[F.__name__] = frame
#             frame.grid(row=0, column=0, sticky="nsew")
#
#         self.show_frame("SetupFrame")
#
#     def show_frame(self, frame_name):
#         frame = self.frames[frame_name]
#         frame.tkraise()
#
# # ==== Setup Screen ====
#
# class SetupFrame(ttk.Frame):
#     def __init__(self, parent, controller: CricketScoringApp):
#         super().__init__(parent)
#         self.controller = controller
#
#         # Title
#         title = ttk.Label(self, text="Cricket Match Setup", font=("Helvetica", 22, "bold"))
#         title.grid(row=0, column=0, columnspan=2, pady=20)
#
#         # Batting Team
#         batting_frame = ttk.LabelFrame(self, text="Batting Team", padding=10)
#         batting_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
#
#         ttk.Label(batting_frame, text="Team Name:", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", pady=5)
#         self.batting_team_entry = ttk.Entry(batting_frame, width=30, font=("Helvetica", 12))
#         self.batting_team_entry.grid(row=0, column=1, padx=10, pady=5)
#
#         ttk.Label(batting_frame, text="Batter Names (comma separated, 11 players):", font=("Helvetica", 12)).grid(
#             row=1, column=0, sticky="w", pady=5)
#         self.batter_names_entry = ttk.Entry(batting_frame, width=50, font=("Helvetica", 12))
#         self.batter_names_entry.grid(row=1, column=1, padx=10, pady=5)
#
#         # Bowling Team
#         bowling_frame = ttk.LabelFrame(self, text="Bowling Team", padding=10)
#         bowling_frame.grid(row=1, column=1, padx=20, pady=10, sticky="ew")
#
#         ttk.Label(bowling_frame, text="Team Name:", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", pady=5)
#         self.bowling_team_entry = ttk.Entry(bowling_frame, width=30, font=("Helvetica", 12))
#         self.bowling_team_entry.grid(row=0, column=1, padx=10, pady=5)
#
#         ttk.Label(bowling_frame, text="Bowler Names (comma separated, at least 5):", font=("Helvetica", 12)).grid(
#             row=1, column=0, sticky="w", pady=5)
#         self.bowler_names_entry = ttk.Entry(bowling_frame, width=50, font=("Helvetica", 12))
#         self.bowler_names_entry.grid(row=1, column=1, padx=10, pady=5)
#
#         # Start Button
#         start_button = ttk.Button(self, text="Start Match", command=self.start_match, style="Accent.TButton")
#         start_button.grid(row=2, column=0, columnspan=2, pady=20)
#
#     def start_match(self):
#         # Get and validate inputs
#         batting_team = self.batting_team_entry.get().strip()
#         batters = [name.strip() for name in self.batter_names_entry.get().split(",") if name.strip()]
#         bowling_team = self.bowling_team_entry.get().strip()
#         bowlers = [name.strip() for name in self.bowler_names_entry.get().split(",") if name.strip()]
#
#         if not batting_team or len(batters) != 11:
#             messagebox.showerror("Input Error", "Please provide a batting team name and exactly 11 batter names.")
#             return
#         if not bowling_team or len(bowlers) < 5:
#             messagebox.showerror("Input Error", "Please provide a bowling team name and at least 5 bowler names.")
#             return
#
#         # Save match data into the controller's match_data dictionary
#         self.controller.match_data["batting_team"] = batting_team
#         self.controller.match_data["bowling_team"] = bowling_team
#         self.controller.match_data["batters_queue"] = [Batter(name) for name in batters]
#         self.controller.match_data["bowlers"] = [Bowler(name) for name in bowlers]
#         self.controller.match_data["total_runs"] = 0
#         self.controller.match_data["total_wickets"] = 0
#         self.controller.match_data["total_overs"] = 0
#         self.controller.match_data["balls_in_over"] = 0
#         self.controller.match_data["ball_commentary"] = []
#
#         # Openers: first two batters are on the field
#         batters_queue = self.controller.match_data["batters_queue"]
#         self.controller.match_data["current_batsmen"] = [batters_queue.pop(0), batters_queue.pop(0)]
#         self.controller.match_data["next_batters"] = batters_queue
#
#         # Set the first bowler as current
#         self.controller.match_data["current_bowler_index"] = 0
#         self.controller.match_data["current_bowler"] = self.controller.match_data["bowlers"][0]
#
#         # Initialize Score Screen display
#         score_frame = self.controller.frames["ScoreFrame"]
#         score_frame.initialize_display()
#         self.controller.show_frame("ScoreFrame")
#
# # ==== Scoring Screen ====
#
# class ScoreFrame(ttk.Frame):
#     def __init__(self, parent, controller: CricketScoringApp):
#         super().__init__(parent)
#         self.controller = controller
#
#         # Top Frame: Overall Score and Overs
#         top_frame = ttk.Frame(self)
#         top_frame.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")
#         top_frame.columnconfigure(0, weight=1)
#         top_frame.columnconfigure(1, weight=1)
#
#         self.score_label = ttk.Label(top_frame, text="Score: 0/0", font=("Helvetica", 20, "bold"))
#         self.score_label.grid(row=0, column=0, sticky="w", padx=20)
#
#         self.overs_label = ttk.Label(top_frame, text="Overs: 0.0", font=("Helvetica", 20, "bold"))
#         self.overs_label.grid(row=0, column=1, sticky="e", padx=20)
#
#         # Middle Frame: Player Stats
#         middle_frame = ttk.Frame(self)
#         middle_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
#         middle_frame.columnconfigure(0, weight=1)
#         middle_frame.columnconfigure(1, weight=1)
#
#         # Batter stats frame
#         self.batsmen_frame = ttk.LabelFrame(middle_frame, text="Batting", padding=10)
#         self.batsmen_frame.grid(row=0, column=0, sticky="nsew", padx=10)
#
#         self.batsman1_label = ttk.Label(self.batsmen_frame, text="", font=("Helvetica", 12))
#         self.batsman1_label.grid(row=0, column=0, sticky="w", pady=5)
#         self.batsman2_label = ttk.Label(self.batsmen_frame, text="", font=("Helvetica", 12))
#         self.batsman2_label.grid(row=1, column=0, sticky="w", pady=5)
#
#         # Bowler stats frame
#         self.bowler_frame = ttk.LabelFrame(middle_frame, text="Bowling", padding=10)
#         self.bowler_frame.grid(row=0, column=1, sticky="nsew", padx=10)
#         self.bowler_info_label = ttk.Label(self.bowler_frame, text="", font=("Helvetica", 12))
#         self.bowler_info_label.grid(row=0, column=0, sticky="w", pady=5)
#
#         # Commentary Frame: Ball-by-Ball Log (scrollable)
#         commentary_frame = ttk.LabelFrame(self, text="Ball-by-Ball Commentary", padding=10)
#         commentary_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")
#         commentary_frame.rowconfigure(0, weight=1)
#         commentary_frame.columnconfigure(0, weight=1)
#
#         self.commentary_box = scrolledtext.ScrolledText(commentary_frame, wrap=tk.WORD, height=12, font=("Helvetica", 11))
#         self.commentary_box.grid(row=0, column=0, sticky="nsew")
#         self.commentary_box.config(state="disabled")
#
#         # Bottom Frame: Scoring Controls
#         control_frame = ttk.Frame(self)
#         control_frame.grid(row=3, column=0, columnspan=2, pady=15)
#
#         # Create scoring buttons for runs
#         for run in [0, 1, 2, 3, 4, 6]:
#             btn = ttk.Button(control_frame, text=str(run), command=lambda r=run: self.record_ball(run=r), width=4)
#             btn.pack(side="left", padx=5)
#
#         # Extras: Wide and No Ball
#         btn_wide = ttk.Button(control_frame, text="Wide", command=lambda: self.record_ball(extra="Wide"), width=6)
#         btn_wide.pack(side="left", padx=5)
#         btn_no_ball = ttk.Button(control_frame, text="No Ball", command=lambda: self.record_ball(extra="No Ball"), width=8)
#         btn_no_ball.pack(side="left", padx=5)
#
#         # Wicket button
#         btn_wicket = ttk.Button(control_frame, text="Wicket", command=self.record_wicket, width=8)
#         btn_wicket.pack(side="left", padx=5)
#
#         # Change bowler button
#         btn_change_bowler = ttk.Button(control_frame, text="Change Bowler", command=self.change_bowler, width=12)
#         btn_change_bowler.pack(side="left", padx=5)
#
#     def initialize_display(self):
#         """Reset display values from the match data."""
#         data = self.controller.match_data
#         data["total_runs"] = 0
#         data["total_wickets"] = 0
#         data["total_overs"] = 0
#         data["balls_in_over"] = 0
#         data["ball_commentary"].clear()
#         self.commentary_box.config(state="normal")
#         self.commentary_box.delete("1.0", tk.END)
#         self.commentary_box.config(state="disabled")
#         self.update_scoreboard()
#         self.update_player_info()
#
#     def update_scoreboard(self):
#         data = self.controller.match_data
#         runs = data["total_runs"]
#         wickets = data["total_wickets"]
#         # Display overs as whole overs and balls in current over (e.g., 3.2 means 3 overs and 2 balls)
#         overs_str = f"{data['total_overs']}.{data['balls_in_over']}"
#         self.score_label.config(text=f"Score: {runs}/{wickets}")
#         self.overs_label.config(text=f"Overs: {overs_str}")
#
#     def update_player_info(self):
#         data = self.controller.match_data
#         batsmen = data["current_batsmen"]
#         if batsmen:
#             b1 = batsmen[0]
#             b2 = batsmen[1]
#             self.batsman1_label.config(text=f"{b1.name}: {b1.runs} ({b1.balls}) | 4s: {b1.fours} 6s: {b1.sixes} | SR: {b1.strike_rate}")
#             self.batsman2_label.config(text=f"{b2.name}: {b2.runs} ({b2.balls}) | 4s: {b2.fours} 6s: {b2.sixes} | SR: {b2.strike_rate}")
#
#         bowler = data["current_bowler"]
#         self.bowler_info_label.config(text=(f"{bowler.name}\nOvers: {bowler.overs_display}\nRuns: {bowler.runs_conceded}\nWickets: {bowler.wickets}"))
#
#     def append_commentary(self, text):
#         """Append text to the commentary log."""
#         self.controller.match_data["ball_commentary"].append(text)
#         self.commentary_box.config(state="normal")
#         self.commentary_box.insert(tk.END, text + "\n")
#         self.commentary_box.see(tk.END)
#         self.commentary_box.config(state="disabled")
#
#     def record_ball(self, run=0, extra=None):
#         data = self.controller.match_data
#         # Handle extras (they add runs but not a legal ball)
#         if extra:
#             extra_run = 1  # common extra run
#             data["total_runs"] += extra_run
#             data["current_bowler"].add_run(extra_run)
#             self.append_commentary(f"{extra}: +{extra_run} run")
#             self.update_scoreboard()
#             self.update_player_info()
#             return
#
#         # Legal delivery processing
#         striker = data["current_batsmen"][0]
#         bowler = data["current_bowler"]
#
#         # Update batsman stats
#         striker.runs += run
#         striker.balls += 1
#         if run == 4:
#             striker.fours += 1
#         if run == 6:
#             striker.sixes += 1
#
#         # Update bowler stats
#         bowler.add_run(run)
#         bowler.add_ball()
#
#         # Update overall match stats
#         data["total_runs"] += run
#         data["balls_in_over"] += 1
#
#         # Append commentary: ball number (e.g., "2.3") and event details.
#         ball_no = f"{data['total_overs']}.{data['balls_in_over']}"
#         self.append_commentary(f"Ball {ball_no}: {striker.name} scores {run} run(s)")
#
#         # Swap strike on odd runs
#         if run % 2 == 1:
#             self.swap_strike()
#
#         # Check for over completion (6 legal deliveries)
#         if data["balls_in_over"] == 6:
#             data["total_overs"] += 1
#             data["balls_in_over"] = 0
#             self.swap_strike()  # End of over swap
#             self.append_commentary("----- End of Over -----")
#
#         self.update_scoreboard()
#         self.update_player_info()
#
#     def record_wicket(self):
#         data = self.controller.match_data
#         striker = data["current_batsmen"][0]
#         bowler = data["current_bowler"]
#         # Increment wicket count and update bowler stats
#         data["total_wickets"] += 1
#         bowler.add_wicket()
#         striker.balls += 1  # count the ball faced
#         ball_no = f"{data['total_overs']}.{data['balls_in_over'] + 1}"
#         self.append_commentary(f"Ball {ball_no}: {striker.name} is OUT!")
#         # Replace striker with the next batter (if available)
#         if data["next_batters"]:
#             new_batter = data["next_batters"].pop(0)
#             data["current_batsmen"][0] = new_batter
#         else:
#             messagebox.showinfo("Innings Ended", "All batters are out!")
#             return
#
#         # Consider wicket ball as legal delivery
#         data["balls_in_over"] += 1
#         bowler.add_ball()
#         if data["balls_in_over"] == 6:
#             data["total_overs"] += 1
#             data["balls_in_over"] = 0
#             self.swap_strike()
#             self.append_commentary("----- End of Over -----")
#
#         self.update_scoreboard()
#         self.update_player_info()
#
#     def swap_strike(self):
#         data = self.controller.match_data
#         data["current_batsmen"][0], data["current_batsmen"][1] = data["current_batsmen"][1], data["current_batsmen"][0]
#         self.update_player_info()
#
#     def change_bowler(self):
#         data = self.controller.match_data
#         bowlers = data["bowlers"]
#         data["current_bowler_index"] = (data["current_bowler_index"] + 1) % len(bowlers)
#         data["current_bowler"] = bowlers[data["current_bowler_index"]]
#         self.append_commentary(f"New bowler: {data['current_bowler'].name}")
#         self.update_player_info()
#
# # ==== Run the Application ====
#
# if __name__ == "__main__":
#     app = CricketScoringApp()
#     app.mainloop()
#
#
prices = [2,4,1]
sorted_l = sorted(prices,reverse=True)
max_profit = 0

if prices == sorted_l:
            print(0)
else:
    for i in prices:
        for j in prices[prices.index(i)+1:]:
            if j>i:
                profit = j-i
                if profit>max_profit:
                    max_profit=profit
print(max_profit)