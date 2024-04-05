from agent import BaseAgent
import math

class Agent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]
        if itr <= 10 or state["history"][itr - 1][op_id] == 1:
            return 1
        if int(math.log(itr)) * sum([1 for i in range(1,itr) if state["history"][i][op_id] == -1]) >= itr:
            return -1
        return 1
    