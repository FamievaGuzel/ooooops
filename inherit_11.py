class Summator:
    def transform(self, n):
        return n

    def sum(self, N):
        total = 0
        for i in range(1, N + 1):
            total += self.transform(i)
        return total


class PowerSummator(Summator):
    def __init__(self, b):
        self.b = b

    def transform(self, n):
        return n ** self.b


class SquareSummator(PowerSummator):
    def __init__(self):
        super().__init__(2)


class CubeSummator(PowerSummator):
    def __init__(self):
        super().__init__(3)

    
# Ваш код

print(PowerSummator(1).sum(10), PowerSummator(2).sum(10), PowerSummator(3).sum(10))
print(SquareSummator().sum(10), CubeSummator().sum(10))
print(round(PowerSummator(0.5).sum(4), 4))

# Ваш код

print(issubclass(PowerSummator, Summator))
print(issubclass(SquareSummator, PowerSummator), issubclass(CubeSummator, PowerSummator))
print('transform' in PowerSummator.__dict__, 'sum' in PowerSummator.__dict__)
print('transform' in SquareSummator.__dict__, 'sum' in SquareSummator.__dict__)
print('transform' in CubeSummator.__dict__, 'sum' in CubeSummator.__dict__)

