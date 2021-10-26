# QCM Generator by SquadTeam 2

## Définition du projet

* Développer une application en Python qui permet de stocker des questions et d’afficher des quizz. 
* L’objectif est de permettre à des utilisateurs qui le souhaite de s’entrainer sur des QCM. 

* Les fonctionnalités attendus seront les suivantes :
   * Pour les administrateurs / créateurs de QCM
      * Création de question (une question, entre 2 et 5 réponses, une bonne réponse)
      * Création de QCM à partir des questions
      * Création d’utilisateurs
   * Pour les utilisateurs
      * Se connecter
      * Choisir un QCM sur un sujet qui les intéresse
      * Effectuer le QCM
      * Revoir ses scores précédents

* L’application devra tourner dans une machine virtuelle sur le cloud. 
* Le code sera stocké dans un dépôt Git. 
* Une automatisation de l’intégration de l’application doit être faite (lancement de tests unitaires, contrôle qualité du code, build d’un package avec stockage dans un dépôt de paquet), avec une visualisation des résultats à chaque build.
* L’application devra être monitorer et les logs centralisés en un seul endroit et accessible à tous.
* Afin de déployer la VM de l’application, il est demander de produire un ou des playbooks Ansible pour faciliter le déploiement de l’application.
