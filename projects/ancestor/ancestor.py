import unittest


class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

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

def earliest_ancestor(ancestors, starting_node):    
    queue = Queue()
    visited = {}

    for edge in ancestors:
        if edge[1] not in visited:
            visited[edge[1]] = set()
        visited[edge[1]].add(edge[0])

    if starting_node in visited:
        queue.enqueue(visited[starting_node])
    else:
        return -1

    while queue:
        current_path = queue.dequeue()
        starting_node = min(current_path)
        if starting_node not in visited:
            return starting_node
        else:
            queue.enqueue(visited[starting_node])
    
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    test_result = [10, -1, 10, -1, 4, 10, 4, 4, 4, -1, -1]
    
    for i in range(1, 12):
        print(earliest_ancestor(test_ancestors, i))
    
    class Test(unittest.TestCase):
        def test_earliest_ancestor(self):
            i = 1
            for n in test_result:
                self.assertEqual(earliest_ancestor(test_ancestors, i), n)
                i += 1

    unittest.main()