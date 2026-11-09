class BaseStat:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)


class MinStat(BaseStat):
    def result(self):
        if not self.numbers:
            return None
        return min(self.numbers)


class MaxStat(BaseStat):
    def result(self):
        if not self.numbers:
            return None
        return max(self.numbers)


class AverageStat(BaseStat):
    def result(self):
        if not self.numbers:
            return None
        return sum(self.numbers) / len(self.numbers)
    
# Ваш код

values = [1, 2, 4, 5]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))

# Ваш код

mins = MinStat()
maxs = MaxStat()
average = AverageStat()

print(mins.result(), maxs.result(), average.result())

# Ваш код

values = [1, 0, 0]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))

