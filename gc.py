import networkx as nx

def creer_graphe_de_controle(programme):
    """
    Crée le graphe de contrôle d'un programme.

    Args:
        programme: Le programme dont on veut créer le graphe de contrôle.

    Returns:
        Le graphe de contrôle du programme.
    """

    graphe_de_controle = nx.DiGraph()
    for i, instruction in enumerate(programme):
        graphe_de_controle.add_node(i, instruction=instruction)
    for i, instruction in enumerate(programme):
        for successeur in instruction[1:]:
            graphe_de_controle.add_edge(i, successeur)
    return graphe_de_controle

def main():
    programme = [
        ["a = 1"],
        ["b = 2"],
        ["if a < b:"],
            ["c = 3"],
        ["else:"],
            ["c = 4"],
        ["end if"],
    ]
    graphe_de_controle = creer_graphe_de_controle(programme)
    print(graphe_de_controle.nodes())

if __name__ == "__main__":
    main()