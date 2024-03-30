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

agents = [
	RandomAgent(2, 0.2),
	TitForTatAgent(2),
	TitForTatDelayAgent(2),
	PreemptErrorAgent(2, 3),
	VSSAgent(2),
	GeneticAgent(2, l),
	CooperateAgent(2),
	DefectAgent(2),
]

a = b = 0
for agent in agents:
	x, y = playoff(Agent(1), agent)
	print(x, y)

	a += x
	b += y

print(f'{a / len(agents):.2f} {b / len(agents):.2f}')
