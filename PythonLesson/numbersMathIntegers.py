age = 20
name  = "r00t"
print(name, "\n", age)
print(type (age))
brojParnih = 0
n = int(input("Unesite broj: "))
for i in  range(n):
    if i % 2 == 0:
        brojParnih += 1
print("Broj parnih: ", brojParnih)

for i in range(2, 10):
    print("Jebem ti staru")