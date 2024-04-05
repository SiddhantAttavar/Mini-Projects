from agent import BaseAgent
import random


class Agent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)
        self.cooperation_probability = 0

    def next_move(self, state):
        itr = state["current_iter"]
        op_id = 1 if self.id == 2 else 2  # Opponent's ID

        if itr == 1:
            return 1  # Cooperate on the first move

        # Get opponent's move from the previous round
        opponent_last_move = state["history"][itr - 1][op_id]

        # Adjust cooperation probability based on opponent's historical behavior
        self.adjust_cooperation_probability(opponent_last_move)

        if opponent_last_move == 1:
            return 1

        # Decide whether to cooperate based on the adjusted probability including randomness
        return 1 if random.uniform(0, 1) < self.cooperation_probability else -1
    def adjust_cooperation_probability(self, opponent_last_move):
        # Update cooperation probability based on opponent's historical behavior
        if opponent_last_move == 1:
            self.cooperation_probability = min(1, self.cooperation_probability + 0.25)
        elif opponent_last_move == 0:
            self.cooperation_probability = max(0, self.cooperation_probability - 0.8)