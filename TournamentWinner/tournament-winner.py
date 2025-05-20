def tournamentWinner(competitions, results):
    results_counter = 0
    output = {}
    max_wins = 0
    max_wins_team = None
    for teams in competitions:
        if results[results_counter] == 0:
            output[teams[1]] = output.get(teams[1], 0) + 3
        else:
            output[teams[0]] = output.get(teams[0], 0) + 3

        results_counter += 1

    for key in output.keys():
        if output[key] > max_wins:
            max_wins = output[key]
            max_wins_team = key   

    return max_wins_team
        
        



        
