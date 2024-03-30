from agent import BaseAgent

class DefectAgent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)

    def next_move(self, state):
        return -1
