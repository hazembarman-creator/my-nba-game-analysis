def print_nba_game_stats(team_dict):
    # Print header
    print("Players\tFG\tFGA\tFG%\t3P\t3PA\t3P%\tFT\tFTA\tFT%\tORB\tDRB\tTRB\tAST\tSTL\tBLK\tTOV\tPF\tPTS")
    
    # Function to print individual player stats
    def print_player_stats(player_data):
        fg = player_data["FG"]
        fga = player_data["FGA"]
        fg_percent = fg / fga if fga > 0 else 0
        fg_percent = round(fg_percent, 3)
        
        threep = player_data["3P"]
        threepa = player_data["3PA"]
        threep_percent = threep / threepa if threepa > 0 else 0
        threep_percent = round(threep_percent, 3)

        ft = player_data["FT"]
        fta = player_data["FTA"]
        ft_percent = ft / fta if fta > 0 else 0
        ft_percent = round(ft_percent, 3)

        # Print the player stats
        print(f"{player_data['player_name']}\t{fg}\t{fga}\t{fg_percent}\t{threep}\t{threepa}\t{threep_percent}\t{ft}\t{fta}\t{ft_percent}\t{player_data['ORB']}\t{player_data['DRB']}\t{player_data['TRB']}\t{player_data['AST']}\t{player_data['STL']}\t{player_data['BLK']}\t{player_data['TOV']}\t{player_data['PF']}\t{player_data['PTS']}")

    # Function to print total stats for the team
    def print_team_totals(team_data):
        total_fg = sum(player["FG"] for player in team_data["players_data"].values())
        total_fga = sum(player["FGA"] for player in team_data["players_data"].values())
        total_3p = sum(player["3P"] for player in team_data["players_data"].values())
        total_3pa = sum(player["3PA"] for player in team_data["players_data"].values())
        total_ft = sum(player["FT"] for player in team_data["players_data"].values())
        total_fta = sum(player["FTA"] for player in team_data["players_data"].values())
        total_orb = sum(player["ORB"] for player in team_data["players_data"].values())
        total_drb = sum(player["DRB"] for player in team_data["players_data"].values())
        total_trb = total_orb + total_drb
        total_ast = sum(player["AST"] for player in team_data["players_data"].values())
        total_stl = sum(player["STL"] for player in team_data["players_data"].values())
        total_blk = sum(player["BLK"] for player in team_data["players_data"].values())
        total_tov = sum(player["TOV"] for player in team_data["players_data"].values())
        total_pf = sum(player["PF"] for player in team_data["players_data"].values())
        total_pts = sum(player["PTS"] for player in team_data["players_data"].values())

        print(f"Team Totals\t{total_fg}\t{total_fga}\t{round(total_fg / total_fga if total_fga > 0 else 0, 3)}\t{total_3p}\t{total_3pa}\t{round(total_3p / total_3pa if total_3pa > 0 else 0, 3)}\t{total_ft}\t{total_fta}\t{round(total_ft / total_fta if total_fta > 0 else 0, 3)}\t{total_orb}\t{total_drb}\t{total_trb}\t{total_ast}\t{total_stl}\t{total_blk}\t{total_tov}\t{total_pf}\t{total_pts}")

    # Print stats for home and away teams
    for team in [team_dict["home_team"], team_dict["away_team"]]:
        print(f"Stats for {team['name']}:")
        for player_name, player_data in team["players_data"].items():
            print_player_stats(player_data)
        print_team_totals(team) 
        