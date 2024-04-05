from agent import BaseAgent
from random import randint

class Agent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]
        if itr == 1:
            return 1
        i = randint(1, 1000)
        if i>998:
            return 1
        return state["history"][itr - 1][op_id]
        
    