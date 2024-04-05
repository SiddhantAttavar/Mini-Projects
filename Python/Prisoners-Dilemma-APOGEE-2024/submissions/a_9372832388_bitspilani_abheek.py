from agent import BaseAgent

class Agent(BaseAgent):
    def _init_(self, id):
        super()._init_(id=id)

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]


        if itr==1 or itr == 2:
            return 1 #cooperate for first 2
        

        consec = 0
        lastmove = state["history"][itr - 1][op_id]

        if lastmove==1:
            return 1
            
        else:
            for i in range (1,itr):
                move = state["history"][itr-i][op_id]
                if move==-1:
                    consec+=1
                if consec>=2:
                    return -1
                if move==1:
                    break

            return 1