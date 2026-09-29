def analyse_nba_game(play_by_play_moves):
    # Initialize empty dictionaries for home and away team statistics
    home_team_stats = {}
    away_team_stats = {}

    # Helper function to initialize player data structure
    def init_player_data(player_name):
        return {
            "player_name": player_name,
            "FG": 0, "FGA": 0, "FG%": 0,
            "3P": 0, "3PA": 0, "3P%": 0,
            "FT": 0, "FTA": 0, "FT%": 0,
            "ORB": 0, "DRB": 0, "TRB": 0,
            "AST": 0, "STL": 0, "BLK": 0,
            "TOV": 0, "PF": 0, "PTS": 0
        }

    # Helper function to ensure player data is initialized
    def get_or_init_player(team_stats, player_name):
        if player_name not in team_stats:
            team_stats[player_name] = init_player_data(player_name)
        return team_stats[player_name]

    # Iterate through each play and update statistics
    for play in play_by_play_moves:
        period, remaining_sec, relevant_team, away_team, home_team, away_score, home_score, description = play.split('|')
        
        # Determine which team is home and away, based on the play's relevant team
        if relevant_team == home_team:
            team_stats = home_team_stats
        else:
            team_stats = away_team_stats
        
        # Parsing the description for player actions
        description = description.lower()

        # Check for scoring actions (2P, 3P, FT)
        if 'makes' in description:
            player_name = description.split('makes')[1].split('(')[0].strip()
            player_data = get_or_init_player(team_stats, player_name)

            if '3-pt' in description:
                player_data["3P"] += 1
                player_data["3PA"] += 1
                player_data["PTS"] += 3
            elif 'free throw' in description:
                player_data["FT"] += 1
                player_data["FTA"] += 1
                player_data["PTS"] += 1
            else:
                player_data["FG"] += 1
                player_data["FGA"] += 1
                player_data["PTS"] += 2

        # Check for missed shots
        elif 'misses' in description:
            player_name = description.split('misses')[1].split('(')[0].strip()
            player_data = get_or_init_player(team_stats, player_name)

            if '3-pt' in description:
                player_data["3PA"] += 1
            else:
                player_data["FGA"] += 1

        # Check for rebounds (offensive or defensive)
        elif 'offensive rebound' in description:
            player_name = description.split('by')[1].strip()
            player_data = get_or_init_player(team_stats, player_name)
            player_data["ORB"] += 1
        elif 'defensive rebound' in description:
            player_name = description.split('by')[1].strip()
            player_data = get_or_init_player(team_stats, player_name)
            player_data["DRB"] += 1

        # Check for assists
        elif 'assist' in description:
            player_name = description.split('by')[1].strip()
            player_data = get_or_init_player(team_stats, player_name)
            player_data["AST"] += 1

        # Check for steals
        elif 'steal' in description:
            player_name = description.split('by')[1].strip()
            player_data = get_or_init_player(team_stats, player_name)
            player_data["STL"] += 1

        # Check for blocks
        elif 'block' in description:
            player_name = description.split('by')[1].strip()
            player_data = get_or_init_player(team_stats, player_name)
            player_data["BLK"] += 1

        # Check for turnovers
        elif 'turnover' in description:
            player_name = description.split('by')[1].strip()
            player_data = get_or_init_player(team_stats, player_name)
            player_data["TOV"] += 1

        # Check for personal fouls
        elif 'foul' in description:
            player_name = description.split('by')[1].strip()
            player_data = get_or_init_player(team_stats, player_name)
            player_data["PF"] += 1

    # Helper function to calculate shooting percentages
    def calculate_shooting_percentages(player_stats):
        if player_stats["FGA"] > 0:
            player_stats["FG%"] = round(player_stats["FG"] / player_stats["FGA"] * 100, 2)
        if player_stats["3PA"] > 0:
            player_stats["3P%"] = round(player_stats["3P"] / player_stats["3PA"] * 100, 2)
        if player_stats["FTA"] > 0:
            player_stats["FT%"] = round(player_stats["FT"] / player_stats["FTA"] * 100, 2)

    # Convert stats into player data format
    def convert_to_player_data(team_stats):
        players_data = []
        for player_name, stats in team_stats.items():
            calculate_shooting_percentages(stats)
            players_data.append(stats)
        return players_data

    # Return game summary
    return {
        "home_team": {
            "name": home_team,
            "players_data": convert_to_player_data(home_team_stats)
        },
        "away_team": {
            "name": away_team,
            "players_data": convert_to_player_data(away_team_stats)
        }
    }

