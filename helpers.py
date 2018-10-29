from calendar import HTMLCalendar
import datetime
import pytz


class _localized_day:

    # January 1, 2001, was a Monday.
    _days = [datetime.date(2001, 1, i+1).strftime for i in range(7)]

    def __init__(self, format):
        self.format = format

    def __getitem__(self, i):
        funcs = self._days[i]
        if isinstance(i, slice):
            return [f(self.format) for f in funcs]
        else:
            return funcs(self.format)

    def __len__(self):
        return 7


# Full and abbreviated names of weekdays
day_name = _localized_day('%A')
day_abbr = _localized_day('%a')


class AppCalendar(HTMLCalendar):

    def __init__(self):
        super(AppCalendar, self).__init__(firstweekday=0)

    # CSS class for the days before and after current month
    cssclass_noday = "noday"

    # CSS classes for the day <td>s
    cssclasses = ["mon text-bold", "tue", "wed", "thu", "fri", "sat", "sun_red"]

    # CSS class for the month
    cssclass_month = "month"

    # CSS classes for the day <th>s
    cssclasses_weekday_head = cssclasses

    @staticmethod
    def get_today():
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        pst_now = utc_now.astimezone(pytz.timezone("Asia/Shanghai"))
        return pst_now.day

    def formatday(self, day, weekday):
        """
        Return a day as a table cell.
        """
        if day == 0:
            # day outside month
            return '<td class="%s">&nbsp;</td>' % self.cssclass_noday
        if day == self.get_today():
            return '<td class="%s"><a href="#"><span style="border-radius:50%%; border:solid blue 2px;padding:3px; text-align: center">%d&nbsp;</span></a></td>' % (self.cssclasses[weekday], day)
        else:
            return '<td class="%s"><a href="#">%d&nbsp;</a></td>' % (self.cssclasses[weekday], day)

    def formatweekday(self, day):
        """
        Return a weekday name as a table header.
        """
        return '<th class="%s">%s&nbsp;&nbsp;</th>' % (
            self.cssclasses_weekday_head[day], day_abbr[day])
