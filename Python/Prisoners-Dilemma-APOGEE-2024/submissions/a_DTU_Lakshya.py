from agent import BaseAgent

class Agent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)
        self.defect_streak = 0
        self.cooperate_streak = 0

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]

        # Initialize streaks if not initialized
        if not hasattr(self, 'defect_streak'):
            self.defect_streak = 0
        if not hasattr(self, 'cooperate_streak'):
            self.cooperate_streak = 0

        # Cooperate in the first round
        if itr == 1:
            return 1

        # Check opponent's move in the last round
        if itr > 1:
            opponent_last_move = state["history"][itr - 1][op_id]
            own_last_move = state["history"][itr - 1][self.id]

            # Update streaks
            if opponent_last_move == -1:
                self.defect_streak += 1
                self.cooperate_streak = 0
            else:
                self.cooperate_streak += 1
                self.defect_streak = 0

            # If opponent cooperates after a series of -1, cooperate twice
            if self.defect_streak >= 5 and opponent_last_move == 1 and self.cooperate_streak == 1:
                return 1

            # Defect if opponent defected last round and we cooperated
            if self.cooperate_streak >= 5 and opponent_last_move == -1:
                return 1

            if opponent_last_move == -1 and own_last_move == 1:
                return -1
            if opponent_last_move == -1 and own_last_move == -1:
                return -1
            if opponent_last_move == 1 and own_last_move == 1:
                return 1
            else:
                return 1
