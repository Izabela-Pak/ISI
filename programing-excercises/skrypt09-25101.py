from datetime import datetime

class Vehicle:
    def __init__(self, nazwa, rok_produkcji, przebieg):
        self.nazwa = nazwa
        self.przebieg = przebieg
        self.rok_produkcji = rok_produkcji

    @property
    def wiek(self):
        return datetime.now().year - self.rok_produkcji
    
    def is_old(self):
        return self.wiek > 10
    
    def is_long_mileage(self):
        return self.przebieg > 200_000


class Car:
    def __init__(self, nazwa, rok_produkcji, przebieg):
        self.nazwa = nazwa
        self.przebieg = przebieg
        self.rok_produkcji = rok_produkcji

    @property
    def wiek(self):
        return datetime.now().year - self.rok_produkcji
    
    def is_old(self):
        return self.wiek > 15
    
    def is_long_mileage(self):
        return self.przebieg > 250_000
    
class CarAfterVehicle(Vehicle):
    def __init__(self, nazwa, rok_produkcji, przebieg):
        super().__init__(nazwa, rok_produkcji, przebieg)  # Wywołanie konstruktora Vehicle


if __name__ == '__main__':
    vehicle = Vehicle("BMW", 2013, 150_000)
    car = Car("Tesla", 2020, 201_000)
    dziedziczenie = CarAfterVehicle("Fiat", 2009, 300_000)

    print("Auto z klasy Vehicle")
    print("Wiek pojazdu:", vehicle.wiek)
    print("Czy jest stary?", vehicle.is_old())
    print("Czy ma duży przebieg?", vehicle.is_long_mileage())

    print("Auto z klasy Car")
    print("Wiek pojazdu:", car.wiek)
    print("Czy jest stary?", car.is_old())
    print("Czy ma duży przebieg?", car.is_long_mileage())

    print("Auto z klasy dziedziczącej po Vehicle")
    print("Wiek pojazdu:", dziedziczenie.wiek)
    print("Czy jest stary?", dziedziczenie.is_old())
    print("Czy ma duży przebieg?", dziedziczenie.is_long_mileage())


