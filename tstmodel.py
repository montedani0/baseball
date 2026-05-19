from model.model import Model

mymodel = Model()
mymodel.getTeamsOfYear(2012)
mymodel.creaGrafo()
print("Grafo creato")
nodi, archi = mymodel.getGraphDetails()
print(f"Il grafo ha {nodi} e {archi} archi")