#!/usr/bin/env python3

#
# 1)
print("Ex 1")
for i in range(10):
    print(i)

# 2)
print("Ex 2")
t1 = list(range(10))
print(t1)
t2 = list(range(2, 11))
print(t2)
t3 = list(range(2, 11, 2))
print(t3)
t4 = list(range(10, 1, -2))
print(t4)

# 3)
print("Ex 3")
L1 = [i for i in range(0, 13, 2)]
print(L1)
L2 = [chr(97 + i) for i in range(6)]
print(L2)
L1.reverse()
print(L2)
L3 = [i for i in zip(L2, L1)]
print(L3)

# 4)
print("Ex 4")
print(L3[2:5])
print(L3[1::2])
L4 = L3[::]
print(L4)
L5 = [0 if k % 3 == 2 else k * 7 for k in range(1, 21)]
print(L5)

# 6)
print("Ex 6")
L = list(range(2, 36, 3))
print(L)
LG = L[: len(L) // 2 :]
print(LG)
LD = L[len(L) // 2 : :]
print(LD)


def f(t):
    if len(t) > 0:
        t[0] += 2022


def g(t):
    if len(t) > 0:
        t[-1] += 2022


LD[-1] += 2022
f(LG)
g(L)
g(L[: len(L) // 2 :])
print(L)
print(LG)
print(LD)

print("Nombres premiers")


def crible_eratosthene(n):
    # calcule la table de booléens où la i-ème position est True
    # si et seulement si i est un nombre premier.
    if n < 0:
        return None
    if n == 0:
        return []
    if n == 1:
        return [False]

    res = [False, False] + [True] * (n - 1)
    for i in range(2, n + 1):
        if res[i]:
            res[i + i :: i] = [False] * (((n - i - i) // i + 1))
    return res


def test_crible(n):
    c = crible_eratosthene(n)
    for i in range(len(c)):
        if c[i]:
            print(i, end=" ")
    print()


def somme_impairs(x):
    # calcule la somme des entiers impairs de 1 à x
    somme = 0
    for i in range(1, x + 1, 2):
        somme += i
    return somme


def test_somme(n):
    # teste que la somme des entiers impairs de 1 à x =
    #    (x/2)*(x/2) si x est pair
    #    (x+1)/2*(x+1)/2 sinon
    # pour tout 1 <= x <= n
    for i in range(1, n + 1):
        if (i % 2) == 0 & somme_impairs(i) != (x // 2) * (x // 2):
            return false
        elif somme_impairs(i) != ((i + 1) // 2) * ((x + 1) // 2):
            return false
    return True


# AJOUTER D'AUTRES TESTS
#  [valeur_x, resultat_attendu]
def testDataSomme():
    """retourne un jeu de tests"""
    return [[0, 0], [3, 4], [24, 144], [-3, 0]]


#
# NE PAS MODIFIER
#
def testOp(op, data):
    print("\n\n* Test function %s:" % op.__name__)
    score = 0
    ldata = len(data)
    for i, dt in enumerate(data):
        print("** test %d/%d : " % (i + 1, ldata), end="")
        x = dt[0]
        refr = dt[1]
        r = op(x)
        if r == refr:
            score += 1
            print("ok")
        else:
            print("ECHEC")
            print("    entree  : %s" % x)
            print("    calcule : %s" % r)
            print("    attendu : %s" % refr)
    print("** Score %d/%d" % (score, ldata))


if __name__ == "__main__":
    test_crible(50)
    testOp(somme_impairs, testDataSomme())
