# Excel Data Manager

## Description
Cette application web permet d'importer, de visualiser, de modifier, de créer et d'exporter des données d'employés à partir de fichiers Excel, en respectant les contraintes du challenge.

## Sommaire
- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [API Web (routes)](#api-web-routes)
- [Choix techniques](#choix-techniques)
- [Commentaires](#commentaires)
- [Auteur](#auteur)

## Fonctionnalités
- Importation de fichiers Excel contenant les employés (nom, prénom, email, téléphone, date de naissance, salaire)
- Création, modification, visualisation et exportation des employés via une interface web responsive
- Stockage dans une base de données relationnelle (SQLite par défaut)
- Interface d'administration Django pour la gestion avancée

## Installation
1. Clonez le dépôt et placez-vous dans le dossier du projet :
   ```bash
   git clone <repo_url>
   cd Gestion_de_tables/excel_manager
   ```
2. Installez les dépendances :
   ```bash
   pip install django pandas openpyxl
   ```
3. Appliquez les migrations :
   ```bash
   python manage.py migrate
   ```
4. Lancez le serveur de développement :
   ```bash
   python manage.py runserver
   ```
5. Accédez à l'application sur [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Utilisation
- Utilisez le menu pour importer un fichier Excel (voir le format attendu dans l'interface).
- Consultez, créez, modifiez ou exportez la liste des employés.
- Accédez à l'admin Django via `/admin` (créez un superuser avec `python manage.py createsuperuser`).

## API Web (routes)
L'application propose les routes suivantes :

| Méthode | URL                          | Description                                      |
|---------|------------------------------|--------------------------------------------------|
| GET     | `/`                          | Page d'accueil                                   |
| GET/POST| `/importer/`                 | Importer un fichier Excel                        |
| GET     | `/employees/`                | Liste des employés                               |
| GET/POST| `/employee/creer/`           | Créer un nouvel employé                          |
| GET/POST| `/employee/<int:pk>/modifier/` | Modifier un employé existant                   |
| GET     | `/exporter/`                 | Exporter la liste des employés au format Excel   |
| GET/POST| `/admin/`                    | Interface d'administration Django                |

### Exemple d'usage
- Pour créer un employé, accédez à `/employee/creer/` et remplissez le formulaire.
- Pour modifier un employé, cliquez sur « Modifier » dans la liste ou accédez à `/employee/<id>/modifier/`.
- Pour importer, allez sur `/importer/` et chargez un fichier Excel conforme.
- Pour exporter, cliquez sur « Exporter vers Excel » ou accédez à `/exporter/`.

## Choix techniques
- **Django** : framework web robuste, gestion native des modèles relationnels et de l'admin.
- **Pandas** : pour la lecture et l'écriture efficace des fichiers Excel.
- **Bootstrap** : pour une interface responsive et moderne.
- **Modèle Employee** : correspond à la table SQL `employees` avec les champs demandés.

## Modèle Employee (mise à jour)

- Le champ `salaire` accepte désormais jusqu'à 50 chiffres (48 avant la virgule, 2 après), ce qui permet de saisir des montants très élevés sans aucune limite pratique.
- Il n'y a plus de contrainte sur la positivité ou la taille du salaire.

## Commentaires
- Le code est commenté pour faciliter la compréhension.
- L'importation vérifie la présence de toutes les colonnes requises.
- L'exportation génère un fichier Excel conforme à la structure de la base.
- La création et la modification utilisent le même formulaire pour la cohérence UX.

## Améliorations UX spécifiques

- **Champ date avec calendrier** : Lors de la création ou modification d’un employé, le champ « date de naissance » utilise un calendrier interactif pour faciliter la saisie.
- **Champ salaire avec formatage automatique** :
    - À la saisie, le champ salaire se formate automatiquement avec séparateur de milliers et deux décimales (ex : `1 234 567.00`).
    - La devise « FCFA » (XAF) est affichée à côté du champ dans le formulaire et dans la liste des employés.
    - À l’affichage, tous les montants sont formatés pour une meilleure lisibilité.

## Documentation API interactive (Swagger & Redoc)

Une documentation interactive de l’API REST est disponible :
- Swagger UI : [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- Redoc : [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

Vous pouvez tester toutes les routes de l’API, voir les schémas, et effectuer des requêtes directement depuis l’interface.

### Endpoints REST principaux
- `GET /api/employees/` : liste des employés
- `POST /api/employees/` : créer un employé (le champ `salaire` accepte jusqu'à 50 chiffres)
- `GET /api/employees/{id}/` : détails d’un employé
- `PUT/PATCH /api/employees/{id}/` : modifier un employé (aucune limite sur le montant du salaire)
- `DELETE /api/employees/{id}/` : supprimer un employé

## Auteur
- [Heinrich Pro] 
