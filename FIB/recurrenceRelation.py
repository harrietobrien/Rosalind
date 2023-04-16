# improve efficiency with memoization
results = dict()


class FIB:
    def __init__(self, data):
        self.data = data
        self.test()

    def fibonacci(self, n, k):
        if n in results:
            return results[n]
        if n == 1:
            result = 1
        elif n == 2:
            result = k
        elif n <= 4:
            result = self.fibonacci(n - 1, k) + \
                     self.fibonacci(n - 2, k)
        else:
            result = self.fibonacci(n - 1, k) + \
                     self.fibonacci(n - 2, k) * k
        results[n] = result
        return result

    def test(self):
        with open(self.data, 'r', encoding='UTF-8') as file:
            vars = None
            for line in file:
                vars = line.strip().split(' ')
        if vars:
            n, k = int(vars[0]), int(vars[1])
            print(self.fibonacci(n, k))


test = FIB('rosalind_fib.txt')
