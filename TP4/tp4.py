#!/usr/bin/env python3

from time import perf_counter as clock
import random
import sys

version = sys.version_info
if version.major < 3:
    sys.exit(
        "Python2 n'est PLUS supporté depuis le 1er Janvier 2020, merci d'installer Python3"
    )


try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    sys.exit("Le module matplolib est nécessaire pour ce TP.")

############################################################
# Exercice 1.1
#
# Tri rapide avec mémoire auxiliaire et en place
#


def partition(T):
    pivot = T[0]
    gauche = []
    droite = []
    milieu = []

    for e in T:
        if (e < pivot):
            gauche.append(e)
        elif (e > pivot):
            droite.append(e)
        else:
            milieu.append(e)

    return gauche, droite, milieu


def tri_rapide(T):
    if len(T) < 2:
        return T

    gauche, droite, milieu = partition(T)

    return tri_rapide(gauche) + milieu + tri_rapide(droite)


def partition_en_place(T, debut, fin):

    pivot = T[debut]
    gauche = debut + 1
    droite = fin - 1

    while (gauche <= droite):
        if (T[gauche] <= pivot):
            gauche += 1
        elif (T[droite] >= pivot):
            droite -= 1
        else:
            T[gauche], T[droite] = T[droite], T[gauche]
    T[droite], T[debut] = pivot, T[droite]
    return droite


def tri_rapide_en_place(T, debut=0, fin=None):
    if (fin == None):
        fin = len(T)
    if (fin - debut < 2):
        return
    pos_pivot = partition_en_place(T, debut, fin)
    tri_rapide_en_place(T, debut, pos_pivot)
    tri_rapide_en_place(T, pos_pivot + 1, fin)

    return T

############################################################
# Exercice 1.2
#
# Tri rapide avec mémoire auxiliaire et en place avec pivot
# aléatoire
#


def partition_random(T):
    pivot = T[random.randint(0, len(T) - 1)]
    gauche = [x for x in T if x < pivot]
    droite = [x for x in T if x > pivot]
    return pivot, gauche, droite


def tri_rapide_aleatoire(T):
    if len(T) < 2:
        return T

    pivot, gauche, droite = partition_random(T)

    return tri_rapide_aleatoire(gauche) + [pivot] + tri_rapide_aleatoire(droite)


def partition_en_place_random(T, debut, fin):
    rand = random.randint(debut, fin - 1)
    T[debut], T[rand] = T[rand], T[debut]

    pivot = T[debut]
    gauche = debut + 1
    droite = fin - 1

    while (gauche <= droite):
        if (T[gauche] <= pivot):
            gauche += 1
        elif (T[droite] >= pivot):
            droite -= 1
        else:
            T[gauche], T[droite] = T[droite], T[gauche]
    T[droite], T[debut] = pivot, T[droite]
    return droite


def tri_rapide_en_place_aleatoire(T, debut=0, fin=None):
    if (fin == None):
        fin = len(T)
    if (fin - debut < 2):
        return
    pos_pivot = partition_en_place_random(T, debut, fin)
    tri_rapide_en_place_aleatoire(T, debut, pos_pivot)
    tri_rapide_en_place_aleatoire(T, pos_pivot + 1, fin)

    return T


############################################################
""" Exercice 1.3: Interprétation des courbes

Pour random_perm, le tri insertion est celui le moins efficace, suivis du tri
rapide en place aleatoire de très peu, et les autres algorithme s'équivalent sur la fin
Pour random_tab, même rendu qu'avant
Pour derange_un_peu(rev=False), tri_rapide fait partie des moins rapide avec
selui en place, et on a à la même place les autres algorithmes
Pour derange_un_peu(rev=True), le tri insertion est le moins efficace,
suivis du tri rapide, puis du tri rapide en place, et les derniers s'équivalent
"""

############################################################
# Exercice 2.1
#
# Tri par insertion  (voir TP3)
#


def rotation(T, i, j):
    temp = T[i]
    for k in range(i-1, j-1, -1):
        T[k+1] = T[k]
    T[j] = temp


def searchIndexDichotomyc(T, i, debut=0):
    j = i - 1
    k = debut

    while (j >= k):
        temp = (j + k) // 2
        if (T[i] > T[temp]):
            k = temp + 1
        elif (T[i] < T[temp]):
            j = temp - 1
        else:
            return temp
    return k


