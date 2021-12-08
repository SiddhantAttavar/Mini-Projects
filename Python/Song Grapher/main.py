'''
Instructions for lyrics search:
 - Get API token from johnwmillr.com/scraping-genius-lyrics
 - Set the environment variable GENIUS_ACCESS_TOKEN with this token
 - Run this script
'''

# Import packages
import networkx as nx
from matplotlib import pyplot as plt
from math import sqrt
from lyricsgenius import Genius

# Read data
if input('Lyrics from file / Lyrics database - F/D: ').lower() == 'f':
	input('Put your song lyrics in input.txt in the same directory and press <Enter>')
	with open('input.txt') as inputFile:
		# Remove all punctuation
		song = inputFile.read()
else:
	genius = Genius()
	artistName = input('Enter artist: ')
	artist = genius.search_artist(artistName, max_songs = 5,sort = "title")
	print(artist.songs)
	title = input('Enter song title: ')
	songObj = artist.song(title)
	song = songObj.lyrics

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for c in punc:
	song.replace(c, '')
song = song.lower()

# Create words array
lines = [l.split() for l in song.splitlines()]

# Get word set
wordSet = set()
for line in lines:
	wordSet = wordSet.union(line)

# Create graph
# Add graph nodes
graph = nx.DiGraph()
graph.add_nodes_from(wordSet)

# Add edges
for line in lines:
	for i in range(1, len(line)):
		graph.add_edge(line[i - 1], line[i])

# set defaults
graph.graph['graph']={'rankdir':'TD'}
graph.graph['node']={'shape':'circle'}
graph.graph['edges']={'arrowsize':'4.0'}

# Display graph
options = {
    "node_size": 1500,
    "alpha": 0.3,
}
pos = nx.kamada_kawai_layout(graph)
nx.draw(graph, pos, **options)
nx.draw_networkx_labels(graph, pos, font_weight = "bold")
plt.show()