play_by_play = [
    "1|720|home|team_away|team_home|0|0|Player A makes 3-pt shot (assist by Player B)",
    "1|710|home|team_away|team_home|3|0|Player C misses 3-pt shot (defensive rebound by Player A)",
    "1|700|away|team_away|team_home|3|0|Player D makes free throw (foul by Player C)",
    # More plays...
]

game_summary = analyse_nba_game(play_by_play)
print(game_summary)

def print_nba_game_stats(team_dict):
    # Print the header
    print("Players\tFG\tFGA\tFG%\t3P\t3PA\t3P%\tFT\tFTA\tFT%\tORB\tDRB\tTRB\tAST\tSTL\tBLK\tTOV\tPF\tPTS")
    
    # Initialize total stats for the team
    total_stats = {
        "FG": 0, "FGA": 0, "3P": 0, "3PA": 0, "FT": 0, "FTA": 0,
        "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0,
        "TOV": 0, "PF": 0, "PTS": 0
    }

    for player in team_dict["players_data"]:
        # Print player stats
        print(f"{player['player_name']}\t{player['FG']}\t{player['FGA']}\t{player['FG%']}\t{player['3P']}\t{player['3PA']}\t{player['3P%']}\t{player['FT']}\t{player['FTA']}\t{player['FT%']}\t{player['ORB']}\t{player['DRB']}\t{player['TRB']}\t{player['AST']}\t{player['STL']}\t{player['BLK']}\t{player['TOV']}\t{player['PF']}\t{player['PTS']}")
        
        # Accumulate total stats
        for stat in total_stats:
            total_stats[stat] += player[stat]

    # Helper function to safely calculate percentages
    def safe_percentage(numerator, denominator):
        return round(numerator / denominator * 100, 2) if denominator > 0 else 0.0

    # Print total stats for the team with percentage calculations
    print(f"Totals\t{total_stats['FG']}\t{total_stats['FGA']}\t{safe_percentage(total_stats['FG'], total_stats['FGA'])}\t{total_stats['3P']}\t{total_stats['3PA']}\t{safe_percentage(total_stats['3P'], total_stats['3PA'])}\t{total_stats['FT']}\t{total_stats['FTA']}\t{safe_percentage(total_stats['FT'], total_stats['FTA'])}\t{total_stats['ORB']}\t{total_stats['DRB']}\t{total_stats['TRB']}\t{total_stats['AST']}\t{total_stats['STL']}\t{total_stats['BLK']}\t{total_stats['TOV']}\t{total_stats['PF']}\t{total_stats['PTS']}")


# Example play-by-play data for testing
play_by_play_moves = [
    "1|708.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|0|Turnover by K. Thompson (bad pass; steal by S. Adams)",
    "1|691.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|3|S. Curry makes 3-pt jump shot from 24 ft (assist by K. Durant)",
    "1|657.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|0|5|K. Durant makes 2-pt layup from 2 ft",
    "1|533.00|GOLDEN_STATE_WARRIORS|OKLAHOMA_CITY_THUNDER|GOLDEN_STATE_WARRIORS|4|10|K. Thompson makes 3-pt jump shot from 26 ft (assist by D. Green)"
]

# Analyse the game
game_summary = analyse_nba_game(play_by_play_moves)

# Print team statistics
print_nba_game_stats(game_summary["home_team"])