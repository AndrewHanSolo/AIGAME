import networkx as nx
import matplotlib.pyplot as plt
import Board 

G = nx.Graph()

board = Board.Board(50, 50)

H=nx.path_graph(board.x * board.y)
G.add_nodes_from(H)

nx.draw(G)
plt.show()
