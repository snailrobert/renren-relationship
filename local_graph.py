# -*- coding: utf-8 -*-

import random
import cPickle as pickle
import subprocess
import numpy as np
import time


import networkx as nx
#from networkx import write_dot
#from networkx.drawing.nx_agraph import write_dot()
import json

from renren import FriendsStore, RenRenRelationShip


RENREN_FILE = 'renren_data'

def _dump(data):
    with open(RENREN_FILE, 'w') as f:
        pickle.dump(data, f, 2)
        
def getAllFriends(sLevel):
    from utils import get_accounts
    r = RenRenRelationShip(*get_accounts())
        
    print 'collect friends'
    data = r.collect_friends(level=sLevel)
    if sLevel == 2:
       _dump(data)
    return data

        
def _load(operate):
    if operate == 'relationShip':
       try:
           with open(RENREN_FILE, 'r') as f:
            return pickle.load(f)
       except IOError:
           return getAllFriends(2)
    else:
       return getAllFriends(1)

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        #if isinstance(obj, time):
        #    return obj.__str__()
        else:
            return super(NpEncoder, self).default(obj)

class GraphAnalysis(object):
    def __init__(self):
        self.G = nx.Graph()
        self.min_node_size = 5
        self.max_node_size = 10

    def import_data(self, fs_list, min_keep=20):
        print 'fs len='+str(len(fs_list))
        for fs in fs_list:
            #print 'uid='+fs.uid+', fiends='+list(fs.friends)[0]
            self.G.add_node(fs.uid, lv=fs.level)
            if fs.friends:
                edges = [(fs.uid, u) for u in fs.friends]
                self.G.add_edges_from(edges)
                
                
        # 删掉level 2点，否则最后生成的图片点重叠在一起，看不清
        for n in list(self.G.nodes()):
            if self.G.node[n]['lv'] == 2:
                self.G.remove_node(n)
                

        self.clear_nodes()
        self.degree = nx.degree(self.G)
        print 'node count='+str(len(list(self.degree)))
        self.max_degree_value = max(max(list(self.degree)))
        print 'max degree value='+self.max_degree_value
        self.max_degree_value_floated = float(self.max_degree_value)
        
        
        
    def _clear_nodes(self):
        need_clear = False
        for n in list(self.G.nodes()):
            if self.G.degree(n) < 2:
                self.G.remove_node(n)
                need_clear = True
                
        return need_clear
    
    
    def clear_nodes(self):
        while self._clear_nodes():
            pass
                
                
                
    def one_node_size(self, n):
        d = self.degree[n]
        d = d / self.max_degree_value_floated * self.max_node_size
        if d < self.min_node_size:
            d = self.min_node_size
        return d
        
                
    
    def get_node_size(self, nodes):
        return [self.one_node_size(n) for n in nodes]
    
    
    def one_node_color(self, n):
        d = self.degree[n]
        if d > self.max_degree_value / 2:
            _range = [0.5, 0.8]
        else:
            _range = [0.8, 1.0]
            
        _make = lambda: random.uniform(*_range)
        _love = _make
        _ohyes = _make
        
        return (_make(), _love(), _ohyes())
    
    
    
    def get_node_color(self, nodes):
        return [self.one_node_color(n) for n in nodes]
            
        


    def save(self, f='result.png', it=55):
        import matplotlib.pyplot as plt
        
        pos = nx.spring_layout(self.G, iterations=it)
        
        nx.draw_networkx_edges(self.G, pos, alpha=0.1)
        
        nx.draw_networkx_nodes(
            self.G,
            pos,
            node_size = self.get_node_size(self.G.nodes()),
            node_color = self.get_node_color(self.G.nodes()),
            alpha = 0.8,
        )
        
        plt.axis('off')
        plt.savefig(f, dpi=200)
        plt.clf()




class DrawGraphviz(GraphAnalysis):
    COLORS = [
        '#F20010', '#FC4292', '#B94C4A', '#D19D39', '#A79D0F', '#A65FCC',
        '#9470E7', '#19CD1D', '#1DDF9A', '#52A79F', '#24B5D9', '#2080DC',
    ]
    
    def __init__(self):
        super(DrawGraphviz, self).__init__()
        self.min_node_size = 0.05
        self.max_node_size = 0.2
        
        
        
    def one_node_color(self, n):
        d = self.degree[n]
        for index, color in enumerate(self.COLORS):
            if d * (index+1) >= self.max_degree_value:
                return color
        return color
        
        
        
    def save(self, f='result.png'):
        node_attr_template = {
            'sharp': "point",
            'color': "",
            'style': "filled",
            'width': 0.1,
            'height': 0.1,
            'fixedsize': "true",
            'label': "",
        }
        
        
        
        for n in self.G.nodes():
            attr = node_attr_template.copy()
            attr['width'] = self.one_node_size(n)
            attr['height'] = attr['width']
            attr['color'] = self.one_node_color(n)
            
            #self.G.node[n] = attr
            self.G.node[n].update(attr)
            
            edges = self.G.edges(n)
            #edges.update(self.G.edges[n])
            #for ed in edges:
                #self.G.edges[n][ed] = {'color': '{0}22'.format(attr['color'])}
                #self.G.edges[n, ed]['color'] = '{0}22'.format(attr['color'])
                #self.G.edges[n, ed]['color'] = 'green'
                
        
        DOT_FILE = '_renren.dot'
        #nx.write_dot(self.G, DOT_FILE)
        write_dot(self.G, DOT_FILE)
        pipe = subprocess.PIPE
        
        graphviz_command = ['dot']
        graphviz_command.append(DOT_FILE)
        graphviz_command.extend(['-Tpng', '-Kneato', '-o'])
        graphviz_command.append(f)
        
        p = subprocess.Popen(graphviz_command, stdin=pipe, stdout=pipe, stderr=pipe)
        ret_code = p.wait()
        if ret_code !=0 :
            _, ret_error_msg = p.communicate()
            raise Exception(ret_error_msg)



if __name__ == '__main__':
    from networkx.drawing.nx_pydot import write_dot,read_dot
    #operate: 'getAllFriends'/'relationShip'
    operate = 'relationShip'
    data = _load(operate)
    if operate == 'relationShip':
      g = DrawGraphviz()
      g.import_data(data)
      g.save()

