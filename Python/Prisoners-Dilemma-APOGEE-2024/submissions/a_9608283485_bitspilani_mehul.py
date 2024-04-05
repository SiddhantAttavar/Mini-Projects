from agent import BaseAgent
import random

class Agent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]
        if random.randint(1, 10) == 7: return 1
        else: return state["history"][itr - 1][op_id] if itr != 1 else 1