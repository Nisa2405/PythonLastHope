class Film:
    def __init__(self, titel="", erscheinungsjahr=0):
        self.titel = titel
        self.erscheinungsjahr = erscheinungsjahr
        self.__genres = set()

#Methoden:
    def add_genre(self,genre):
        self.__genres.add(genre)

    def remove_genre(self,genre):
        self.__genres.remove(genre)

    def genre(self):
        return set(self.__genres)
        
f1= Film("Coraline")
f1.add_genre("Animation")
f1.add_genre("Grusel")
f1.remove_genre("Animation")

print(f1.genre())
