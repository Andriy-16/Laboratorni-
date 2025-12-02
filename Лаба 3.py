g = {}

while True:
    n = input("Ім'я: ")
    if n == "stop": break
    g[n] = int(input("Оцінка: "))

print("\nСписок студентів:", g)

avg = sum(g.values()) / len(g)
print("Середній бал:", avg)

print("Відмінники:", [x for x,y in g.items() if 10<=y<=12])
print("Хорошисти:", [x for x,y in g.items() if 7<=y<=9])
print("Відстаючі:", [x for x,y in g.items() if 4<=y<=6])
print("Не здали:", [x for x,y in g.items() if 1<=y<=3])
