#!/usr/bin/env python3

from time import process_time as clock
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
# Tri selection
#

def findMinAfterIndex(T, index):
    min = index

    for j in range(index + 1, len(T)):
        if (T[j] < T[min]):
            min = j
    return min


def triSelection(T):
    for i in range(len(T)):
        min = findMinAfterIndex(T, i)
        T[i], T[min] = T[min], T[i]

    return T

############################################################
# Exercice 1.2
#
# randomPerm prend en paramètre un entier n et renvoie une
# permutation aléatoire de longueur n dont l'algorithme s'appuie
# sur le tri sélection
#


def randomPerm(n):
    T = [i+1 for i in range(n)]

    for i in range(n-1):
        temp = random.randint(i+1, n-1)
        T[i], T[temp] = T[temp], T[i]
    return T

############################################################
# Exercice 1.3
#
# testeQueLaFonctionTrie prend en paramètre une fonction de
# tri f et l’applique sur des permutations aléatoires de
# taille i variant de 2 à 100 et vérifie que le résultat est
# un tableau trié
#


def isSortedPerm(T):
    for i in range(1, len(T)):
        if (i != T[i-1]):
            return False
    return True


def testeQueLaFonctionTrie(f):
    for length in range(2, 100):
        tabRandomPerm = randomPerm(length)

        if (not isSortedPerm(f(tabRandomPerm[:]))):
            print(tabRandomPerm)
            return False
    return True

############################################################
# Exercice 1.4
#
# randomTab prend des entiers n, a et b et renvoie un tableau
# aléatoire de taille n contenant des entiers compris entre
# les bornes a et b.
#


def randomTab(n, a, b):

    return [random.randint(a, b) for _ in range(n)]


############################################################
# Exercice 1.5
#
# derangeUnPeu prend des entiers n, k et un booléen rev et
# effectue k échanges entre des positions aléatoires sur la
# liste des entiers de 1 à n si rev vaut False ou sur la
# liste des entiers n à 1 si rev vaut True.
#


def derangeUnPeu(n, k, rev):
    T = [n - i for i in range(n)] if rev else [i + 1 for i in range(n)]

    for i in range(k):
        x1, x2 = random.randint(0, n-1), random.randint(0, n-1)
        T[x1], T[x2] = T[x2], T[x1]

    return T


############################################################
# Exercice 2.1
#
# Trois variantes du tri par insertion L échanges successifs,
# insertion directe à la bonne position, et avec recherche
# dichotomique de la position
#

def triInsertionEchange(T):

    for i in range(1, len(T)):
        for j in range(i, 0, -1):
            if T[j-1] > T[j]:
                T[j-1], T[j] = T[j], T[j-1]
            else:
                break

    return T


def rotation(T, i, j):
    temp = T[i]
    for k in range(i-1, j-1, -1):
        T[k+1] = T[k]
    T[j] = temp


def searchIndexSimple(T, i):
    for j in range(i-1, -1, -1):
        if (T[i] > T[j]):
            return j + 1
    return 0


def searchIndexDichotomyc(T, i):
    j = i - 1
    k = 0

    while (j >= k):
        temp = (j + k) // 2
        if (T[i] > T[temp]):
            k = temp + 1
        elif (T[i] < T[temp]):
            j = temp - 1
        else:
            return temp
    return k


def triInsertionRotation(T):
    for i in range(1, len(T)):
        j = searchIndexSimple(T, i)
        rotation(T, i, j)
    return T


def triInsertionRapide(T):
    for i in range(1, len(T)):
        j = searchIndexDichotomyc(T, i)
        rotation(T, i, j)
    return T

############################################################
# Exercice 2.2
#
# Tri fusion
#


def fusion(T1, T2):
    if (len(T1) == 0):
        return T2
    if (len(T2) == 0):
        return T1
    res = []
    lenT1 = len(T1)
    lenT2 = len(T2)
    i = 0
    j = 0

    while (i + j < lenT1 + lenT2):
        if (i == lenT1):
            res.append(T2[j])
            j += 1
        elif (j == lenT2):
            res.append(T1[i])
            i += 1
        elif (T1[i] <= T2[j]):
            res.append(T1[i])
            i += 1
        else:
            res.append(T2[j])
            j += 1
    return res


