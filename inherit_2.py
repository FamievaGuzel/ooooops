class Acellularia:
    pass

class Cellularia:
    pass

class Prokaryota(Cellularia):
    pass

class Eukaryota(Cellularia):
    pass

class Unicellularia(Eukaryota):
    pass

class Fungi(Eukaryota):
    pass

class Plantae(Eukaryota):
    pass

class Animalia(Eukaryota):
    pass

# Ваш код

print(issubclass(Prokaryota, Cellularia), issubclass(Eukaryota, Cellularia))
print(issubclass(Unicellularia, Eukaryota), issubclass(Fungi, Eukaryota),
      issubclass(Plantae, Eukaryota), issubclass(Animalia, Eukaryota))
print(issubclass(Animalia, Cellularia), issubclass(Acellularia, Cellularia),
      issubclass(Fungi, Prokaryota), issubclass(Eukaryota, Prokaryota))