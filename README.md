# RGAA_conform
Mettre à terme à disposition des internautes un service web qui permette de tester le niveau de conformité d’un système d’information avec la réglementation en vigueur notamment celle du référentiel général d'amélioration de l'accessibilité dans la version en vigueur.

Permettre la création d’un tableau de bord du niveau de conformité de l’ensemble des Systèmes et indiquer ceux pouvant faire l’objet d’une sanction administrative. 

Ce tableau de bord devra être déclinable en version compréhensible par des personnes qui ne sont pas des experts en technologie de l'informaton et traduise l'impact du non respect des systèmes d'information dont ils sont responsables en évaluant le montant de la sanction administrative prévue par la réglementation.

Dans l'esprit il sera possible d'étendre le dispositif pour le rendre applicable aux obligations règlementaires relative au RGPD, mentions légales ... 

Tout site public se devant d'être conforme à la réglementation et la mise à disposition publique de ce type de service doit permettre à chacun d'évaluer par lui même la qualité d'un service public en ligne sans etre un expert web...

Tous les contributeurs à ce projet sont bienvenus, le langage retenu est python en v3,x

Présentation rapide des modules existants et en cours 

Un premier module list.py élabore un tableau créé à partir d'une liste de sites ou services web à tester.
Le teste porte sur la présence d'un lien présent sur la page d'accueil qui pointe vers une page dédiée à l'accessibilité conformément au RGAA,
le tableau est remplis automatiquement et les différentes colonnes sont renseignées en fonction du résultat des testes effectués dans le module.
Ce tableau sert de fichier d'entrée pour le module télécharge_webpage qui télécharge localement la page accessibilité des site pointés par le test précédent.
ce téléchargement local permet de traiter localement la page pour d'autre tests sans nécessiter un acces à internet. Cette page est sensée contenir toutes les informations importantes en matièere de contact .... qui font l'objet de modules spécifiques à développer selon l'objectif choisi exemple : présence des coordonnées du défenseur des droits, présence d'un point de contact pour les mesures compensatoires ... 