def triFusion(T, deb=0, fin=None):
    if fin == None:
        fin = len(T)
    if fin - deb < 2:
        return T[deb:fin]
    else:
        mid = (fin + deb) // 2
        return fusion(triFusion(T, deb, mid), triFusion(T, mid, fin))

############################################################
# Exercice 2.3
#
# Tri à bulles
#


def triBulles(T):
    for i in range(len(T) - 1, 0, -1):
        T_trie = True
        for j in range(0, i):
            if (T[j+1] < T[j]):
                T[j+1], T[j] = T[j], T[j+1]
                T_trie = False
        if (T_trie):
            break
    return T

############################################################
# Exercice 3.1
#
# Trie par insertion le sous-tableau T[debut::gap] de T
#


def searchIndexSimpleWithGap(T, i, gap, deb):
    for j in range(i-gap, deb-1, -gap):
        if (T[i] > T[j]):
            return j + gap
    return deb


def rotationWithGap(T, i, j, gap):
    temp = T[i]
    for k in range(i-gap, j-1, -gap):
        T[k+gap] = T[k]
    T[j] = temp


def triInsertionPartiel(T, gap, deb):
    for i in range(deb+gap, len(T), gap):
        j = searchIndexSimpleWithGap(T, i, gap, deb)
        rotationWithGap(T, i, j, gap)
    return T

############################################################
# Exercice 3.2
#
# Tri Shell
#


def triShell(T):
    triInsertionPartiel(T, 53, 0)
    triInsertionPartiel(T, 23, 0)
    triInsertionPartiel(T, 10, 0)
    triInsertionPartiel(T, 4, 0)
    triInsertionPartiel(T, 1, 0)
    return T

##############################################################
#
# Mesure du temps
#


def mesure(algo, T):
    debut = clock()
    algo(T)
    return clock() - debut


def mesureMoyenne(algo, tableaux):
    return sum([mesure(algo, t[:]) for t in tableaux]) / len(tableaux)


couleurs = ['b', 'g', 'r', 'm', 'c', 'k', 'y', '#ff7f00', '.5',
            '#00ff7f', '#7f00ff', '#ff007f', '#7fff00', '#007fff']
marqueurs = ['o', '^', 's', '*', '+', 'd', 'x', '<',
             'h', '>', '1', 'p', '2', 'H', '3', 'D', '4', 'v']


def courbes(algos, tableaux, styleLigne='-'):
    x = [t[0] for t in tableaux]
    for i, algo in enumerate(algos):
        print('Mesures en cours pour %s...' % algo.__name__)
        y = [mesureMoyenne(algo, t[1]) for t in tableaux]
        plt.plot(x, y, color=couleurs[i % len(couleurs)], marker=marqueurs[i % len(
            marqueurs)], linestyle=styleLigne, label=algo.__name__)


def affiche(titre):
    plt.xlabel('taille du tableau')
    plt.ylabel('temps d\'execution')
    plt.legend(loc='upper left')
    plt.title(titre)
    plt.show()


def compareAlgos(algos, taille=1000, pas=100, ech=5):
    # taille = 1000 : taille maximale des tableaux à trier
    # pas = 100 : pas entre les tailles des tableaux à trier
    # ech = 5 : taille de l'échantillon pris pour faire la moyenne
    for tri in algos:
        if testeQueLaFonctionTrie(tri):
            print(tri.__name__ + ": OK")
        else:
            print(tri.__name__ + ": échoue")
    print()
    print("Comparaison à l'aide de randomPerm")
    tableaux = [[i, [randomPerm(i) for j in range(ech)]]
                for i in range(2, taille, pas)]
    courbes(algos, tableaux, styleLigne='-')
    affiche("Comparaison à l'aide de randomPerm")
    print()

    print("Comparaison à l'aide de randomTab")
    tableaux = [[i, [randomTab(i, 0, 1000000) for j in range(ech)]]
                for i in range(2, taille, pas)]
    courbes(algos, tableaux, styleLigne='-')
    affiche("Comparaison à l'aide de randomTab")
    print()

    print("Comparaison à l'aide de derangeUnPeu (rev = True)")
    tableaux = [[i, [derangeUnPeu(i, 10, True) for j in range(ech)]]
                for i in range(2, taille, pas)]
    courbes(algos, tableaux, styleLigne='-')
    affiche("Comparaison à l'aide de derangeUnPeu (rev = True)")
    print()

    print("Comparaison à l'aide de derangeUnPeu (rev = False)")
    tableaux = [[i, [derangeUnPeu(i, 10, False) for j in range(ech)]]
                for i in range(2, taille, pas)]
    courbes(algos, tableaux, styleLigne='-')
    affiche("Comparaison à l'aide de derangeUnPeu (rev = False)")
    print()


