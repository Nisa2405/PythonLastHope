class Film:
    def __init__(self, titel="", erscheinungsjahr=0):
        self.titel = titel
        self.erscheinungsjahr = erscheinungsjahr

#Drei Objekte erzeugen
f1= Film("Nemo",2003)
f2= Film("Cars",2006)
f3= Film("Coraline",2009)

print(f1.titel, f1.erscheinungsjahr)
print(f2.titel, f1.erscheinungsjahr)
print(f3.titel, f1.erscheinungsjahr)
