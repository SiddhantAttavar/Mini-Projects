from time import time
from playoff import playoff

from strategies.tit_for_tat import TitForTatAgent
from strategies.tit_for_tat_delay import TitForTatDelayAgent
from strategies.random import RandomAgent
from strategies.preempt_error import PreemptErrorAgent
from strategies.vss import VSSAgent
from strategies.genetic import GeneticAgent
from strategies.cooperator import CooperateAgent
from strategies.defector import DefectAgent
from strategies.final_genetic import Agent

l = []
with open('out.txt', 'r') as file:
	l = eval(file.read())

repetitions = 1000

def run_tournament(agents):
	start = time()
	num_agents = len(agents)
	scores = [0] * num_agents

	for i in range(num_agents):
		for j in range(i):
			for k in range(repetitions):
				x, y = playoff(agents[i][0](1, *agents[i][2:]), agents[j][0](2, *agents[j][2:]))
				scores[i] += x
				scores[j] += y

	print(f'Time: {time() - start:.2f}s')
	return scores

agents = [
	(RandomAgent, 'random', 0.2),
	(TitForTatAgent, 'tit_for_tat', ),
	(TitForTatDelayAgent, 'tit_for_tat_delay', ),
	(PreemptErrorAgent, 'preempt_error', 3),
	(VSSAgent, 'vss', ),
	(GeneticAgent, 'genetic', l),
	(CooperateAgent, 'cooperator', ),
	(DefectAgent, 'defector', ),
	(Agent, 'final', )
]

scores = run_tournament(agents)
for i in sorted(range(len(agents)), key = lambda x: -scores[x]):
	print(f'{agents[i][1]}: {scores[i] / (repetitions * (len(agents) - 1)):.2f}')
