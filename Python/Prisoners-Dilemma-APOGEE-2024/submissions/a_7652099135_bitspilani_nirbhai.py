from agent import BaseAgent

class Agent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]

        # Always cooperate on the first round.
        if itr == 1:
            return 1
        
        # Review opponent's last move.
        opponent_last_move = state["history"][itr - 1][op_id]
        
        # Check for a consistent pattern of defection, which might suggest a non-tit-for-tat player.
        if itr >= 4:
            consistent_defections = all(state["history"][itr - i][op_id] == -1 for i in range(1, 4))
            if consistent_defections:
                # If facing consistent defections, retaliate.
                return -1

        # If the opponent cooperated in the last round, we continue to cooperate.
        if opponent_last_move == 1:
            return 1
        
        # If the opponent defected in the last round, retaliate once, but be ready to switch back to cooperation.
        if opponent_last_move == -1:
            # Before retaliating, check if this is a one-time defection or a pattern.
            if itr == 2 or (itr > 2 and state["history"][itr - 2][op_id] == 1):
                # It might be a one-time defection, so retaliate once.
                return -1
            else:
                # It seems to be a pattern of defections, be cautious but ready to switch back to cooperation.
                # Look for a chance to cooperate again if they switch back.
                if itr > 3 and state["history"][itr - 3][op_id] == 1:
                    return 1
                else:
                    return -1

        # Default action is to cooperate.
        return 1
