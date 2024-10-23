class mathematics():
    def __init__(self):
        pass

    def addition(self, a, b, c, d):
        e = a + b + c + d
        return e
    
    def multiplication(self, a, b, c):
        f = a * b * c
        return f

res = mathematics()
result = res.addition(5, 6, 7)
product = res.multiplication(8, 6, 7)
divide = result/product

print(result)
print(product)
print(divide)