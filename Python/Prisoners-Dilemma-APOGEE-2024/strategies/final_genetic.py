from agent import BaseAgent
class Agent(BaseAgent):
    def __init__(self, id):super().__init__(id)
    def next_move(self, s):
        x = 0
        for i in range(max(1,s['current_iter']-3),s['current_iter']):
            x=(x<<2)^(s['history'][i][self.id]+1)^((s['history'][i][3-self.id]+1)>>1)
        return ((17289855990632610313>>x)&1)<<1-1
