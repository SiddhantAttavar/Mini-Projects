from agent import BaseAgent
from random import randint

class Agent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)
        self.hist=[]

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"] # number of rounds played
        if itr == 1:
            return 1
        if state["history"][itr - 1][op_id]:
            self.hist.append(1)
        else:
            self.hist.append(-1)
        if(len(self.hist) == 30):
            self.hist.pop(0)
        total = sum(self.hist)
        if total>=0:
            return 1
        else:
            return 0