from agent import BaseAgent
class Agent(BaseAgent):
    def __init__(self, id):
        super().__init__(id = id)

    def next_move(self, state):
        opp_id = 1 if self.id == 2 else 2

        curr_itr = state['current_iter']
        hist = state['history']
        encoded_visible_hist = 0
        for i in range(max(1, curr_itr - 3), curr_itr):
            encoded_visible_hist = 2 * encoded_visible_hist + (hist[i][self.id] == 1)
            encoded_visible_hist = 2 * encoded_visible_hist + (hist[i][opp_id] == 1)
        
        if 18156819335893725033 & (1 << encoded_visible_hist):
            return 1
        return -1

