"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.vertices:
            pass
        else:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print('Only one vertice in graph')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if self.vertices[vertex_id]:
            return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # need a queue for where we are visiting and a set to place those that we have
        # already visited 
        
        vertex_queue = Queue()
        vertex_queue.enqueue(starting_vertex)

        vertex_visited = set()

        # while our vertex queue is greater than one we will continue to traverse our nodes
        while vertex_queue.size() > 0:

            # dequeue our starting vertex to a variable
            current = vertex_queue.dequeue()

            # check if the current vertex is in our visited
            if current not in vertex_visited:

                # print out the vertex
                print(current)

                # add vertex to visited if not already in there.
                vertex_visited.add(current)

                # check all the existing neighbors for the current vertex, and add them to the queue
                for i in self.get_neighbors(current):
                    vertex_queue.enqueue(i)
            
        # once there are no vertices in our queue we will return our list of visited vertices
        return vertex_visited

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # use a stack for depth traversion
        vertex_stack = Stack()
        vertex_stack.push(starting_vertex)

        vertex_visited = set()

        while vertex_stack.size() > 0:
            
            current = vertex_stack.pop()

            if current not in vertex_visited:
                print(current)
                vertex_visited.add(current)

                for i in self.get_neighbors(current):
                    vertex_stack.push(i)
        
        return vertex_visited



    def dft_recursive(self, starting_vertex, vertex_visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # added a parameter vertex_visited and set to an empty set()

        # if the starting vertex is not in the vertex_visited set then print and add 
        # that vertex to the set
        if starting_vertex not in vertex_visited:
            print(starting_vertex)
            vertex_visited.add(starting_vertex)

            # for each neighbor of the starting vertex run the dft_recursive method. 
            for i in self.get_neighbors(starting_vertex):
                self.dft_recursive(i, vertex_visited)

        


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # start a queue that is a list of paths.
        paths = Queue()
        paths.enqueue([starting_vertex])

        while paths.size() > 0:
            # dequeue the path so we can add nodes to the path
            path = paths.dequeue()
            # current path is the last node in the path
            current_vertex = path[-1]

            if current_vertex == destination_vertex:
                return path
            
            # otherwise initialize new paths for each neighbor
            else:
                for i in self.get_neighbors(current_vertex):
                    new_path = path + [i]
                    paths.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

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
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
