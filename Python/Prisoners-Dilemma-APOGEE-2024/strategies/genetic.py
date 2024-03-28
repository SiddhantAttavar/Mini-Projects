from agent import BaseAgent
from math import log2

class GeneticAgent(BaseAgent):
    def __init__(self, id, strat):
        super().__init__(id = id)
        self.vis = int(log2(len(strat))) // 2
        self.strat = strat

    def next_move(self, state):
        opp_id = 1 if self.id == 2 else 2

        curr_itr = state['current_iter']
        hist = state['history']
        encoded_visible_hist = 0
        for i in range(max(1, curr_itr - self.vis), curr_itr):
            encoded_visible_hist = 2 * encoded_visible_hist + (hist[i][self.id] == 1)
            encoded_visible_hist = 2 * encoded_visible_hist + (hist[i][opp_id] == 1)
        
        if self.strat[encoded_visible_hist]:
            return 1
        return -1

