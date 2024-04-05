from agent import BaseAgent
import random

bruh = {}

class Agent(BaseAgent):

    def __init__(self, id):
        super().__init__(id=id)
        self.zero_streak = 0
        self.coop_streak = 0
        self.forgiveness = 2
        self.buffer = 0
        self.error_forgiveness = 3
        self.op_zero_count = 0
        self.tft_check = 0

        self.update = {"zs": 0, "zc": 0, "cs": 0, "ef": 3}

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]

        # region hardcode
        if itr == 1:
            return -1
        opp, me = state["history"][itr - 1][op_id], state["history"][itr - 1][self.id]
        if itr == 3:
            return -1
        elif itr in [2, 4]:
            return 1

        if itr == 170 and self.coop_streak > 25:
            return -1

        if self.buffer > 0:
            self.buffer -= 1
            return 1
        # endregion

        # region streak update
        self.coop_streak = self.update["cs"]
        self.op_zero_count = self.update["zc"]
        self.error_forgiveness = self.update["ef"]
        self.zero_streak = self.update["zs"]

        if itr > 1 and opp + me == -2:
            self.update["zs"] += 1
        else:
            self.update["zs"] = 0

        if itr > 1 and opp == -1:
            self.update["zc"] += 1
        else:
            self.update["zc"] = 0

        if itr > 1 and opp + me == 2:
            self.update["cs"] += 1

        else:
            self.update["cs"] = 0

        if self.coop_streak > 0 and self.coop_streak % 25 == 0:
            self.update["ef"] += 1

        # endregion

        # region TFT
        if self.tft_check > 2:
            if self.tft_check > 5:
                return 1

            if (
                state["history"][itr - 4][op_id] == -1
                and state["history"][itr - 3][op_id] == 1
                and state["history"][itr - 2][op_id] == -1
                and state["history"][itr - 1][op_id] == 1
                and state["history"][itr - 4][self.id] == 1
                and state["history"][itr - 3][self.id] == -1
                and state["history"][itr - 2][self.id] == 1
                and state["history"][itr - 1][self.id] == -1
            ):
                self.tft_check += 2
                self.buffer += 1
                return 1

            if opp == -1:
                if self.coop_streak > 10:
                    self.error_forgiveness -= 0.5
                    self.buffer += 1
                    return 1

                if self.op_zero_count > 2 and self.zero_streak == 0:

                    return 1

                if self.zero_streak > 3 and self.forgiveness > 0:
                    self.forgiveness -= 1
                    self.buffer += 1
                    return 1

            return opp
        # endregion

        # region Not TFT
        if itr == 5:
            if (
                state["history"][itr - 3][op_id] == -1
                and state["history"][itr - 2][op_id] == 1
                and state["history"][itr - 1][op_id] == -1
            ):
                self.tft_check += 2
                return 1

        if (
            state["history"][itr - 4][op_id] == -1
            and state["history"][itr - 3][op_id] == 1
            and state["history"][itr - 2][op_id] == -1
            and state["history"][itr - 1][op_id] == 1
            and state["history"][itr - 4][self.id] == 1
            and state["history"][itr - 3][self.id] == -1
            and state["history"][itr - 2][self.id] == 1
            and state["history"][itr - 1][self.id] == -1
        ):
            self.tft_check += 2
            self.buffer += 1
            return 1

        if state["history"][itr - 1][op_id] == 1:
            return 1

        if state["history"][itr - 1][op_id] == -1:
            if self.coop_streak > 10:
                self.error_forgiveness -= 1
                self.buffer += 1
                return 1

            if self.zero_streak > 3 and self.forgiveness > 0:
                self.forgiveness -= 1
                self.buffer += 1
                return 1

            if self.op_zero_count > 2 and self.zero_streak == 0:
                return 1
            return -1
        # endregion

    