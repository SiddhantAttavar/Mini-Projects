from agent import BaseAgent
import random


class Agent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]

        if itr == 1 or itr == 2:
            return -1
            # return 0

        last_opponent_move = state["history"][itr - 1][op_id]
        if last_opponent_move == 1 or state["history"][itr - 2][op_id] == 1:
            return 1
        else:
            if random.random() < 0.1:
                return 1
            else:
                return -1
