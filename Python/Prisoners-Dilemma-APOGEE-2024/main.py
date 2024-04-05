from copy import deepcopy
from random import choice, random, randrange
from time import time
from matplotlib import pyplot as plt
from multiprocessing import Pool
from glob import glob
from importlib import import_module

from playoff import playoff

from strategies.genetic import GeneticAgent
# from strategies.random import RandomAgent
# from strategies.tit_for_tat import TitForTatAgent
# from strategies.tit_for_two_tats import TitForTwoTatsAgent
# from strategies.tit_for_tat_delay import TitForTatDelayAgent
# from strategies.vss import VSSAgent
# from strategies.preempt_error import PreemptErrorAgent
# from strategies.cooperator import CooperateAgent
# from strategies.defector import DefectAgent

def get_agent_score(agent):
    res = 0
    for opp in opposition:
        res += opp[1] * sum(
            playoff(GeneticAgent(1, agent), opp[0](2, *opp[2:]))[0] for _ in range(repetitions)
        )
    return res

def evaluate_agents(agents):
    global best_score, best_agent, process_pool
    start = time()
    num_agents = len(agents)

    scores = process_pool.map(
        get_agent_score,
        agents
    )

    best_agent = []
    best_score = 0
    for i in range(num_agents):
        if scores[i] > best_score:
            best_score = scores[i]
            best_agent = agents[i]

    print(f'Time: {time() - start:.2f}s')
    return scores

def next_gen(agents, filter, mutation_prob, upsample):
    global gen_scores, effective_opp_size
    num_agents = len(agents)
    scores = evaluate_agents(agents)

    top_agents = []
    score_sum = 0
    for i in sorted(range(num_agents), key = lambda x: -scores[x])[:filter]:
        top_agents.append(agents[i])
        score_sum += scores[i]

    avg_surv_score = score_sum / (repetitions * filter * effective_opp_size)
    gen_scores.append(avg_surv_score)
    print(f'Avg surviving score: {avg_surv_score:.2f}')
    new_agents = top_agents
    if upsample:
        new_agents.extend(deepcopy(choice(top_agents)) for _ in range(num_agents - filter))

    for i in range(num_agents):
        while random() < mutation_prob:
            j = randrange(len(new_agents[i]))
            new_agents[i][j] = not new_agents[i][j]
    
    return new_agents

visibility = 3
strat_len = 1 << (2 * visibility)
num_agents = min(100, 1 << strat_len)
num_generations = 100
filter = num_agents // 10
mutation_prob = 0.2
repetitions = 10

l = []
with open('out.txt', 'r') as file:
	l = eval(file.read())

opposition = []
for i, file in enumerate(glob('submissions/*.py')):
    module = import_module(file.replace('/', '.')[:-3])
    opposition.append((module.Agent, 1))

# opposition = [
# 	(TitForTatAgent, 5),
# 	(TitForTwoTatsAgent, 3),
# 	(TitForTatDelayAgent, 1),
#     (PreemptErrorAgent, 1, 3),
#     (VSSAgent, 1),
#     (CooperateAgent, 1),
#     (DefectAgent, 1),
# ]
effective_opp_size = sum(i[1] for i in opposition)

gen_scores = []
best_agent = []
best_score = 0

process_pool = Pool(num_agents)

# Generation 0
curr_gen = [[random() < 0.5 for _ in range(strat_len)] for _ in range(num_agents * 10)]
curr_gen = next_gen(curr_gen, num_agents, 0, False)
# curr_gen = [[random() < 0.5 for _ in range(strat_len)] for _ in range(num_agents)]

for i in range(num_generations):
    print(f'Generation: {i}')
    curr_gen = next_gen(curr_gen, filter, mutation_prob, True)

with open('out.txt', 'w') as file:
    file.write(str(best_agent))

plt.plot(gen_scores)
plt.yscale('linear')
plt.show()