def compareAlgosSurTableauxTries(algos, taille=20000, pas=1000, ech=10):
    print("Comparaison à l'aide de derangeUnPeu (rev = False)")
    tableaux = [[i, [derangeUnPeu(i, 10, False) for j in range(ech)]]
                for i in range(2, taille, pas)]
    courbes(algos, tableaux, styleLigne='-')
    affiche("Comparaison à l'aide de derangeUnPeu (rev = False)")

##############################################################
#
# Main
#


if __name__ == '__main__':
    trisInsertion = [triInsertionEchange,
                     triInsertionRotation, triInsertionRapide]
    trisLents = [triSelection, triBulles]

    sys.setrecursionlimit(4000)

    # Question 1.6

    testeQueLaFonctionTrie(triFusion)

    print("Exercice 1")
    algos = [triSelection]
    compareAlgos(algos)

    # Question 2.4

    print("Exercice 2")
    algos += trisInsertion + [triFusion, triBulles]
    compareAlgos(algos)

    ###################################################################
    ##### Commentez ici les résultats obtenus pour les différents #####
    ##### algorithmes sur les différents types de tableaux ############
    ###################################################################
    # Lorsqu'on utilise le randomPerm, l'algorithme le plus couteux est
    # le triBulles suivis du TriInsertionEchange, suivi des
    # TriSelection et TriInsertionRotation qui évolue à peu près
    # de la même façon, suivi du TriInsertionRapide et enfin le
    # triFusion
    #
    # Lorsqu'on utilise le randomTab, les résultats sont les mêmes
    # qu'avant
    #
    # Lorsqu'on utilise le derangeUnPeu avec rev = True, on a le
    # triInsertionEchange et triBulle qui sont plus proche, ainsi
    # que le triInsertionRapide et le triSelection qui sont plus proche
    #
    # Lorsqu'on utilise le derangeUnPeu avec rev = False, les
    # triSelection et triBulles sont plus couteux, suivis de plus bas
    # par le triFusion et enfin par le TriInsertionRapide et le
    # TriInsertionRotation
    ###################################################################

    # Question 3.3

    print("Exercice 3")
    algos = [triShell]
    compareAlgos(algos)

    # Question 3.4

    print("Comparaisons de tous les algos")
    algos = trisInsertion + trisLents + [triFusion, triShell]
    compareAlgos(algos, taille=2000, pas=200)

    ###################################################################
    ##### Commentez ici les résultats obtenus pour les différents #####
    ##### algorithmes sur les différents types de tableaux ############
    ###################################################################
    # Pour le randomPerm, le triShell est entre le triInsertionRapide
    # et ke triSelection (cela s'explique par le fait que on utilise
    # pas la recherche dichotomique pour le shell)
    #
    # Pour le randomTab, la place du triShell reste pareil
    #
    # Ensuite, pour le derangeUnPeu avec rev = True, il reste entre
    # le triRotation et le triRapide
    #
    # Enfin, le tri rest tout en bas avec les algorithmes de triFusin /
    # triRapide
    ###################################################################

    # compare les tris fusions et Shell

    print("Comparaisons des tris fusion et Shell")
    algos = [triFusion, triShell]
    compareAlgos(algos, taille=10000, pas=500)

    ###################################################################
    ##### Commentez ici les résultats obtenus pour les différents #####
    ##### algorithmes sur les différents types de tableaux ############
    ###################################################################
    # Le tri fusion reste toujours meilleur
    ###################################################################

    # comparaison sur tableaux presque triés

    print("\nComparaisons sur tableaux presque triés")
    algos = trisInsertion + [triFusion, triShell]
    compareAlgosSurTableauxTries(algos)

    ###################################################################
    ##### Commentez ici les résultats obtenus pour les différents #####
    ##### algorithmes sur les différents types de tableaux ############
    ###################################################################

    # Sur des tableaux presque tries, les tris insertion sont plus
    # efficace que le triFusion, le TriRapide reste meilleur que le
    # shell

    ###################################################################
