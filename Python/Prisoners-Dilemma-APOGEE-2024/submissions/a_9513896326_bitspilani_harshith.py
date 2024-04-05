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
        
        credits = 7
        defections = 0

        for i in range(1, itr):
            if state["history"][i][op_id] == 1:
                credits += 1
                if (credits > 8):
                    credits = 8

            elif state["history"][i][op_id] == -1:
                credits -= 2
                defections += 1
                if (credits < -7):
                    credits = -7
            
            if (i > 2 and i < itr-1 and credits < 0):
                credits = 4
        
        if (itr == 2):
            return 1
        
        if (credits > 0):
            return 1
        
        if (itr <= 10):
            return -1

        if (defections/itr >= 0.15):
            return -1
        
        return 1
    