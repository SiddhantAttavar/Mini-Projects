from agent import BaseAgent

class PreemptErrorAgent(BaseAgent):
    def __init__(self, id, max_forgiveness):
        super().__init__(id=id)
        self.streak = 0
        self.max_forgiveness = max_forgiveness
        self.forgive_count = 0

    def next_move(self, state):
        opp_id = 3 - self.id
        itr = state['current_iter']
        history = state['history']

        if itr == 1:
            return 1

        if self.streak == 44:
            return 1

        if history[itr - 1][self.id] == 1 and history[itr - 1][opp_id] == 1:
            self.streak += 1
        else:
            self.streak = 0

        if self.forgive_count < self.max_forgiveness:
            self.forgive_count += 1
            return 1

        if self.streak == 44:
            return -1
        return history[itr - 1][opp_id]
