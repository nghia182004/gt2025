import numpy as np
from collections import defaultdict

class Graph:
    def __init__(self, edges):
       
        self.V = max(max(edge[0], edge[1]) for edge in edges)
        
        
        self.graph = np.zeros((self.V, self.V))
        for edge in edges:
            self.graph[edge[0]-1][edge[1]-1] = edge[2]
            self.graph[edge[1]-1][edge[0]-1] = edge[2]  
            
    def prim_mst(self, root):
        
        parent = [-1] * self.V
        key = [float('inf')] * self.V
        mst_set = [False] * self.V
        
       
        key[root-1] = 0
        
        for _ in range(self.V):
            
            min_key = float('inf')
            min_index = -1
            for v in range(self.V):
                if not mst_set[v] and key[v] < min_key:
                    min_key = key[v]
                    min_index = v
                    
            if min_index == -1:  
                continue
                    
            
            mst_set[min_index] = True
            
            
            for v in range(self.V):
                if (self.graph[min_index][v] > 0 and 
                    not mst_set[v] and 
                    self.graph[min_index][v] < key[v]):
                    key[v] = self.graph[min_index][v]
                    parent[v] = min_index
        
       
        mst_edges = []
        total_weight = 0
        for i in range(self.V):
            if parent[i] != -1:
                weight = int(self.graph[i][parent[i]])  
                mst_edges.append((parent[i]+1, i+1, weight))
                total_weight += weight
                
        return mst_edges, total_weight
    
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]
    
    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)
        
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1
            
    def kruskal_mst(self):
       
        edges = []
        for i in range(self.V):
            for j in range(i+1, self.V):
                if self.graph[i][j] > 0:
                    edges.append((i+1, j+1, int(self.graph[i][j])))  
                    
        
        edges.sort(key=lambda x: x[2])
        
       
        parent = list(range(self.V))
        rank = [0] * self.V
        
        
        mst_edges = []
        total_weight = 0
        
        edge_count = 0
        i = 0
        while edge_count < self.V - 1 and i < len(edges):
            u, v, w = edges[i]
            x = self.find(parent, u-1)
            y = self.find(parent, v-1)
            
            if x != y:
                self.union(parent, rank, u-1, v-1)
                mst_edges.append(edges[i])
                total_weight += w
                edge_count += 1
            i += 1
                
        return mst_edges, total_weight

def main():
    
    G = [
        [1, 5, 1], [1, 2, 4], [1, 7, 2], [2, 3, 7],
        [2, 6, 5], [3, 4, 1], [3, 6, 8], [4, 6, 6],
        [4, 7, 4], [4, 8, 3], [5, 6, 9], [5, 7, 10],
        [6, 9, 2], [7, 9, 8], [8, 9, 1], [7, 7, 2]
    ]
    
    
    graph = Graph(G)
    
    
    root = int(input("Enter root node for Prim's algorithm: "))
    
    
    prim_edges, prim_weight = graph.prim_mst(root)
    kruskal_edges, kruskal_weight = graph.kruskal_mst()
    
    
    print("\nPrim's MST starting from node", root)
    print("Edges in MST:", prim_edges)
    print("Total weight:", prim_weight)
    
    print("\nKruskal's MST")
    print("Edges in MST:", kruskal_edges)
    print("Total weight:", kruskal_weight)

if __name__ == "__main__":
    main()