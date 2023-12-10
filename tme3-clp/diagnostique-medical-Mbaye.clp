;;; IAMSI 2023 : séance TME 3
;;; diagnostique-medical.clp


;; Les faits initiaux

; le patient a des tâches rouges 
; il a peu de boutons
; il ressent une sensation de froid
; il a une forte fièvre
; il a mal aux yeux 
; ses amygdales sont rouges 
; sa peau pèle et elle est sèche

(deffacts initial
	(initial-fact)
)
(defrule my-init
  (initial-fact)
=>
	(watch facts)
	(watch rules)
	(assert (taches-rouges))
	(assert (peu-boutons))
	(assert (sensation-froid))
	(assert (forte-fievre))
	(assert (yeux-douloureux))
	(assert (amygdales-rouges))
	(assert (peau-pele))
	(assert (peau-seche))
	(printout t "Fonction d'initialisation." crlf)
)

; si le sujet a peu ou beaucoup de boutons on dit qu’il a comme symptôme une  éruption cutanée
(defrule eruption-cutannee-par-bouton
  (or (peu-boutons) (beaucoup-boutons))
	=>
	(assert (eruption-cutannee))
)

; on dit que le sujet a un exanthème s’il a des  éruptions cutanées ou des rougeurs
(defrule exantheme-par-eruption-cutannee-ou-rougeur
	(or (eruption-cutannee) (rougeurs))
	=>
	(assert (exantheme))
)

; un sujet est dans un  état fébrile s’il a une forte fièvre ou s’il ressent une sensation de froid
(defrule etat-febrile-par-forte-fievre-ou-sensation-de-froid
	(or (forte-fievre) (sensation-froid))
	=>
	(assert (etat-febrile))
)

; le fait d’avoir les amygdales rouges, des tâches rouges et la peau qui pèle est un signe suspect
(defrule signe-suspect-par-amydales-rouges-taches-rouges-peau-pele
	(amygdales-rouges)
	(taches-rouges)
	(peau-pele)
	=>
	(assert (signe-suspect))
)

; la rougeole est diagnostiquée si le patient est dans un état fébrile et qu’il a des yeux douloureux et un exanthème
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

; s’il a peu de fièvre et peu de boutons, ce n’est pas la rougeole
(defrule pas-rougeole-annule-rougeole
	(pas-rougeole)
	?r <- (rougeole)
	=>
	(retract ?r)
)
(defrule pas-rougeole-1
	(peu-fievre)
	(peu-boutons)
	=>
	(assert (pas-rougeole))
)

; on relève une douleur si le patient a les yeux ou le dos douloureux
(defrule relever-douleur
	(yeux-douloureux)
	(dos-douloureux)
	=>
	(assert (douleur))
)

; la grippe est diagnostiquée si le sujet a le dos douloureux et un état fébrile
(defrule diagnostique-grippe
	(dos-douloureux)
	(etat-febrile)
	=>
	(assert (grippe))
)

; on peut diagnostiquer la rubéole et la varicelle si on a déjà déterminée qu’il ne s’agissait pas de la rougeole
(defrule diagnostique-rubeole-varicelle
	(pas-rougeole)
	=>
	(assert (rubeole))
	(assert (varicelle))
)

; si le sujet a de fortes démangeaisons et des pustules alors c’est la varicelle
(defrule varicelle-par-demangeaisons-pustules
	(fortes-demangeaisons)
	(pustules)
	=>
	(assert (varicelle))
)

; s’il a la peau sèche, une inflammation des ganglions mais ni pustules ni sensation de froid, c’est la rubéole
(defrule rubeole-par-peau-seche-etc
	(peau-seche)
	(inflammation-ganglions)
	(not (pustules))
	(not (sensation-froid))
	=>
	(assert (rubeole))
)


; ----- fin fichier diagnostique-medical.clp
