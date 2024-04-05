from agent import BaseAgent
import random

class Agent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]

        if itr == 1:
            return 1

        last_op_move = state["history"][itr-1][op_id]

        if last_op_move == -1 and random.random() < 0.1:
            return 1
        else:
            return last_op_move
    