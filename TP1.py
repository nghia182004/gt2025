def check_path(graph, start, end):
    
    visited = set()
    stack = [start]

    while stack:
        current = stack.pop()
        if current == end:
            return True
        if current not in visited:
            visited.add(current)
            stack.extend(graph.get(current, []))

    return False

def main():
    # Initilize the graph we want to check in adjacency list
    graph = {
        1: [2],
        2: [1, 5],
        5: [2],
        3: [6],
        6: [3, 4, 7],
        7: [4, 6],
        4: [6, 7]
    }
#     Edge List:
#     1: 1 2 
#     2: 2 5
#     3: 3 6
#     4: 6 4
#     5: 6 7
#     6: 4 7

    # Take input from user 
    start_node = int(input("Start node: "))
    end_node = int(input("End node: "))
    print(f"Is path exists : {check_path(graph, start_node, end_node)}")

if __name__ == "__main__":
    main()

