def create_adjacency_matrix(edges, n_vertices):
    
    matrix = [[0 for _ in range(n_vertices)] for _ in range(n_vertices)]
    
    for edge in edges:
        from_vertex, to_vertex = edge
        matrix[from_vertex-1][to_vertex-1] = 1
    
    return matrix

def inorder_traversal(adj_matrix, node, visited=None):
    if visited is None:
        visited = set()
    
    n = len(adj_matrix)
    
    node_idx = node - 1
    
    
    children = [i+1 for i in range(n) if adj_matrix[node_idx][i] == 1]
    
    # Check the left
    if children and not children[0] in visited:
        inorder_traversal(adj_matrix, children[0], visited)
    
   
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
    
    # Check the rest except the first
    for child in children[1:]:
        if child not in visited:
            inorder_traversal(adj_matrix, child, visited)


edges = [
    [1, 2],
    [1, 3],
    [2, 5],
    [2, 6],
    [5, 7],
    [3, 4],
    [4, 8]
]


n_vertices = max(max(edge) for edge in edges)


adj_matrix = create_adjacency_matrix(edges, n_vertices)


print("\nAdjacency Matrix:")
for row in adj_matrix:
    print(row)

default_node = 1
print("All nodes from inorder traversal: ")
inorder_traversal(adj_matrix, default_node)

start_node = int(input("\nEnter starting node: "))
print(f"Inorder traversal from node {start_node}:")
inorder_traversal(adj_matrix, start_node)