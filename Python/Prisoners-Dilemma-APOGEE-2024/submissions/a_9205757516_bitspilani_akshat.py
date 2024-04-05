from agent import BaseAgent
import random


class Agent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2

        itr = state["current_iter"]

        if itr == 1:
            return 1

        opponent_last_move = state["history"][itr - 1][op_id]
        my_last_2 = []
        opponent_last_3 = []

        if itr >= 3:
            my_last_2 = [state["history"][itr - i][self.id] for i in range(1, 3)]

        if itr >= 4:
            opponent_last_3 = [state["history"][itr - i][op_id] for i in range(1, 4)]

        if opponent_last_3 == [-1, -1, -1]:
            return 1

        if random.random() > 0.9:

            if -1 in my_last_2:
                return 1
        return opponent_last_move
