Hey!
Here's the eval engine for you to test your strategies. Just modify the existing strategies or make new one's. Simply modify player1 and player2 (line 3,10,11) and run the code. 

Also while submitting your strategy, stick to the format given in the main document.
It should look something like this:

from agent import BaseAgent

class Agent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]
        if itr == 1:
            return 1
        return state["history"][itr - 1][op_id]

DO NOT CHANGE LINE 9-14

Also make sure the name of your strategy and file are exactly the same.

All the best! 