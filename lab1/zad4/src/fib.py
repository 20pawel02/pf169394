class Fibonacci:
    def fib(self, n):
        if n < 0:
            raise ValueError("n musi być > 0")
        elif n == 0:
            return 1
        else:
            a, b = 0, 1
            for i in range(2, n + 1):
                a, b = b, a + b
            return b
