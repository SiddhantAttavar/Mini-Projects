from playoff import playoff
from random import choice, random, randrange
from time import time

from strategies.genetic import GeneticAgent
from strategies.random import RandomAgent
from strategies.tit_for_tat import TitForTatAgent
from strategies.nice_and_greedy import NiceAndGreedyAgent

def evaluate_agents(agents):
    start = time()
    num_agents = len(agents)
    scores = [0] * num_agents

    for i in range(num_agents):
        for opp in opposition:
            x = playoff(GeneticAgent(1, agents[i]), opp)[0]
            scores[i] += x
        scores[i] /= len(opposition)

    print(f'Time: {time() - start}')
    return scores

def next_gen(agents, filter, mutation_prob):
    num_agents = len(agents)
    scores = evaluate_agents(agents)
    print(f'Max score: {max(scores)}')

    top_agents = [agents[i] for i in sorted(range(num_agents), key = lambda x: scores[x])]
    new_agents = [choice(top_agents) for _ in range(num_agents)]

    for i in range(num_agents):
        while random() < mutation_prob:
            j = randrange(len(new_agents[i]))
            new_agents[i][j] = not new_agents[i][j]
    
    return new_agents

visibility = 2
strat_len = 1 << (2 * visibility)
num_agents = min(100, 1 << strat_len)
num_generations = 10
filter = num_agents // 10
mutation_prob = 0.1

opposition = [
	# RandomAgent(2, 0.5),
	TitForTatAgent(2),
    NiceAndGreedyAgent(2)
]

curr_gen = [[random() < 0.5 for _ in range(strat_len)] for _ in range(num_agents)]
for i in range(num_generations):
	print(f'Generation: {i}')
	curr_gen = next_gen(curr_gen, filter, mutation_prob)

print(curr_gen[0])
