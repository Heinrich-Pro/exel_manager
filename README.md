# Excel Data Manager

## Description

Cette application web permet d'importer, de visualiser, de modifier, de créer, de supprimer et d'exporter des données d'employés à partir de fichiers Excel, en respectant les contraintes du challenge. Elle propose une interface web responsive, une API REST documentée (Swagger/Redoc), et gère les salaires en FCFA sans limite de montant.

## Sommaire
- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [API Web & Documentation interactive](#api-web--documentation-interactive)
- [Modèle Employee](#modèle-employee)
- [Améliorations UX spécifiques](#améliorations-ux-spécifiques)
- [Choix techniques](#choix-techniques)
- [Auteur](#auteur)

## Fonctionnalités
- Importation de fichiers Excel contenant les employés (nom, prénom, email, téléphone, date de naissance, salaire)
- Création, modification, suppression (avec confirmation) et visualisation des employés via une interface web responsive
- Exportation de la liste des employés au format Excel
- API REST complète (CRUD) avec documentation interactive (Swagger/Redoc)
- Interface d'administration Django pour la gestion avancée
- Gestion de très grands salaires (jusqu'à 50 chiffres)

## Installation
1. Clonez le dépôt et placez-vous dans le dossier du projet :
   ```bash
   git clone <https://github.com/Heinrich-Pro/exel_manager.git>
   cd Gestion_de_tables/excel_manager
   ```
2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
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
- Consultez, créez, modifiez, supprimez ou exportez la liste des employés.
- Accédez à l'admin Django via `/admin` (créez un superuser avec `python manage.py createsuperuser`).

## API Web & Documentation interactive
L'application propose une API REST complète, documentée et testable via Swagger et Redoc :
- Swagger UI : [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- Redoc : [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

### Principales routes web et API
| Méthode  | URL                                 | Description                                      |
|----------|-------------------------------------|--------------------------------------------------|
| GET      | `/`                                 | Page d'accueil                                   |
| GET/POST | `/importer/`                        | Importer un fichier Excel                        |
| GET      | `/employees/`                       | Liste des employés                               |
| GET/POST | `/employee/creer/`                  | Créer un nouvel employé                          |
| GET/POST | `/employee/<int:pk>/modifier/`      | Modifier un employé existant                     |
| GET/POST | `/employee/<int:pk>/supprimer/`     | Supprimer un employé (avec confirmation)         |
| GET      | `/exporter/`                        | Exporter la liste des employés au format Excel   |
| GET/POST | `/admin/`                           | Interface d'administration Django                |
| GET      | `/api/employees/`                   | Liste des employés (API REST)                    |
| POST     | `/api/employees/`                   | Créer un employé (API REST, salaire jusqu'à 50 chiffres) |
| GET      | `/api/employees/{id}/`              | Détails d’un employé (API REST)                  |
| PUT/PATCH| `/api/employees/{id}/`              | Modifier un employé (API REST)                   |
| DELETE   | `/api/employees/{id}/`              | Supprimer un employé (API REST)                  |

### Exemple d'usage
- Pour créer un employé, accédez à `/employee/creer/` ou utilisez l'API REST.
- Pour modifier ou supprimer, utilisez les boutons dans la liste ou l'API REST.
- Pour importer, allez sur `/importer/` et chargez un fichier Excel conforme.
- Pour exporter, cliquez sur « Exporter vers Excel » ou accédez à `/exporter/`.

## Modèle Employee (mise à jour)
- Le champ `salaire` accepte désormais jusqu'à 50 chiffres (48 avant la virgule, 2 après), ce qui permet de saisir des montants très élevés sans aucune limite pratique.
- Il n'y a plus de contrainte sur la positivité ou la taille du salaire.
- Les autres champs sont : nom, prénom, email (unique), téléphone, date de naissance, date de création/modification.

## Améliorations UX spécifiques
- **Champ date avec calendrier** : Lors de la création ou modification d’un employé, le champ « date de naissance » utilise un calendrier interactif pour faciliter la saisie.
- **Champ salaire** :
    - Saisie uniquement numérique (chiffres, point, virgule).
    - Affichage formaté (séparateur de milliers, deux décimales, FCFA) dans la liste.
    - Aucune limite sur le montant.
- **Suppression** : Confirmation systématique avant suppression d’un employé.

## Choix techniques
- **Django** : framework web robuste, gestion native des modèles relationnels et de l'admin.
- **Django REST Framework** : API RESTful puissante et flexible.
- **drf-yasg** : documentation Swagger/Redoc automatique.
- **Pandas & openpyxl** : lecture/écriture efficace des fichiers Excel.
- **Bootstrap** : interface responsive et moderne.
- **Sécurité** : confirmation pour la suppression, validation des champs.

## Auteur
- [Heinrich Pro] 
