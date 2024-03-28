from agent import BaseAgent
from random import random

class RandomAgent(BaseAgent):
    def __init__(self, id, defect_prob):
        super().__init__(id=id)
        self.defect_prob = defect_prob

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        if random() < self.defect_prob:
            return -1
        return 1
