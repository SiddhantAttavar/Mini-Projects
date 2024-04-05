from agent import BaseAgent


class Agent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2

        itr = state["current_iter"]
        if itr == 1:
            return 1
        if state["history"][itr - 1][op_id] == 1:
            return 1
        if itr == 2:
            return 1
        if state["history"][itr - 2][op_id] == 1:
            return 1
        else:
            return -1
