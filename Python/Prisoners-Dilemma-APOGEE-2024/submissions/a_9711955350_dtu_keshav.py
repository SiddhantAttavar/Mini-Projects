from agent import BaseAgent
import random

class Agent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)
        self.forgiveness_factor = 0.3
    
    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]
        if itr == 1:
            return 1
        opponent_last_move = state["history"][itr - 1][op_id]
        if opponent_last_move == 0:
            return 1 if random.random() < self.forgiveness_factor else 0
        return 1


