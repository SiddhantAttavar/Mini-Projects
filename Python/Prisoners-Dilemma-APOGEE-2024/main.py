from playoff import playoff
from random import choice, random, randrange
from time import time
from strategies.genetic import GeneticAgent

def run_tournament(agents):
    start = time()
    num_agents = len(agents)
    scores = [0] * num_agents

    for i in range(num_agents):
        for j in range(i):
            x, y = playoff(GeneticAgent(1, agents[i]), GeneticAgent(2, agents[j]))
            scores[i] += x
            scores[j] += y
	
    print(f'Time: {time() - start}')
    return scores

def next_gen(agents, filter, mutation_prob):
    num_agents = len(agents)
    scores = run_tournament(agents)
    print(f'Max score: {max(scores)}')

    top_agents = [agents[i] for i in sorted(range(num_agents), key = lambda x: scores[x])]
    new_agents = [choice(top_agents) for _ in range(num_agents)]

    for i in range(num_agents):
        while random() < mutation_prob:
            j = randrange(len(new_agents[i]))
            new_agents[i][j] = not new_agents[i][j]
    
    return new_agents

visibility = 10
strat_len = 1 << (2 * visibility)
num_agents = min(100, 1 << strat_len)
num_generations = 100
filter = num_agents // 10
mutation_prob = 0.1

curr_gen = [[random() < 0.5 for _ in range(strat_len)] for _ in range(num_agents)]
for i in range(num_generations):
	print(f'Generation: {i}')
	curr_gen = next_gen(curr_gen, filter, mutation_prob)

print(curr_gen[0])
