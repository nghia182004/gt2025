# Implementation for connected components
# Marking vertices as visited and collecting connected vertices
def find_component(graph, vertex, visited):
    visited[vertex] = True
    component = [vertex]
    for i in range(len(graph)):
        if (graph[vertex][i] or graph[i][vertex]) and not visited[i]:
            component.extend(find_component(graph, i, visited))
    return component
# Keeps track of the visited vertices and returns the index
def get_components(graph):
    visited = [False] * len(graph)
    components = []
    for vertex in range(len(graph)):
        if not visited[vertex]:
            components.append([x + 1 for x in find_component(graph, vertex, visited)]) # The index of the first vertex is always 1
    return components

# Implementation for strongly connected components (Kosaraju's algorithm)
def find_scc(graph):
    # Visit all neighbors vertices in order and add them to the stack in reverse order
    def dfs(v, visited, stack):
        visited[v] = True
        for i in range(len(graph)):
            if graph[v][i] and not visited[i]:
                dfs(i, visited, stack)
        stack.append(v)
    
    # Reverses the direction of all edges in the graph
    def get_transpose():
        n = len(graph)
        t = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                t[i][j] = graph[j][i]
        return t
    
    # Collects 
    def collect_scc(v, visited, component):
        visited[v] = True
        component.append(v)
        for i in range(len(graph)):
            if graph[v][i] and not visited[i]:
                collect_scc(i, visited, component)
    
    
    n = len(graph)
    visited = [False] * n
    stack = []
    
    
    for v in range(n):
        if not visited[v]:
            dfs(v, visited, stack)
    
    
    graph = get_transpose()
    visited = [False] * n
    components = []
    
    
    while stack:
        v = stack.pop()
        if not visited[v]:
            component = []
            collect_scc(v, visited, component)
            
            components.append([x + 1 for x in component])
    
    return components


def get_user_matrix():
    try:
        
        n = int(input("Enter the size of the adjacency matrix (n x n): "))
        print(f"Enter the adjacency matrix ({n} x {n}):")
        print("Enter each row with spaces between numbers (0 and 1)")
        matrix = []
        
        for i in range(n):
            while True:
                
                row = list(map(int, input(f"Row {i + 1}: ").split()))
                
                if len(row) == n and all(x in [0, 1] for x in row):
                    matrix.append(row)
                    break
                print(f"Enter {n} values (0 or 1)")
        return matrix
    except ValueError:
        print("Invalid input")
        return None

def main():


 while True:
    print("\nChoose an option:")
    print("1. Use test graph")
    print("2. Input a graph")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        # Test graph(the one you gave me)
        G = [ [0, 1, 0, 1, 0, 0, 0, 0, 0], 
             [0, 0, 1, 0, 0, 1, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 0, 0, 0, 1], 
             [0, 0, 1, 1, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 1, 1, 0, 1, 0], 
             [0, 0, 1, 0, 0, 0, 0, 0, 1], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0] ]
    elif choice == '2':
        
        G = get_user_matrix()
        if G is None:
            continue
    else:
        
        break
    
    
    print("\nComponents:", get_components(G))
    print("Strongly Connected Components:", find_scc(G))
if __name__ == "__main__":
    main()    