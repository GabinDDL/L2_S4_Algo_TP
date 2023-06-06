#!/usr/bin/env python3


# 1) Si la variable n'est pas définit, le programme ne connait pas la variable alors que si quand on lui attribut une valeur, meme null
print("Ex 1")
Z = None
print(Z) # renvoie None
del Z
# print(val) # val n'est plus definit et renvoie une erreur

# 2)
print("Ex 2")
Z = ""
expression2 = True if Z == None else False
print(expression2)
Z = None
expression2 = True if Z == None else False
print(expression2)

# 3)
print("Ex 3")
expression3 = "sans valeur" if Z == None else "chaine vide" if Z == "" else "autre"
print(expression3)
Z = ""
expression3 = "sans valeur" if Z == None else "chaine vide" if Z == "" else "autre"
print(expression3)

# 4)
# 3 -> True
# -5 -> False
# None -> None

#
# Expression conditionnelle
# retourne True si x > 0, False si x <= 0 ou si x vaut None
def expression_5(x) :
    # A REMPLIR
    return False if x == None else x>0


#
# AJOUTER D'AUTRES TESTS
#  [valeur_x, resultat_attendu]
def testData():
	return [[5, True], [None, False], [-2, False], [-3.4, False]]


#
# NE PAS MODIFIER
#
def testExpr(data) :
	score = 0
	ldata = len(data)
	for i, dt in enumerate(data) :
		print('  test %d/%d : ' % (i + 1, ldata), end='')
		x = dt[0]
		refr = dt[1]
		r = expression_5(x)
		if r == refr :
			score+=1
			print('ok')
		else :
			print('ECHEC')
			print('    entree  : %s' % x)
			print('    calcule : %s' % r)
			print('    attendu : %s' % refr)

	print('Score %d/%d' % (score, ldata))


if __name__ == '__main__':
	testExpr(testData())
