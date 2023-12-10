# Exercice 1

La traduction de la formule F de l'exercie 2 est dans le fichier exercice2-Mbaye.cnf.
bin/glucose_static tme4-Mbaye/exercice2.cnf nous rend bien s UNSATISFIABLE.

La traduction de la première formule de l'exercice 4 du Td se trouve dans le fichier exercice4-1-Mbaye.cnf.
bin/glucose_static -model tme4-Mbaye/exercice4-1-Mbaye.cnf nous rend:
s SATISFIABLE
v 1 -2 -3 4 -5 -6 7 -8 0. 
La formule est satisfiable avec {x1,-x2,-x3,x4,-x5,-x6,x7,-x8}.

La traduction de la deuxième formule de l'exercice 4 du Td se trouve dans le fichier exercice4-2-Mbaye.cnf.
bin/glucose_static -model tme4-Mbaye/exercice4-2-Mbaye.cnf nous rend:
s SATISFIABLE
v 1 -2 -3 4 5 -6 -7 -8 -9 10 -11 12 -13 -14 -15 -16 0
La formule est satisfiable avec {x1, -x2, -x3, x4, x5, -x6, -x7, -x8, -x9, x10, -x11, x12, -x13, -x14, -15, -x16}.