## Question 1:
Implémentation en CLIPS dans le fichier diagnostique-medical.clp

## Question 2: En considérant les faits initiaux
f-1     (initial-fact)
f-2     (taches-rouges)
f-3     (peu-boutons)
f-4     (sensation-froid)
f-5     (forte-fievre)
f-6     (yeux-douloureux)
f-7     (amygdales-rouges)
f-8     (peau-pele)
f-9     (peau-seche)


En faisant (run 1) ; déduction de faits étape par étape
(run 1)
FIRE    1 signe-suspect-par-amydales-rouges-taches-rouges-peau-pele: f-7,f-2,f-8
==> f-10    (signe-suspect)
Nous observons l'ajout du fait f-10 (signe-suspect) par application de la règle signe-suspect-par-amydales-rouges-taches-rouges-peau-pele
à partir des faits f-7     (amygdales-rouges), f-2     (taches-rouges) et f-8     (peau-pele).

(run 1)
FIRE    1 rougeole-par-signe-suspect-ou-forte-fievre: f-10,f-5
==> f-11    (rougeole)
Nous obersons l'ajout du fait f-11 (rougeole) par application de la règle rougeole-par-signe-suspect-ou-forte-fievre à partir des faits
f-10    (signe-suspect) et f-5     (forte-fievre).

(run 1)
FIRE    1 etat-febrile-par-forte-fievre-ou-sensation-de-froid: f-5
==> f-12    (etat-febrile)
Nous observons l'ajout du fait f-12 (etat-febrile) par application de la règle etat-febrile-par-forte-fievre-ou-sensation-de-froid sur le fait
f-5     (forte-fievre).

(run 1)
FIRE    1 etat-febrile-par-forte-fievre-ou-sensation-de-froid: f-4
f-12    (etat-febrile) déjà présent donc la règle n'en rajoute pas un nouveau.

(run 1)
FIRE    1 eruption-cutannee-par-bouton: f-3
==> f-13    (eruption-cutannee)
Nous observons l'ajout du fait f-13    (eruption-cutannee) par application de la règle eruption-cutannee-par-bouton sur le fait f-3     (peu-boutons).

(run 1)
FIRE    1 exantheme-par-eruption-cutannee-ou-rougeur: f-13
==> f-14    (exantheme)
Nous observons l'ajout du fait f-14    (exantheme) par application de la règle exantheme-par-eruption-cutannee-ou-rougeur sur le fait f-13    (eruption-cutannee)

(run 1)
FIRE    1 diagnostique-rougeole-etat-febrile-yeux-douloureux-exantheme: f-12,f-6,f-14
Le fait f-11    (rougeole) déjà présent.

FIN.

## Question 3:
Nous constatons que la stratégie de CLIPS est de choisir la règle qui a été définit en premier quand plusieurs règles sont appliquables.

## Question 4:
CLIPS procède par un chainage avant.

## Question 5: Saturation de la base de fait.
==> f-10    (signe-suspect)
==> f-11    (rougeole)
==> f-12    (etat-febrile)
==> f-13    (eruption-cutannee)
==> f-14    (exantheme)

## Question 6:
On considère les faits initiaux :
f-1     (initial-fact)
f-2     (taches-rouges)
f-3     (peu-boutons)
f-4     (sensation-froid)
f-5     (forte-fievre)
f-6     (yeux-douloureux)
f-7     (amygdales-rouges)
f-8     (peau-pele)
f-9     (peau-seche)

## Pour le fait f-10    (signe-suspect)
Nous avons une seule règle qui peut la conclure: signe-suspect-par-amydales-rouges-taches-rouges-peau-pele
(defrule signe-suspect-par-amydales-rouges-taches-rouges-peau-pele
	(amygdales-rouges)
	(taches-rouges)
	(peau-pele)
	=>
	(assert (signe-suspect))
)
Cette règle requiert les faits : (amygdales-rouges),(taches-rouges),(peau-pele)
or celles-ci sont présentent dans notre base des faits: f-7,f-2,f-8. Donc on peut l'appliquer pour prouver f-10    (signe-suspect)

## Pour le fait f-11    (rougeole)
Nous avons deux règles pour la trouver:
(defrule diagnostique-rougeole-etat-febrile-yeux-douloureux-exantheme
	(etat-febrile)
	(yeux-douloureux)
	(exantheme)
	=>
	(assert (rougeole))
)
;, ou bien s’il a un signe suspect et une forte fièvre
(defrule rougeole-par-signe-suspect-ou-forte-fievre
	(signe-suspect)
	(forte-fievre)
	=>
	(assert (rougeole))
)
Le fait f-5     (forte-fievre) est déjà présent dans la base de fait et on a précédemment que l'on peut prouver f-10    (signe-suspect) par la règle 
signe-suspect-par-amydales-rouges-taches-rouges-peau-pele. Donc on peut prouver f-11    (rougeole).

## Pour le fait f-12    (etat-febrile)
Il existe une seule règle pour déterminer cet état:
(defrule etat-febrile-par-forte-fievre-ou-sensation-de-froid
	(or (forte-fievre) (sensation-froid))
	=>
	(assert (etat-febrile))
)
Pour que cette règle soit appliquable, il y'a besoin du fait (forte-fievre) ou de (sensation-froid). Or ces deux faits déjà présents dans la base.
Donc par suite nous avons f-12    (etat-febrile).

## Pour le fait f-13    (eruption-cutannee)
Nous avons une seule règle pour donner le but (eruption-cutannee):
(defrule eruption-cutannee-par-bouton
  (or (peu-boutons) (beaucoup-boutons))
	=>
	(assert (eruption-cutannee))
)
Pour appliquer cette règle nous avons besoin du fait (peu-boutons) ou (beaucoup-boutons). Or le fait f-3     (peu-boutons) est déjà présent dans notre base
de faits. Donc nous pouvons atteindre le but (eruption-cutannee) en appliquant cette règle.

## Pour le fait f-14    (exantheme)
Nous avons une seule règle pour trouver ce but:
(defrule exantheme-par-eruption-cutannee-ou-rougeur
	(or (eruption-cutannee) (rougeurs))
	=>
	(assert (exantheme))
)
Cette règle pour qu'elle soit appliquable a besoin du fait (eruption-cutannee) ou (rougeurs).
Pour le fait (eruption-cutannee) nous avons vu précedemment qu'on pouvait le trouver par la règle eruption-cutannee-par-bouton sur le fait (peu-boutons).
Donc nous avons bien le but (exantheme).