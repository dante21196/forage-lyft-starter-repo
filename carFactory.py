
from car import Car

from .battery import Spindler
from .battery import Nubbin
from .engine import sternman_engine
from .engine import willoughby_engine
from .engine import  capulet_engine


class carFactory():
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        engine=capulet_engine(current_mileage,last_service_mileage)
        battery=Spindler(current_date,last_service_date)
        car = Car(engine,battery)
        return  car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        engine = willoughby_engine(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        engine = willoughby_engine(current_mileage, last_service_mileage)
        battery = Nubbin(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        engine = capulet_engine(current_mileage, last_service_mileage)
        battery = Nubbin(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_calliope(current_date, last_service_date, warning_light_is_on)
        engine = sternman_engine(warning_light_is_on)
        battery = Spindler(current_date, last_service_date)
        car = Car(engine, battery)
        return car