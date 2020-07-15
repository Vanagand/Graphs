"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from graph import Graph

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}


    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertices not found.")


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        q = Queue()

        # Create a set to store the visited nodes
        visited = set()

        # Init: enqueue the starting node
        q.enqueue(starting_vertex)

        # While the queue isn't empty
        while q.size() > 0:
            # Dequeue the first item
            v = q.dequeue()
            # If it's not been visited:
            if v not in visited:
                # Mark as visited (i.e. add to the visited set)
                visited.add(v)

                # Do something with the node
                print(f"Visited {v}")

                # Add all neighbors to the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        s = Stack()

        # Create a set to store the visited nodes
        visited = set()

        # Init: push the starting node
        s.push(starting_vertex)

        # While the stack isn't empty
        while s.size() > 0:
            # pop the first item
            v = s.pop()
            # If it's not been visited:
            if v not in visited:
                # Mark as visited (i.e. add to the visited set)
                visited.add(v)

                # Do something with the node
                print(f"Visited {v}")

                # Add all neighbors to the stack
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        print(f"Visited {starting_vertex}")
        visited.add(starting_vertex)
        
        for next_vertex in self.get_neighbors(starting_vertex):
            if next_vertex not in visited:
                self.dft_recursive(next_vertex, visited) 
            

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue
        queue = Queue()

        # Create a set to store the visited nodes
        visited = set()

        # Init: enqueue the starting node
        queue.enqueue([starting_vertex])

        while queue:
            current_path = queue.dequeue()
            current_vertex = current_path[-1]
            if current_vertex == destination_vertex:
                return current_path
            else:
                if current_vertex not in visited:
                    visited.add(current_vertex)
                    for neighbor in self.get_neighbors(current_vertex):
                        path = list(current_path)
                        path.append(neighbor)
                        queue.enqueue(path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack
        stack = Stack()

        # Create a set to store the visited nodes
        visited = set()

        # Init: push the starting node
        stack.push([starting_vertex])

        # While the stack isn't empty
        while stack:
            current_path = stack.pop()
            current_vertex = current_path[-1]
            if current_vertex == destination_vertex:
                return current_path
            else:
                if current_vertex not in visited:
                    visited.add(current_vertex)
                    for neighbor in self.vertices[current_vertex]:
                        path = list(current_path)
                        path.append(neighbor)
                        stack.push(path)


    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(starting_vertex)
        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path
        else:
            for neighbor in self.get_neighbors(starting_vertex):
                if neighbor not in visited:
                    current_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                    if current_path is not None:
                        return current_path
        return None 


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    
    '''
    Should print:
        {1: {2}},
        {2: {3, 4}},
        {3: {5}}
        {4: {6, 7}}
        {5: {3}},
        {6: {3}},
        {7: {1, 6}}
    '''
    # print(graph.get_neighbors(1))
    # print(graph.get_neighbors(2))
    # print(graph.get_neighbors(3))
    # print(graph.get_neighbors(4))
    # print(graph.get_neighbors(5))
    # print(graph.get_neighbors(6))
    # print(graph.get_neighbors(7))

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
