"""
No modules added
"""
class Musician:
    """
    This class creates an object called musician
    """
    def __init__(self, name: str = "", fee: int = 0, age: int = 20):
        self.name = name
        self.fee = fee
        self.age = age

    def __str__(self):
        return f'Musician {self.name} needs to be paid {self.fee}₴, is {self.age} y.o.'

    def __repr__(self):
        return f'Musician({self.name}, {self.fee}, {self.age})'

class MusicFestival:
    """
    This class creates an object called music festival,
    which would include list of musicians and calculate total fee for them.
    """
    def __init__(self, list_of_musicians: list, max_budget: int = 0):
        self.max_budget = max_budget
        self.musicians = []
        for musician in list_of_musicians:
            if self.get_total_fee() <= self.max_budget:
                self.musicians.append(musician)
            else:
                print(f'{musician.name} was not added to the festival because of budget issues')

    def __str__(self):
        return f'Music Festival has max budget which equals to {self.max_budget}'

    def __repr__(self):
        return f'MusicFestival({self.max_budget})'

    def add_musician(self, musician):
        """
        This method adds musicians in list of musicians of the festival
        """
        if self.get_total_fee() + musician.fee <= self.max_budget:
            self.musicians.append(musician)
            print(f"{musician.name} was added to the festival")
            print(f"Now total fee is equal to {self.get_total_fee()}")
        else:
            print(f"{musician.name} was not added to the festival because of budget issues")

    def remove_musician(self, musician):
        """
        This method removes musicians from the list of musicians of the festival
        """
        if musician in self.musicians:
            self.musicians.remove(musician)
            print(f"{musician.name} was removed from the festival")
            print(f"Now total fee is equal to {self.get_total_fee()}")
        else:
            print(f"{musician.name} was not found to be added before")

    def get_total_fee(self):
        """
        This method returns the amount of money that would be spent on musicians
        """
        return sum(musician.fee for musician in self.musicians)

def print_info(*args):
    """
    This function prints everything it gets
    """
    for element in args:
        print(element)

def main():
    """
    This function runs on the program
    """
    musician_ivo_bobul = Musician("Ivo Bobul", 20000, 70)
    musician_oleg_vinnik = Musician("Oleg Vinnik", 40000, 50)
    musician_pavlo_zibrov = Musician("Pavlo Zibrov", 15000, 66)

    list_of_musicians = [musician_ivo_bobul, musician_oleg_vinnik]

    festival = MusicFestival(50000, list_of_musicians)

    festival.add_musician(musician_pavlo_zibrov)

    festival.remove_musician(musician_oleg_vinnik)

    print_info(musician_ivo_bobul, musician_oleg_vinnik, musician_pavlo_zibrov, festival)

main()
