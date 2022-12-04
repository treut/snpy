class WrongNumberOfPlayersError(Exception):
    """ Количество игроков больше 2 """
    pass


class NoSuchStrategyError(Exception):
    """ Ход отличается от R, P или S """
    pass


def rps_game_winner(players):
    if len(players) > 2:
        raise WrongNumberOfPlayersError
    for player in players:
        if player[1] not in ['R', 'P', 'S']:
            raise NoSuchStrategyError
    pl1 = players[0]
    pl2 = players[1]
    if (pl1[1] == "S" and pl2[1] == "P") or \
            (pl1[1] == "R" and pl2[1] == "S") or \
            (pl1[1] == "P" and pl2[1] == "R") or \
            (pl1[1] == pl2[1]):
        result = pl1
    else:
        result = pl2

    print(" ".join(result))


# rps_game_winner([["player1", "P"], ["player2", "S"], ["player3", "S"]])

# rps_game_winner([["player1", "P"], ["player2", "A"]])

rps_game_winner([["player1", "P"], ["player2", "S"]])
# rps_game_winner([["player1", "S"], ["player2", "P"]])
# rps_game_winner([["player1", "S"], ["player2", "R"]])
# rps_game_winner([["player1", "R"], ["player2", "S"]])
# rps_game_winner([["player1", "R"], ["player2", "P"]])
# rps_game_winner([["player1", "P"], ["player2", "R"]])

# rps_game_winner([["player1", "P"], ["player2", "P"]])
# rps_game_winner([["player1", "S"], ["player2", "S"]])
# rps_game_winner([["player1", "R"], ["player2", "R"]])