def tri_insertion(T, debut=0, fin=None):
    if (fin == None):
        fin = len(T)

    if (fin - debut < 2):
        return T

    for i in range(debut + 1, fin):
        j = searchIndexDichotomyc(T, i, debut)
        rotation(T, i, j)
    return T


############################################################
# Exercice 2.2
#
# les tableaux de taille < 15 sont triés par insertion, le
# reste avec l'algo de tri rapide usuel.
#

def tri_rapide_ameliore(T, debut=0, fin=None):
    if (fin == None):
        fin = len(T)
    if (fin - debut < 15):
        return tri_insertion(T, debut, fin)
    pos_pivot = partition_en_place(T, debut, fin)
    tri_rapide_ameliore(T, debut, pos_pivot)
    tri_rapide_ameliore(T, pos_pivot + 1, fin)

    return T

############################################################
# Exercice 2.3
#
# Tri rapide seulement pour les tableaux de taille >= 15 et
# ne fait rien pour les tableaux de taille < 15
#


def tri_rapide_partiel(T, debut=0, fin=None):
    if (fin == None):
        fin = len(T)
    if (fin - debut < 15):
        return T
    pos_pivot = partition_en_place(T, debut, fin)
    tri_rapide_partiel(T, debut, pos_pivot)
    tri_rapide_partiel(T, pos_pivot + 1, fin)

    return T


############################################################
# Exercice 2.4
#
# Trie par  le résultat de tri_rapide_partiel(T).
#


def tri_sedgewick(T):
    return tri_insertion(tri_rapide_partiel(T))


############################################################
""" Exercice 2.5: Interprétation des courbes

Parmi les courbes de temps, pour les random_perm, sedgewick fait partis des pire algorithme rapide, plus lent que celui de fusion, alors que
le tri rapide ameliore se trouve parmi les meilleurs, avec le tri_rapide_aleatoire par exemple

Parmi les courbes de temps, pour les random_tab, sedgewick a la même position qu'avant, avec une croissance
encore plus accrus qu'avant
Quant à lui, le tri rapide ameliore a une croissance plus importante que les meileurs algorithme pour ces cas la
comme le tri rapide, et est à la même place que le tri_rapide_en_place aleatoire

Parmi les courbes de temps, à l'aide de derange un peu (rev = False), sedgewick et tri_rapide_ameliore sont a peu près à la
même place avec les tri_rapide_en_place_aleatoire et tri_rapide, avec le tri_ et tri_fusion
restant les meilleurs pours ces cas

Parmi les courbes de temps, à l'aide de derange un peu (rev = True), le tri_fusion reste le plus rapide,
avec sedgewick en dessous du tri par insertion mais au dessus des autres tris, et le tri rapide
ameliore est parmi les meilleurs avec les autres algorithmes de tri rapide
"""


############################################################
# Exercice 3.1
#
# Tris drapeau. Attention, les éléments du tableau ne peuvent pas
# avoir d'autres valeurs que 1, 2 ou 3.
#

BLEU, BLANC, ROUGE = 1, 2, 3


def tri_drapeau(T):
    t_bleu = []
    t_blanc = []
    t_rouge = []

    for e in T:
        if (e == BLEU):
            t_bleu.append(BLEU)
        elif (e == BLANC):
            t_blanc.append(BLANC)
        else:
            t_rouge.append(ROUGE)

    return t_bleu + t_blanc + t_rouge


def tri_drapeau_en_place(T):
    i, j, k = 0, 0, len(T) - 1

    while (j <= k):
        if (T[j] == BLANC):
            j += 1

        elif (T[j] == BLEU):
            T[j], T[i] = T[i], T[j]
            j += 1
            i += 1

        else:
            T[j], T[k] = T[k], T[j]
            k -= 1
    return T


############################################################
# Exercice 3.2
#
# Effectue un tri drapeau par rapport au pivot.
# Les éléments strictements inférieur au pivot ont couleur 1,
# les éléments égaux au pivot ont couleur 2,
# et les éléments supérieur au pivot ont couleur 3.
# Retourne trois tableaux, contenant respectivement les éléments de couleurs 1, 2 et 3.
#

def partition_drapeau(T):
    t_bleu = []
    t_blanc = []
    t_rouge = []

    pivot = T[random.randint(0, len(T) - 1)]

    for e in T:
        if (e < pivot):
            t_bleu.append(e)
        elif (e == pivot):
            t_blanc.append(e)
        else:
            t_rouge.append(e)

    return t_bleu, t_blanc, t_rouge

