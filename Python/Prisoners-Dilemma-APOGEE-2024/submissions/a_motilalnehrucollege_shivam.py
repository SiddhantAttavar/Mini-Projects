from agent import BaseAgent


class Agent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2

        itr = state["current_iter"]
        # If it's the first round, cooperate
        if itr == 1:
            return 1
        # Get the opponent's last move
        op_last_move = state["history"][itr - 1][op_id]
        # If the opponent cooperated in the last round, cooperate
        if op_last_move == 1:
            return 1
        # If the opponent defected in the last round
        else:
            # Check if it was a misinterpretation by generating a random number
            import random

            if random.random() < 0.02:  # 2% chance of misinterpretation
                # If it was a misinterpretation, cooperate (forgive)
                return 1
            else:
                # If it was not a misinterpretation, defect
                return -1
