from agent import BaseAgent

class NiceAndGreedyAgent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]
        greed =0
        while (itr == 1)or(state["history"][itr - 1][op_id] ==1):
            if state['streak'] > 4 :
                greed = 2
                return -1            
            return 1
        if state["history"][itr - 1][op_id] == -1 :
            if greed >0 :
                greed -=1
                return 1
            return -1
        