############################################################
# Exercice 3.2
#
# Tris rapide, pivot drapeau pour amélioration si le tableau en entrée
# est très répété.
#


def tri_rapide_drapeau(T):
    if len(T) < 2:
        return T

    gauche, milieu, droite = partition_drapeau(T)

    return tri_rapide_drapeau(gauche) + milieu + tri_rapide_drapeau(droite)


############################################################
""" Exercice 3.3: Interprétation des courbes

# Les tris drapeaux sont aussi rapides que le tri rapide d'après la courbe

"""

############################################################
# Exercice 3.4
#
# Effectue un tri drapeau EN PLACE par rapport au pivot.
# Les éléments strictements inférieur au pivot ont couleur 1,
# les éléments égaux au pivot ont couleur 2,
# et les éléments supérieur au pivot ont couleur 3.
# Retourne l'indice du premier élement blanc et du premier element rouge dans le tableau.
# (le premier élément bleu étant à la position 0 si il existe, pas besoin de le préciser.)
#


def partition_drapeau_en_place(T, debut, fin, pivot):
    i, j, k = debut, debut, fin - 1

    while (j <= k):
        if (T[j] == pivot):
            j += 1

        elif (T[j] < pivot):
            T[j], T[i] = T[i], T[j]
            i += 1
            j += 1

        else:
            T[j], T[k] = T[k], T[j]
            k -= 1
    return i, k

############################################################
# Exercice 3.4
#
# Tri rapide en place utilisant un partitionnement drapeau
#


def tri_rapide_drapeau_en_place(T, debut=0, fin=None):
    if (fin == None):
        fin = len(T)
    if (fin - debut < 2):
        return
    # pivot = random.randint(debut, fin - 1) don't work
    i, j = partition_drapeau_en_place(T, debut, fin, T[debut])
    tri_rapide_drapeau_en_place(T, debut, i)
    tri_rapide_drapeau_en_place(T, j + 1, fin)
    return T


##############################################################
#
# Tri Fusion, pour comparaison
#

def fusion(T1, T2):
    i = 0
    j = 0
    res = []
    while i < len(T1) and j < len(T2):
        if T1[i] < T2[j]:
            res.append(T1[i])
            i += 1
        else:
            res.append(T2[j])
            j += 1
    res += T1[i:]
    res += T2[j:]
    return res


def tri_fusion(T, deb=0, fin=None):
    if fin is None:
        fin = len(T)
    if fin - deb <= 1:
        return T[deb:fin]
    m = (fin - deb)//2
    T1 = tri_fusion(T, deb, deb+m)
    T2 = tri_fusion(T, deb+m, fin)
    return fusion(T1, T2)

##############################################################
#
# Mesure du temps
#


def mesure(algo, T):
    debut = clock()
    algo(T)
    return clock() - debut


def mesure_moyenne(algo, tableaux):
    return sum([mesure(algo, t[:]) for t in tableaux]) / len(tableaux)


couleurs = ['b', 'g', 'r', 'm', 'c', 'k', 'y', '#ff7f00', '.5',
            '#00ff7f', '#7f00ff', '#ff007f', '#7fff00', '#007fff']
marqueurs = ['o', '^', 's', '*', '+', 'd', 'x', '<',
             'h', '>', '1', 'p', '2', 'H', '3', 'D', '4', 'v']


def courbes(algos, tableaux, styleLigne='-'):
    x = [t[0] for t in tableaux]
    for i, algo in enumerate(algos):
        print('Mesures en cours pour %s...' % algo.__name__)
        y = [mesure_moyenne(algo, t[1]) for t in tableaux]
        plt.plot(x, y, color=couleurs[i % len(couleurs)], marker=marqueurs[i % len(
            marqueurs)], linestyle=styleLigne, label=algo.__name__)


def affiche(titre):
    plt.xlabel('taille du tableau')
    plt.ylabel('temps d\'execution (sec)')
    plt.legend(loc='upper left')
    plt.title(titre)


def random_perm(n):
    T = list(range(n))
    random.shuffle(T)
    return T


def test_tri(f):
    for i in range(2, 101):
        T = random_perm(i)
        T_sorted = sorted(T)
        T_output = f(T)
        if T_output != T_sorted:
            print("Échec sur :")
            print(T)
            return False
    return True


