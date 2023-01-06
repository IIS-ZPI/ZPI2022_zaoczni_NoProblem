from datetime import *
from dateutil.relativedelta import *

from nbp_enums import Period


class DateUtil:
    def __init__(self):
        self.end_date = datetime.now()

    def get_distance_between_dates(self, interval: Period):
        intervals = {
            Period.WEEK: relativedelta(weeks=-1),
            Period.TWO_WEEKS: relativedelta(weeks=-2),
            Period.MONTH: relativedelta(months=-1),
            Period.QUARTER: relativedelta(months=-3),
            Period.HALF_YEAR: relativedelta(months=-6),
            Period.YEAR: relativedelta(years=-1)
        }

        return intervals.get(interval)

    def get_end_date(self, interval: Period):
        return (self.end_date + self.get_distance_between_dates(interval)).date()
