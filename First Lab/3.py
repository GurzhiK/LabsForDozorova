s = int(input("Введите вверхнюю граниу троек:"))
n = int(input("Введите число троек :"))
def find_pythagorean_triples(n):
    triples = []
    a = 1
    
    while len(triples) < n:
        for b in range(a, s):
            c = (a ** 2 + b ** 2) ** 0.5
            if c == int(c):
                triples.append((a, b, int(c)))
                break
        a += 1

    return triples
print(find_pythagorean_triples(n))