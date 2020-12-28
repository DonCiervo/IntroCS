import check50
import check50.py

#check50 fau-is/IntroCS/PyGraphsTrees/Network --local

check50.include('network.py')
network = check50.py.import_('network.py')

@check50.check()
def exists():
    """network.py exists"""
    check50.exists("network.py")

@check50.check(exists)
def add_vertex():
    """adds vertex"""
    n = network.Graph()
    n.add_vertex('A')
    if 'A' not in n:
        raise check50.Failure("Expected add Vertex")

@check50.check(add_vertex)
def add_edge():
    """adds weighted edges"""
    Vertices = ['A', 'B', 'C', 'D']
    Edges = ['AB2', 'AC3', 'BD2', 'CB4']
    n = network.Graph()
    for vertex in Vertices:
        n.add_vertex(vertex)
    for edge in Edges:
        n.add_edge(edge[:1], edge[1], int(edge[2:]))

    #Edges outgoing A
    if ('B', 2) not in n['A'] and ('C', 3) not in n['A']:
        raise check50.Failure("Edges A->B w:2 and A->C w:3 (in requested format)", n['A'])
    #Edges outgoing B
    if ('A', 2) not in n['B'] and ('D', 2) not in n['B'] and ('C', 4) not in n['B']:
        raise check50.Failure("Edges B->A w:2; B->D w:2 and B->C w:4 (in requested format)", n['B'])
    #Edges outgoing C
    if ('A', 3) in n['C'] and ('B', 4) in n['C']:
        raise check50.Failure("Edges C->A w:3 and C->B w:4 (in requested format)", n['C'])
    #Edges outgoing D
    if ('B', 2) in n['D']:
        raise check50.Mismatch("Edge D->B w:2 (in requested format)", n['D'])
