from agent import BaseAgent
import random

class Agent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"] # number of rounds played
        if itr < 4:
            return 1
        else:
            if( state["history"][itr - 1][op_id]==0 and state["history"][itr - 2][op_id]==0 and state["history"][itr - 3][op_id]==0 ):
                return 0
            else:
                return 1
       
    