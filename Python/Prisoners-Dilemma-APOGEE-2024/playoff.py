import random, copy

COOP = 1
DEFECT = -1

coop_win = lambda x: 20 + 5 * (x // 4)
betrayal_win = lambda x: 50
betrayal_lose = lambda x: -10 * (x // 4)
defect = lambda x: -5 * (x // 4)
payoff_matrx = [[coop_win, coop_win], [betrayal_win, betrayal_lose], [defect, defect]]

error = lambda x: max(1, 10 - x / 2) / 100
# time_limit = 0.001  # seconds
rounds = 175

def threaded_player_call(players, player, streak, history, iteration, move_queue):
    state = {"current_iter": iteration, "history": history, "streak": streak}
    # state = copy.deepcopy(state)
    move = players[player].next_move(state)
    # print(f"Player {player}:", move, iteration, history)
    if not iteration in history:
        move_queue[player] = move

def playoff(p1, p2):
    history = {}
    players = [p1, p2]
    move_queue = [0, 0]
    iteration = 1
    streak = 0
    score = {1: 0, 2: 0}

    while iteration <= rounds:
        # Starts threads to wait for agents to update move_queue and then waits for time limit
        # threading.Thread(target=threaded_player_call, args=(0, None, iteration)).start()
        # threading.Thread(target=threaded_player_call, args=(1, None, iteration)).start()
        # time.sleep(time_limit)
        threaded_player_call(players, 0, None, history, iteration, move_queue)
        threaded_player_call(players, 1, None, history, iteration, move_queue)

        # If TLE on first then random, else repeat last move
        if not move_queue[0] or move_queue[0] not in [COOP, DEFECT]:
            if iteration == 1:
                move_queue[0] = random.choice([COOP, DEFECT])
            else:
                move_queue[0] = history[iteration - 1][1]

        if not move_queue[1] or move_queue[1] not in [COOP, DEFECT]:
            if iteration == 1:
                move_queue[1] = random.choice([COOP, DEFECT])
            else:
                move_queue[1] = history[iteration - 1][2]

        # errors in communication with agents
        is_err1 = random.random() < error(streak)
        is_err2 = random.random() < error(streak)

        if is_err1:
            move_queue[0] = -move_queue[0]
        if is_err2:
            move_queue[1] = -move_queue[1]

        """
        Payoff matrix calculations
        Streak is not reset to 0 if rift in communication is caused by errors
        """

        if move_queue[0] == COOP and move_queue[1] == COOP:
            score[1] += payoff_matrx[0][0](streak)
            score[2] += payoff_matrx[0][1](streak)
            streak += 1
        elif move_queue[0] == DEFECT and move_queue[1] == COOP:
            score[1] += payoff_matrx[1][0](streak)
            score[2] += payoff_matrx[1][1](streak)
            streak = (streak + 1) // 2 if (is_err1 or is_err2) else 0
        elif move_queue[0] == COOP and move_queue[1] == DEFECT:
            score[1] += payoff_matrx[1][1](streak)
            score[2] += payoff_matrx[1][0](streak)
            streak = (streak + 1) // 2 if (is_err1 or is_err2) else 0
        else:
            score[1] += payoff_matrx[2][0](streak)
            score[2] += payoff_matrx[2][1](streak)
            streak = (streak + 1) // 2 if (is_err1 and is_err2) else 0

        history[iteration] = {
            1: move_queue[0],
            2: move_queue[1],
            "score": copy.deepcopy(score),
        }
        move_queue = [0, 0]

        iteration += 1

    return score[1], score[2]
