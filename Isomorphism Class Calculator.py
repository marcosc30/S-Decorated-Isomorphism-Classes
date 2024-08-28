import networkx as nx
from math import comb

def are_equivalent(graph, u, v) -> bool:
    # Check if vertices exist in the graph
    if u in graph.nodes and v in graph.nodes:
        #check degrees are the same
        if graph.degree(u) != graph.degree(v):
            return False
        # Get subgraph of neighbors of u
        neighbors_u = graph.subgraph(graph.neighbors(u))
        # Get subgraph of neighbors of v
        neighbors_v = graph.subgraph(graph.neighbors(v))
        # Check if the subgraphs are isomorphic
        return nx.is_isomorphic(neighbors_u, neighbors_v)

    else:
        raise ValueError("Vertices do not exist in the graph.")
    
def s_decorated_isomorphism_classes(n: int, size_of_s: int):
    # Generate all possible graphs with n vertices
    all_representative_graphs = list(nx.nonisomorphic_trees(n))

    # Iterate over all possible graphs
    running_iso_classes = 0
    for graph in all_representative_graphs:
        #pick a vertex that is unmarked
        running_core_iso_classes = 1
        marked_vertices = []
        for vertex in graph.nodes:
            if vertex not in marked_vertices:
                marked_vertices.append(vertex)
                equal_vertices = [vertex]
                for other_vertex in graph.nodes:
                    if other_vertex not in marked_vertices:
                        if are_equivalent(graph, vertex, other_vertex):
                            equal_vertices.append(other_vertex)
                            marked_vertices.append(other_vertex)
                size_of_beta = len(equal_vertices)
                result = comb(size_of_s + size_of_beta - 1, size_of_beta)
                running_core_iso_classes *= result
        running_iso_classes += running_core_iso_classes
    
    return running_iso_classes

def optimized_s_decorated_isomorphism_classes(n: int, size_of_s: int):
    #  Generate all possible graphs with n vertices
    all_representative_graphs = list(nx.nonisomorphic_trees(n))

    # Iterate over all possible graphs
    running_iso_classes = 0
    while all_representative_graphs:
        graph = all_representative_graphs[0]
        o = 1
        if nx.complement(graph) in all_representative_graphs:
            all_representative_graphs = all_representative_graphs.remove(graph).remove(nx.complement(graph))
            o = 2
        else:
            all_representative_graphs = all_representative_graphs.remove(graph)
        #pick a vertex that is unmarked
        running_core_iso_classes = 1
        marked_vertices = []
        for vertex in graph.nodes:
            if vertex not in marked_vertices:
                marked_vertices.append(vertex)
                equal_vertices = [vertex]
                for other_vertex in graph.nodes:
                    if other_vertex not in marked_vertices:
                        if are_equivalent(graph, vertex, other_vertex):
                            equal_vertices.append(other_vertex)
                            marked_vertices.append(other_vertex)
                size_of_beta = len(equal_vertices)
                result = comb(size_of_s + size_of_beta - 1, size_of_beta)
                running_core_iso_classes *= result
        running_iso_classes += o * running_core_iso_classes
    
    return running_iso_classes

# Print the number of isomorphism classes
print("Number of tree isomorphism classes, n = 2, |S| = 1:", optimized_s_decorated_isomorphism_classes(2, 1))
print("Number of tree isomorphism classes, n = 3, |S| = 2:", optimized_s_decorated_isomorphism_classes(3, 2))
print("Number of tree isomorphism classes, n = 3, |S| = 3:", optimized_s_decorated_isomorphism_classes(3, 3))
print("Number of tree isomorphism classes, n = 3, |S| = 4:", optimized_s_decorated_isomorphism_classes(3, 4))
print("Number of tree isomorphism classes, n = 4, |S| = 4:", optimized_s_decorated_isomorphism_classes(4, 4))
print("Number of tree isomorphism classes, n = 4, |S| = 7:", optimized_s_decorated_isomorphism_classes(4, 7))
print("Number of tree isomorphism classes, n = 5, |S| = 3:", optimized_s_decorated_isomorphism_classes(5, 3))
print("Number of tree isomorphism classes, n = 5, |S| = 5:", optimized_s_decorated_isomorphism_classes(5, 5))
print("Number of tree isomorphism classes, n = 6, |S| = 6:", optimized_s_decorated_isomorphism_classes(6, 6))
print("Number of tree isomorphism classes, n = 6, |S| = 15:", optimized_s_decorated_isomorphism_classes(6, 15))
print("Number of tree isomorphism classes, n = 7, |S| = 7:", optimized_s_decorated_isomorphism_classes(7, 7))
print("Number of tree isomorphism classes, n = 8, |S| = 8:", optimized_s_decorated_isomorphism_classes(8, 8))
print("Number of tree isomorphism classes, n = 9, |S| = 6:", optimized_s_decorated_isomorphism_classes(9, 6))
print("Number of tree isomorphism classes, n = 9, |S| = 9:", optimized_s_decorated_isomorphism_classes(9, 9))
print("Number of tree isomorphism classes, n = 10, |S| = 10:", optimized_s_decorated_isomorphism_classes(10, 10))
print("Number of tree isomorphism classes, n = 10, |S| = 100:", optimized_s_decorated_isomorphism_classes(10, 100))
print("Number of tree isomorphism classes, n = 18, |S| = 20:", optimized_s_decorated_isomorphism_classes(17, 20))

# only did it for trees but using pynauty this exact process is extendable to all graphs, granted you have to slightly adjust representation of graphs for however pynauty does it