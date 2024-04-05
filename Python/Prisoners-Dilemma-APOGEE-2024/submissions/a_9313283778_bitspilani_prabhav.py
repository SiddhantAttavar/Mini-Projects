from agent import BaseAgent
import random


class Agent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)
        self.s = 0

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2

        itr = state["current_iter"]
        if itr <= 10:
            if itr % 2 == 1:
                return 1
            else:
                return -1

        if (
            state["history"][itr - 1][op_id] == 1
            and state["history"][itr - 1][self.id] == 1
        ):
            self.s += 1

        if (
            state["history"][itr - 1][op_id] == -1
            or state["history"][itr - 1][self.id] == -1
        ):
            self.s = 0
        sum = 0
        t = 0
        for i in range(1, 11):
            sum = sum + state["history"][i][op_id]

        if sum >= 7:
            t = 1
        elif sum <= -6:
            t = 2
        elif sum > -2 and sum < 2:
            t = 3
        else:
            t = 4

        if itr == 11:
            return 1
        p = random.random()
        if p > 0.1:
            if self.s == 5:
                return -1
        else:
            if self.s == 10:
                return -1
        if itr > 11:
            if t == 1:
                return -1
            elif t == 2:
                return -1
            elif t == 3:

                if (
                    state["history"][itr - 1][op_id]
                    == state["history"][itr - 1][self.id]
                ):
                    return 1
                else:
                    return -1
            elif t == 4:
                if (
                    state["history"][itr - 1][op_id]
                    == state["history"][itr - 1][self.id]
                ):
                    return 1
                else:
                    return -1
