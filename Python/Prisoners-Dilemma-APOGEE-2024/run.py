from playoff import playoff

from strategies.genetic import GeneticAgent
from strategies.final_genetic import Agent

l = []
with open('out.txt', 'r') as file:
	l = eval(file.read())

for i in range(10):
	print(*playoff(GeneticAgent(1, l), Agent(2)))
