def tournamentWinner(competitions, results):
    output = {}
    max_wins = 0
    max_wins_team = None

    for i, teams in enumerate(competitions):
        winner = teams[0] if results[i] == 1 else teams[1]
        output[winner] = output.get(winner, 0) + 3

        if output[winner] > max_wins:
            max_wins = output[winner]
            max_wins_team = winner

    return max_wins_team
