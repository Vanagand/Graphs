import unittest
import sys
import io
from graph import Graph

class Test(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

        self.graph.add_vertex(1)
        self.graph.add_vertex(2)
        self.graph.add_vertex(3)
        self.graph.add_vertex(4)
        self.graph.add_vertex(5)
        self.graph.add_vertex(6)
        self.graph.add_vertex(7)
        
        self.graph.add_edge(5, 3)
        self.graph.add_edge(6, 3)
        self.graph.add_edge(7, 1)
        self.graph.add_edge(4, 7)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(7, 6)
        self.graph.add_edge(2, 4)
        self.graph.add_edge(3, 5)
        self.graph.add_edge(2, 3)
        self.graph.add_edge(4, 6)

    def test_vertices(self):
        vertices = {
          1: {2},
          2: {3, 4},
          3: {5},
          4: {6, 7}, 
          5: {3},
          6: {3},
          7: {1, 6}
        }
        self.assertDictEqual(self.graph.vertices, vertices)

    def test_bft(self):
        bft = [
            "Visited 1\nVisited 2\nVisited 3\nVisited 4\nVisited 5\nVisited 6\nVisited 7\n",
            "Visited 1\nVisited 2\nVisited 3\nVisited 4\nVisited 5\nVisited 7\nVisited 6\n",
            "Visited 1\nVisited 2\nVisited 3\nVisited 4\nVisited 6\nVisited 7\nVisited 5\n",
            "Visited 1\nVisited 2\nVisited 3\nVisited 4\nVisited 6\nVisited 5\nVisited 7\n",
            "Visited 1\nVisited 2\nVisited 3\nVisited 4\nVisited 7\nVisited 6\nVisited 5\n",
            "Visited 1\nVisited 2\nVisited 3\nVisited 4\nVisited 7\nVisited 5\nVisited 6\n",
            "Visited 1\nVisited 2\nVisited 4\nVisited 3\nVisited 5\nVisited 6\nVisited 7\n",
            "Visited 1\nVisited 2\nVisited 4\nVisited 3\nVisited 5\nVisited 7\nVisited 6\n",
            "Visited 1\nVisited 2\nVisited 4\nVisited 3\nVisited 6\nVisited 7\nVisited 5\n",
            "Visited 1\nVisited 2\nVisited 4\nVisited 3\nVisited 6\nVisited 5\nVisited 7\n",
            "Visited 1\nVisited 2\nVisited 4\nVisited 3\nVisited 7\nVisited 6\nVisited 5\n",
            "Visited 1\nVisited 2\nVisited 4\nVisited 3\nVisited 7\nVisited 5\nVisited 6\n"
        ]

        stdout_ = sys.stdout
        sys.stdout = io.StringIO()
        self.graph.bft(1)
        output = sys.stdout.getvalue()

        self.assertIn(output, bft)

        sys.stdout = stdout_  # Restore stdout

    def test_dft(self):
        dft = [
            "Visited 1\nVisited 2\nVisited 3\nVisited 5\nVisited 4\nVisited 6\nVisited 7\n",
            "Visited 1\nVisited 2\nVisited 3\nVisited 5\nVisited 4\nVisited 7\nVisited 6\n",
            "Visited 1\nVisited 2\nVisited 4\nVisited 7\nVisited 6\nVisited 3\nVisited 5\n",
            "Visited 1\nVisited 2\nVisited 4\nVisited 6\nVisited 3\nVisited 5\nVisited 7\n"
        ]

        stdout_ = sys.stdout
        sys.stdout = io.StringIO()
        self.graph.dft(1)
        output = sys.stdout.getvalue()

        self.assertIn(output, dft)

        sys.stdout = stdout_  # Restore stdout

    def test_dft_recursive(self):
        dft = [
            "Visited 1\nVisited 2\nVisited 3\nVisited 5\nVisited 4\nVisited 6\nVisited 7\n",
            "Visited 1\nVisited 2\nVisited 3\nVisited 5\nVisited 4\nVisited 7\nVisited 6\n",
            "Visited 1\nVisited 2\nVisited 4\nVisited 7\nVisited 6\nVisited 3\nVisited 5\n",
            "Visited 1\nVisited 2\nVisited 4\nVisited 6\nVisited 3\nVisited 5\nVisited 7\n"
        ]

        stdout_ = sys.stdout
        sys.stdout = io.StringIO()
        self.graph.dft_recursive(1)
        output = sys.stdout.getvalue()

        self.assertIn(output, dft)

        sys.stdout = stdout_  # Restore stdout

    def test_bfs(self):
        bfs = [1, 2, 4, 6]
        self.assertListEqual(self.graph.bfs(1, 6), bfs)

    def test_dfs(self):
        dfs = [
            [1, 2, 4, 6],
            [1, 2, 4, 7, 6]
        ]
        self.assertIn(self.graph.dfs(1,6), dfs)

    def test_dfs_recursive(self):
        dfs = [
            [1, 2, 4, 6],
            [1, 2, 4, 7, 6]
        ]
        self.assertIn(self.graph.dfs_recursive(1,6), dfs)

if __name__ == '__main__':
    unittest.main()
