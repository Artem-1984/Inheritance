# class Device:
#     def __init__(self,electricity,engine):
#         self.electricity=electricity
#         self.engine=engine
# class CoffeeMachine(Device):
#     def __init__(self,electricity,engine):
#         super().__init__(electricity,engine)
#     def action(self):
#         print(f"{self.engine}\n{self.electricity}\nУмеет варить кофе")
# class Blender(Device):
#     def __init__(self,electricity,engine):
#         super().__init__(electricity,engine)
#     def action1(self):
#         print(f"{self.engine}\n{self.electricity}\nУмеет измельчать еду")
# class MeatGrinder(Device):
#     def __init__(self,electricity,engine):
#         super().__init__(electricity,engine)
#     def action3(self):
#         print(f"{self.engine}\n{self.electricity}\nПерекручивает мясо")
#
# d1=CoffeeMachine(2.3,1.0)
# d2=Blender(1.2,2.1)
# d3=MeatGrinder(1.2,1.6)
# d1.action()
# d2.action1()
# d3.action3()


# class Ship:
#     def __init__(self,engine,boats):
#         self.engine=engine
#         self.boats=boats
# class Frigate(Ship):
#     def __init__(self,engine,boats):
#         super().__init__(engine,boats)
#     def action(self):
#         print(f"{self.engine},{self.boats},носит ядерное оружие")
# class Destroyer(Ship):
#     def __init__(self,engine,boats):
#         super().__init__(engine,boats)
#     def action1(self):
#         print(f"{self.engine},{self.boats},быстромоневренный корабль")
# class Cruiser(Ship):
#     def __init__(self,engine,boats):
#         super().__init__(engine,boats)
#     def action2(self):
#         print(f"{self.engine},{self.boats},туристический корабль")
# s1=Frigate('80 000 л.с','10шт')
# s2=Destroyer('5 200л.с','20шт')
# s3=Cruiser('11 971 л.с','100шт')
# s1.action()
# s2.action1()
# s3.action2()

class Money:
    def __init__(self,euro, dollars, rubles,cents, eurocents, kopecks):
        self._euro=euro
        self._dollars=dollars
        self._rubles=rubles
        self._cents=cents
        self._eurocents=eurocents
        self._kopecks=kopecks
    def show(self):
        return (f'Euro={self._euro}.{self._cents}\nDollars={self._dollars}.{self._eurocents}\nRubles={self._rubles}.{self._kopecks}')


manu=Money(12,13,14,15,16,17)
print(manu.show())




