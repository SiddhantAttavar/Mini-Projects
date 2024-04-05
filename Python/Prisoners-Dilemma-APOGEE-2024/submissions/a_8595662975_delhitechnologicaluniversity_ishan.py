from agent import BaseAgent
from random import randint
class Agent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)
        self.forgiveness = randint(10,20)
        self.first_move = 1
        self.dishonesty = 0
        
    def next_move(self,state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]
        if (itr == 1):
            return self.first_move;
        
        history = state['history']
        mylastMove = state['history'][itr-1][self.id]
        oplastMove = state['history'][itr-1][op_id]
        
        if (itr == 2):
            if oplastMove == -1:
                self.dishonesty += 1
        
        if (itr > 2 and history[itr-2][self.id] == 1 and oplastMove == 1):
            self.dishonesty = 0
            
        if (itr > 2 and history[itr-2][self.id] == 1 and oplastMove == -1):
            self.dishonesty += 1
            if self.dishonesty >= 3:
                self.forgiveness = 0
                
                
        if oplastMove == -1:
            if randint(1,100) <= self.forgiveness:
                return 1
            else:
                return -1
        return 1