from copy import deepcopy
from random import choice, random, randrange
from time import time
from playoff import playoff

from strategies.genetic import GeneticAgent
# from strategies.random import RandomAgent
from strategies.tit_for_tat import TitForTatAgent
from strategies.tit_for_tat_delay import TitForTatDelayAgent
from strategies.vss import VSSAgent
from strategies.preempt_error import PreemptErrorAgent
from strategies.cooperator import CooperateAgent

def evaluate_agents(agents):
    global best_score, best_agent
    start = time()
    num_agents = len(agents)
    scores = [0] * num_agents

    for i in range(num_agents):
        for opp in opposition:
            for k in range(repetitions):
                x = playoff(GeneticAgent(1, agents[i]), opp[0](2, *opp[1:]))[0]
                scores[i] += x

        if scores[i] > best_score:
            best_score = scores[i]
            best_agent = agents[i]

    print(f'Time: {time() - start:.2f}s')
    return scores

def next_gen(agents, filter, mutation_prob):
    num_agents = len(agents)
    scores = evaluate_agents(agents)

    top_agents = []
    score_sum = 0
    for i in sorted(range(num_agents), key = lambda x: -scores[x])[:filter]:
        top_agents.append(agents[i])
        score_sum += scores[i]

    print(f'Avg surviving score: {score_sum / (repetitions * filter * len(opposition))}')
    new_agents = top_agents + [deepcopy(choice(top_agents)) for _ in range(num_agents - filter)]

    for i in range(num_agents):
        while random() < mutation_prob:
            j = randrange(len(new_agents[i]))
            new_agents[i][j] = not new_agents[i][j]
    
    return new_agents

visibility = 3
strat_len = 1 << (2 * visibility)
num_agents = min(100, 1 << strat_len)
num_generations = 30
filter = num_agents // 10
mutation_prob = 0.1
repetitions = 10

l = []
with open('out.txt', 'r') as file:
	l = eval(file.read())

opposition = [
	# RandomAgent(2, 0.5),
	(TitForTatAgent,),
	(TitForTatAgent,),
	(TitForTatAgent,),
	(TitForTatDelayAgent,),
    (PreemptErrorAgent, 3),
    (VSSAgent,),
    (GeneticAgent, l),
    (CooperateAgent,),
]

curr_gen = [[random() < 0.5 for _ in range(strat_len)] for _ in range(num_agents)]
best_agent = []
best_score = 0

for i in range(num_generations):
	print(f'Generation: {i}')
	curr_gen = next_gen(curr_gen, filter, mutation_prob)
with open('out.txt', 'w') as file:
    file.write(str(best_agent))
