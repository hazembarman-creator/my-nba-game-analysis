# My NBA Game Analysis
A Python project that analyzes NBA play‑by‑play data and generates full player statistics for both teams based on game events.

***

## Task
You are given NBA play‑by‑play event lines such as:

"1|708.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|0|Turnover by K. Thompson (bad pass; steal by S. Adams)"
"1|703.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|0|Turnover by P. George (bad pass)"
"1|691.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|3|S. Curry makes 3-pt jump shot from 24 ft (assist by K. Durant)"

Code

Your task is to build a function:

### `analyse_nba_game(play_by_play_moves)`
This function must:

- Parse each play  
- Detect the action (shot, rebound, assist, turnover, foul, block…)  
- Identify the player involved  
- Update the correct stat in the correct team  
- Build a full statistical summary for both teams  

The returned dictionary must follow this structure:

```json
{
  "home_team": {
    "name": "TEAM_NAME",
    "players_data": [ ... ]
  },
  "away_team": {
    "name": "TEAM_NAME",
    "players_data": [ ... ]
  }
}
Each player must include:

Code
FG, FGA, FG%, 3P, 3PA, 3P%, FT, FTA, FT%, 
ORB, DRB, TRB, AST, STL, BLK, TOV, PF, PTS
Description
Each play follows this format:

Code
PERIOD|REMAINING_SEC|RELEVANT_TEAM|AWAY_TEAM|HOME_TEAM|AWAY_SCORE|HOME_SCORE|DESCRIPTION
Example:

Code
1|691.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|3|S. Curry makes 3-pt jump shot from 24 ft (assist by K. Durant)
Your program must:

Parse the string

Extract the player name

Detect the type of action

Update the correct stat

Aggregate totals for each team

This project teaches:

Data parsing

Pattern recognition

Statistical aggregation

Clean dictionary structuring

Printing formatted tables

Installation
Clone the repository:

bash
git clone https://github.com/yourusername/my_nba_game_analysis.git
cd my_nba_game_analysis
Make sure you have Python 3.x installed.

macOS / Linux
bash
brew install python3
Windows
Download Python from:

Code
https://www.python.org/downloads/
No external dependencies are required — only Python’s built‑in libraries.

Usage
Example usage:

python
from my_nba_game_analysis import analyse_nba_game, print_nba_game_stats

game_data = [
    "1|708.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|0|Turnover by K. Thompson (bad pass; steal by S. Adams)",
    "1|691.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|3|S. Curry makes 3-pt jump shot from 24 ft (assist by K. Durant)",
    "1|671.00|OKLAHOMA_CITY_THUNDER|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|3|Offensive rebound by D. Schröder"
]

summary = analyse_nba_game(game_data)

print_nba_game_stats(summary["home_team"])
print_nba_game_stats(summary["away_team"])
Run your project:

bash
python my_nba_game_analysis.py
Or:

bash
./my_project argument1 argument2
Tips
If you’re unsure what abbreviations like TRB, AST, or PF mean —
search for NBA box score abbreviations.
Understanding your dataset deeply is part of being a great data scientist.

The Core Team
Hazem — Project Lead & Developer

Team Member (Testing) — Verified accuracy of stats and edge cases

Team Member (Documentation) — Contributed to README and usage examples
