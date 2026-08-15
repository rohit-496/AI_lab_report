import networkx as nx

G = nx.DiGraph()

# Semantic network
G.add_edge("Sparrow", "Bird", relation="is-a")
G.add_edge("Bird", "Animal", relation="is-a")
G.add_edge("Bird", "Wings", relation="has")
G.add_edge("Bird", "Fly", relation="can")
G.add_edge("Animal", "Move", relation="can")

# Display relationships
print("Semantic Network:")
for u, v, d in G.edges(data=True):
    print(f"{u} --[{d['relation']}]--> {v}")

# Inference: Sparrow is a Bird, so it inherits Bird's properties
print("\nInferred properties of Sparrow:")
for u, v, d in G.out_edges("Bird", data=True):
    if d["relation"] in ["has", "can"]:
        print(f"Sparrow --[{d['relation']}]--> {v}")