from pelicula import Pelicula

if __name__ == "__main__":

    pelicula1 = Pelicula(6249, "El robo del siglo", 114, "Roger Donaldson", False)
    pelicula2 = Pelicula(3848, "Contrarreloj", 91, "Nimród Antal", False)
    pelicula3 = Pelicula(6249, "Duro de matar", 131, "John McTiernan", True)
    
    print(pelicula1)
    print(pelicula2)
    print(pelicula3)

    print(pelicula1.devolver())
    print(pelicula2.prestar())
    print(pelicula3.prestar())

    print(pelicula1.costo_reproduccion(255))
    print(pelicula2.costo_reproduccion(255))
    print(pelicula3.costo_reproduccion(255))
    
    print("¿pelicula1 y pelicula2 tienen el mismo ID/Codigo?", pelicula1 == pelicula2)
    print("¿pelicula1 y pelicula3 tienen el mismo ID/Codigo?", pelicula1 == pelicula3)