def random_tab(n, a, b):
    return [random.randint(a, b) for _ in range(n)]


def derange_un_peu(n, k, rev):
    T = [n - i for i in range(n)] if rev else [i + 1 for i in range(n)]
    for i in range(k):
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        T[a], T[b] = T[b], T[a]
    return T


def compare_algos(algos):
    for tri in algos:
        if test_tri(tri):
            print(tri.__name__ + ": OK")
        else:
            print(tri.__name__ + ": échoue")
    taille = 1000  # taille maximale des tableaux à trier
    pas = 100  # pas entre les tailles des tableaux à trier
    ech = 5  # taille de l'échantillon pris pour faire la moyenne

    plt.subplot(221)
    print()
    print("Comparaison à l'aide de random_perm")
    tableaux = [[i, [random_perm(i) for j in range(ech)]]
                for i in range(2, taille, pas)]
    courbes(algos, tableaux, styleLigne='-')
    affiche("Comparaison à l'aide de random_perm")

    plt.subplot(222)
    print()
    print("Comparaison à l'aide de random_tab")
    tableaux = [[i, [random_tab(i, 0, 1000000) for j in range(ech)]]
                for i in range(2, taille, pas)]
    courbes(algos, tableaux, styleLigne='-')
    affiche("Comparaison à l'aide de random_tab")

    plt.subplot(223)
    print()
    print("Comparaison à l'aide de derange_un_peu (rev = False)")
    tableaux = [[i, [derange_un_peu(i, 20, False) for j in range(ech)]]
                for i in range(2, taille, pas)]
    courbes(algos, tableaux, styleLigne='-')
    affiche("Comparaison à l'aide de derange_un_peu (rev = False)")

    plt.subplot(224)
    print()
    print("Comparaison à l'aide de derange_un_peu (rev = True)")
    tableaux = [[i, [derange_un_peu(i, 20, True) for j in range(ech)]]
                for i in range(2, taille, pas)]
    courbes(algos, tableaux, styleLigne='-')
    affiche("Comparaison à l'aide de derange_un_peu (rev = True)")

    plt.show()


def test_tri_non_perm(tri, maxVal=3):
    for size in range(2, 101):
        T = random_tab(size, 1, maxVal)
        T2 = tri(T)
        for i in range(1, len(T2)):
            if T2[i-1] > T2[i]:
                return False
    return True


def compare_tableaux_repetes(algos, taille=20000, pas=1000, ech=15, maxVal=3):
    for tri in algos:
        if test_tri_non_perm(tri):
            print(tri.__name__ + ": OK")
        else:
            print(tri.__name__ + ": échoue")

    print("Comparaison à l'aide de random_tab")
    tableaux = [[i, [random_tab(i, 1, 3) for j in range(ech)]]
                for i in range(2, taille, pas)]
    courbes(algos, tableaux, styleLigne='-')
    affiche("Comparaison à l'aide de random_tab")
#
#
#
#
    plt.show()


##############################################################
#
# Main
#

if __name__ == '__main__':
    trisRapides = [tri_insertion, tri_fusion, tri_rapide, tri_rapide_en_place,
                   tri_rapide_aleatoire, tri_rapide_en_place_aleatoire]
    trisHybrides = [tri_rapide_ameliore, tri_sedgewick]
    trisDrapeaux = [tri_drapeau, tri_drapeau_en_place]
    trisRapidesDrapeaux = [tri_fusion,
                           tri_rapide_drapeau, tri_rapide_drapeau_en_place]

    # exercice 1

    print("Exercice 1")
    algos = trisRapides
    compare_algos(algos)

    # exercice 2

    print("Exercice 2")
    algos = trisHybrides
    compare_algos(algos)
    algos = trisRapides + trisHybrides
    compare_algos(algos)

    # exercice 3

    print("Exercice 3")
    # comparaison des tris drapeaux
    print("Comparaisons sur tableaux très répétés")
    algos = trisDrapeaux
    compare_tableaux_repetes(algos, maxVal=3)
    # comparaison des tris rapide drapeaux
    print("Comparaisons sur tableaux très répétés")
    algos = [tri_rapide, tri_rapide_en_place] + trisRapidesDrapeaux
    compare_tableaux_repetes(algos, taille=1000, pas=100, ech=5, maxVal=5)
