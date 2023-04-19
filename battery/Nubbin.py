from .battery import battery
from .util import battery_service_year


class Nubbin(battery):
        def __init__(self, current_date, last_service_date):
            self.last_service_date = last_service_date
            self.current_date = current_date

        def needs_service(self):
            return self.current_date>battery_service_year(self.last_service_date,4)