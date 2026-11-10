class Summator:
    def transform(self, n):
        return n

    def sum(self, N):
        total = 0
        for i in range(1, N + 1):
            total += self.transform(i)
        return total


class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3
    
# Ваш код

print(Summator().sum(10), SquareSummator().sum(10), CubeSummator().sum(10))
print(Summator().transform(3), SquareSummator().transform(3), CubeSummator().transform(3))
print(issubclass(SquareSummator, Summator), issubclass(CubeSummator, Summator))
print('sum' in SquareSummator.__dict__, 'sum' in CubeSummator.__dict__)