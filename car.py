from abc import ABC, abstractmethod
from serviceable import Serviceable
import datetime
class Car(Serviceable):
    def __init__(self, engine,battery):
        self.engine=engine
        self.battery=battery

    @abstractmethod
    def needs_service(self):
         if self.battery.needs_service() or self.engine.needs_service()
             return true
         else
             return false
