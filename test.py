__author__ = 'Whitney'

#this code works in terminal but not in pycharm. Not sure why...
#last updated May 17 2012 17:47

from pygraphviz import *

G = AGraph()
#G.layout('dot')
G.add_edge('a','b',penwidth=4)
G.add_edge('a','c',penwidth=2)


G.draw('/Users/Whitney/Dropbox/SStalk/test.png',prog='dot')
