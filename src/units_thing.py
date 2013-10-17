
from collections import Counter

class UnitsThing(object):
    UNITS = ["kg", "km", "m", "s"]
    def __init__(self, measure, units):
        self.measure = measure
        if type(units) is str:
            if "/" not in units:
                over, under = units, ""
            else:
                over, under = units.split("/")
            o, u = self.unitize(over), self.unitize(under)
            o.subtract(u)
            self.units = o
        else:
            self.units = units
        p = self.units.get("km")
        if p:
            self.units["m"] += p
            self.units["km"] = 0
            self.measure *= 1000.0 ** p
    def __mul__(self, x):
        if type(x) is UnitsThing:
            new_units = self.units.copy()
            new_units.update(x.units)
            return UnitsThing(self.measure * x.measure, new_units)
        else:
            return UnitsThing(self.measure * x, self.units.copy())
    def __div__(self, x):
        if type(x) is UnitsThing:
            new_units = self.units.copy()
            new_units.subtract(x.units)
            return UnitsThing(self.measure / x.measure, new_units)
        else:
            return UnitsThing(self.measure / x, self.units.copy())
    def __plus__(self, x):
        assert type(x) is UnitsThing
        assert x.units == self.units
        return UnitsThing(self.measure + x, self.units)
    def __sub__(self, x):
        assert type(x) is UnitsThing
        assert x.units == self.units
        return UnitsThing(self.measure - x, self.units)
    def unitize(self, units):
        c = Counter()
        for u in self.UNITS:
            while u in units:
                c[u] += 1
                i = units.index(u)
                units = units[:i] + units[i + len(u):]
        return c
    def unit_format(self, c):
        return "".join("{0}^{1}".format(k, v) for k, v in c.items() if v)
    def __str__(self):
        u = self.unit_format(self.units)
        return "{0} {1}".format(self.measure, u)
    def sqrt(self):
        return UnitsThing(self.measure ** 0.5, self.units)
