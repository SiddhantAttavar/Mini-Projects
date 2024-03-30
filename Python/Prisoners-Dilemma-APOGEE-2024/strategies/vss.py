from agent import BaseAgent

class VSSAgent(BaseAgent):
    def __init__(self, id):
        super().__init__(id=id)
        self.zero_streak =0
        self.coop_streak=0
        self.forgiveness =4
        self.buffer=0
        self.error_forgiveness=3
        self.tft_check=0

    def next_move(self, state):
        op_id = 1 if self.id == 2 else 2
        itr = state["current_iter"]
        if itr == 1 :
            return -1
        if itr == 2 :
            return 1
        if itr == 3 :
            return -1
        if itr == 4 :
            return 1
        

        if itr >1 and state["history"][itr - 1][op_id]== -1 and state["history"][itr - 1][self.id] == -1:
            self.zero_streak+=1
        else :
            self.zero_streak=0

        if itr >1 and state["history"][itr - 1][op_id]== 1 and state["history"][itr - 1][self.id] == 1 :
            self.coop_streak+=1
        else :
            self.coop_streak=0

        if self.coop_streak >0 and self.coop_streak%10 ==0 :
            self.error_forgiveness +=1

        
        if self.tft_check>1 :
            if self.tft_check>2:
                return 1
            if state["history"][itr - 1][op_id] == -1  :
                if self.coop_streak >6:
                    self.error_forgiveness-=0.5
                    self.buffer+=1
                    return 1
                        
                if self.zero_streak > 2 and self.forgiveness >0:
                    self.forgiveness-=0.5
                    self.buffer+=1
                    return 1
                
                if self.buffer>0:
                    self.buffer-=1
                    return 1
                return -1

            return 1

        if self.buffer>0:
                    self.buffer-=1
                    return 1


        if self.tft_check <2 and itr >1 :
            if (itr == 5):
                if state["history"][itr - 4][op_id]== 1 and state["history"][itr - 3][op_id]== -1 and state["history"][itr - 2][op_id]== 1 and state["history"][itr - 1][op_id]== -1 :
                    self.tft_check+=2
                return 1

            if itr > 4 and state["history"][itr - 4][op_id]== -1 and state["history"][itr - 3][op_id]== 1 and state["history"][itr - 2][op_id]== -1 and state["history"][itr - 1][op_id]== 1 and state["history"][itr - 4][self.id]== 1 and state["history"][itr - 3][self.id]== -1 and state["history"][itr - 2][self.id]== 1 and state["history"][itr - 1][self.id]== -1 :
                self.tft_check+=1
                return 1

            if state["history"][itr - 1][op_id] ==1:
                return 1


            if state["history"][itr - 1][op_id] == -1  :
                if self.coop_streak >6:
                    self.error_forgiveness-=1
                    self.buffer+=1
                    return 1
                        
                if self.zero_streak > 2 and self.forgiveness >0:
                    self.forgiveness-=1
                    self.buffer+=1
                    return 1
                
                if self.buffer>0:
                    self.buffer-=1
                    return 1
                return -1
        
