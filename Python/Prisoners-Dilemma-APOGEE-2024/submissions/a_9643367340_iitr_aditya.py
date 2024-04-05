from agent import BaseAgent
import random

class Agent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr= state["current_iter"]
        if itr==1:
            return 1
        rand_num = random.randint(1, 100)
        if state["history"][itr-1][op_id]==1 :
            return 1;
        else :
            if rand_num<=98 :
                return -1;
            else :
                return 1;

            
        

    