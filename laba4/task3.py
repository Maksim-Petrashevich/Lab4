class Vehicle:
    name = "NULL"
    def __init__(self, time, cost, distance, city_1, city_2):
        self.time=time
        self.cost=cost
        self.distance=distance
        self.city_1=city_1
        self.city_2=city_2
    def journey(self):
        pass

class Plain(Vehicle):
    def journey(self):
        self.name= "Самолет"

class Train(Vehicle):
    def journey(self):
        self.name= "Поезд"

class Car(Vehicle):
    def journey(self):
        self.name= "Автомобиль"

if __name__=='__main__':
    plain={"time": 1.5, "cost": 100, "distance": 675, "city_1": "Минск", "city_2": "Москва"}
    train={"time": 7, "cost": 85, "distance": 700, "city_1": "Минск", "city_2": "Москва"}
    car={"time": 9, "cost": 165, "distance": 720, "city_1": "Минск", "city_2": "Москва"}
    workplain=Plain(**plain)
    workplain.journey()
    worktrain=Train(**train)
    worktrain.journey()
    workcar=Car(**car)
    workcar.journey()
    vehicle=[workplain, worktrain, workcar]
    best_time=float('inf')
    best_cost=float('inf')
    best_vehicle = None
    for vehicle in vehicle:
        if vehicle.time < best_time or (vehicle.time == best_time and vehicle.cost< best_cost):
            best_time=vehicle.time
            best_cost=vehicle.cost
            best_vehicle=vehicle
print(f"Cамый быстрой и экономичной поездкой будет на {best_vehicle.name}. За {best_time} часа. Стоимостью - {best_cost} BYR")

