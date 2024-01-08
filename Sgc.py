import ast
import graphviz
import cmath  # Ajoutez cette ligne pour importer le module cmath
import inspect

def build_control_flow_graph(node, dot=None):
    if dot is None:
        dot = graphviz.Digraph(comment='The Control Flow Graph', format='png', engine='dot', graph_attr={'rankdir': 'TB'})


    dot.node(str(id(node)), str(node.__class__.__name__))

    for child_node in ast.iter_child_nodes(node):
        dot = build_control_flow_graph(child_node, dot)
        dot.edge(str(id(node)), str(id(child_node)))

    return dot

def main():
    print("Entrez les coefficients de l'équation quadratique (ax^2 + bx + c = 0):")
    a = float(input("a : "))
    b = float(input("b : "))
    c = float(input("c : "))

    # Calcul du discriminant (b^2 - 4ac)
    discriminant = b**2 - 4 * a * c

    if discriminant > 0:
        # Deux solutions réelles distinctes
        root1 = (-b + discriminant**0.5) / (2 * a)
        root2 = (-b - discriminant**0.5) / (2 * a)
        print("Deux solutions distinctes :")
        print(f"x1 = {root1}")
        print(f"x2 = {root2}")
    elif discriminant == 0:
        # Une seule solution réelle (racine double)
        root = -b / (2 * a)
        print("Une seule solution (racine double) :")
        print(f"x = {root}")
    else:
        # Pas de solution réelle (solutions imaginaires/complexes)
        print("Pas de solution ")

    # Générer le graphe de contrôle
    tree = ast.parse(inspect.getsource(main))
    dot = build_control_flow_graph(tree)
    dot.render('control_flow_graph', format='png', cleanup=True)

if __name__ == "__main__":
    main()