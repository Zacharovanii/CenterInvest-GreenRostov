from enum import Enum


emission_factors_shopping = {
        "Яйца": 4.0,
        "Рыба": 6.5,
        "Заправить автомобиль": 8.0
    }

emission_factors_activity = {
        "Транспорт (общественный)": 10.0,
        "Транспорт (воздушный)": 25.0
    }

class Emission_factors_shopping(Enum):
    eggs = "Яйца"
    fish = "Рыба"
    Refuel = "Заправить автомобиль"
    

class Emission_factors_activity(Enum):
    public_transport = "Транспорт (общественный)"
    air_transport = "Транспорт (воздушный)"