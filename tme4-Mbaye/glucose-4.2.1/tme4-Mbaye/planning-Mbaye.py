#!/usr/bin/python3
# -*- coding: utf-8 -*- 

def codage(ne,nj,j,x,y):
  if (nj <= j) or (ne <= x) or (ne <= y):
    return -1
  return j * (ne**2) + x*ne + y + 1

def decodage(k,ne):
  k -= 1  # k = j * (ne**2) + x*ne + y = ne(j*ne+x) + y
  y = k % ne
  k -= y  # k = = ne(j*ne+x)
  k = k // ne # k = j*ne+x
  x = k % ne
  j = k // ne
  
  return j,x,y

def clauses_format_dimacs(contraintes):
  """On reçoit une liste des clauses et on transforme les nombres en chaine de caractères et on ajoute le zéro de fin de ligne

  Args:
      contraintes (list[list]): liste de liste d'entiers, chaque sous liste est une clause représentée par ses entiers le composant

  Returns:
      str: retourne une chaine de caractères représentant toutes les contraintes de tous les clauses dans le format DIMACS
  """
  contraintes_s = []
  for cont in contraintes:
    cont_s = [str(x) for x in cont]
    cont_s = " ".join(cont_s) + " 0"
    contraintes_s.append(cont_s)
  
  return "\n".join(contraintes_s)

def generer_fichier_dimacs(ne,nj,clauses,nom_fic):
  with open(nom_fic,'w') as f:
    f.write('c Planning match\n')
    f.write(f"p cnf {nj*ne*ne} {len(clauses)}\n")
    f.write(clauses_format_dimacs(clauses))

def au_moins(l):
  return  [[x for x in l]]  # rend une liste de contraintes (ici un seul élément dans la liste)


def au_plus(l):
  # rend la liste des contraintes (sans le zéro à la fin, on l'ajoutera quand on convertira en chaine de caractère)
  contraintes = []
  for i in range(len(l)-1):
    x = l[i]
    for y in l[1+i:]:
      contraintes.append([-x,-y])
  
  return contraintes

def equipe_match_par_jour(ne,nj,j,x):
  # tous matchs possible avec x le jour j
  l = [codage(ne,nj,j,x,y) for y in range(ne) if y!=x] + [codage(ne,nj,j,y,x) for y in range(ne) if y!=x]

  return [[-codage(ne,nj,j,x,x)]] + au_plus(l)  # une équipe ne peut jouer contre elle même

def encoderC1(ne,nj):
  clauses = []
  for j in range(nj):
    for x in range(ne):
      clauses.extend(equipe_match_par_jour(ne,nj,j,x))
      
  return clauses

def encoderC2(ne,nj):
  clauses = []
  # pour chaque couple d'équipe x!=y
  for x in range(ne):
    for y in range(x+1,ne):
      lx = [codage(ne,nj,j,x,y) for j in range(nj)] # sur le terrain de x
      ly = [codage(ne,nj,j,y,x) for j in range(nj)] # sur le terrain de y

      # au moins un match sur le terrain de x et y aussi
      au_m_x = au_moins(lx)
      au_m_y = au_moins(ly)

      # au plus un match sur chaque terrain
      au_p_x = au_plus(lx)
      au_p_y = au_plus(ly)

      # on les ajoute dans l'ensemble des clauses
      clauses.extend(au_m_x)
      clauses.extend(au_m_y)
      clauses.extend(au_p_x)
      clauses.extend(au_p_y)
  
  return clauses

def encoder(ne,nj):
  return encoderC1(ne,nj) + encoderC2(ne,nj)

def decoder_fichier(ne,fic_glucose,fic_noms_eq=False,fic_planning=False):
  # traduction du résultat
  lm = []
  with open(fic_glucose,"r") as f:
    l = f.readline()
    lk = l.split(" ")
    for k in lk:
      k = int(k)
      if k > 0:
        lm.append(decodage(k,ne))
  
  noms = []
  # lecture des noms des équipes
  if fic_noms_eq != False:
    with open(fic_noms_eq,"r") as f:
      noms = f.readlines()
    for i in range(len(noms)):
      noms[i] = noms[i][:-1]
  else:
    # si pas de noms d'équipes donnés(noms par défaut)
    noms = [f"equipe {i}" for i in range(1,1+ne)]
  
  # ecriture dans le fichier de planning des matchs du championnat
  if fic_planning != False:
    with open(fic_planning,"w") as f:
      f.write("Planning des matchs du championnat:\n")
      j0 = -1
      for j,x,y in lm:
        if j != j0:
          j0 = j
          f.write(f"\nJournée {j+1} :\n")
        
        f.write(f"\t{noms[x]} vs {noms[y]}\n")
  else:
    # Affichage si pas de noms de fichier de sortie
    print("Planning des matchs du championnat:\n\n")
    j0 = -1
    for j,x,y in lm:
      if j != j0:
        j0 = j
        print(f"\nJournée {j+1} :\n")
      
      print(f"\t{noms[x]} vs {noms[y]}\n")    

# Main du script

import sys
import  os

if len(sys.argv) < 3:
  print("Usage 1:",sys.argv[0],"<nombre d'équipes> <nombre de jours>")
  print("Usage 2:",sys.argv[0],"<nombre d'équipes> <nombre de jours> <nom fichier noms équipes>")
  print("Usage 3:",sys.argv[0],"<nombre d'équipes> <nombre de jours> <nom fichier noms équipes>  <nom fichier planning>")
  exit()

ne = int(sys.argv[1])
nj = int(sys.argv[2])
fic_noms_eq = False
fic_planning = False
if len(sys.argv) > 3:
  fic_noms_eq = sys.argv[3]
if len(sys.argv) > 4:
  fic_planning = sys.argv[4]

clauses = encoder(ne,nj)
generer_fichier_dimacs(ne,nj,clauses,f"tme4-Mbaye/log/match-championnat-{ne}-{nj}.cnf")

#appel à glucose
commande = f"bin/glucose_static tme4-Mbaye/log/match-championnat-{ne}-{nj}.cnf tme4-Mbaye/log/sortie-glucose-{ne}-{nj}.txt > tme4-Mbaye/log/out"
os.system(commande)

decoder_fichier(ne,f"tme4-Mbaye/log/sortie-glucose-{ne}-{nj}.txt",fic_noms_eq,fic_planning)