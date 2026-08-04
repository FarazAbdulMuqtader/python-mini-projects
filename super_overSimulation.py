import random

class Batsman:
    def __init__(self, name):
        self.name = name
        self.runs_scored = 0  
    def score_runs(self, runs):
        self.runs_scored += runs

player = Batsman("Babar")

print(f"--- Starting over for {player.name} ---")
for ball in range(1, 7):
    runs_this_ball = random.choice([0, 1, 2, 4, 6])
    player.score_runs(runs_this_ball)
    print(f"Ball {ball}: {runs_this_ball} run(s)")
    
print(f"{player.name}'s Total Runs: {player.runs_scored}")