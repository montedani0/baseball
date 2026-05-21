from model.model import Model

mymodel = Model()
mymodel.getTeamsOfYear(2012)
mymodel.creaGrafo(2012)
print("Grafo creato")
nodi, archi = mymodel.getGraphDetails()
print(f"Il grafo ha {nodi} e {archi} archi")

path, score = mymodel.getPathV2(mymodel.getRandomNode())

print(f"Trovata soluzione {len(path)} con somma pesi archi {score} ")
for p in path:
    print(p)