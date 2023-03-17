import random

flavors = ['клубника', 'апельсин', 'яблоко', 'ананас', 'вишня']

shapes = ['круг', 'квадрат', 'треугольник', 'звезда', 'сердце']
random_flavor = random.choice(flavors)
random_shape = random.choice(shapes)

print(f'Мармеладка в форме {random_shape} со вкусом {random_flavor}')