# 📝 ToDo Django App

## 📌 Description
Cette application web permet à un utilisateur de gérer ses tâches personnelles.

Chaque utilisateur peut :
- créer un compte
- se connecter
- gérer ses propres tâches

---

## 🚀 Fonctionnalités

- 🔐 Authentification (inscription / connexion)
- ➕ Ajout de tâches
- ✏️ Modification de tâches
- ❌ Suppression de tâches
- ✔️ Marquer comme terminée
- ⚡ Priorité (Basse / Moyenne / Haute)
- 🏷️ Catégories (Études, Travail, Personnel, Autre)
- 📅 Deadline (date limite)


---

## 🛠️ Technologies utilisées

- Python
- Django
- HTML / CSS
- SQLite

---

## ⚙️ Installation

```bash
# Cloner le projet
git clone https://github.com/leilasayadi09-creator/todo-django-project.git

# Aller dans le dossier
cd todo-django-project

# Créer un environnement virtuel
python -m venv .venv

# Activer l’environnement
.venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Appliquer les migrations
python manage.py migrate

# Lancer le serveur
python manage.py runserver

# Resume 
git clone https://github.com/leilasayadi09-creator/todo-django-project.git
cd todo-django-project
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver