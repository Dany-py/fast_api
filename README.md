# FastAPI Project

Bienvenue dans ce projet utilisant **FastAPI**, un framework moderne, rapide et performant pour la création d'API en Python.
Cette api à été créer dans le cadre d'un projet Rasa IA.

## 📌 Fonctionnalités
- ⚡ Basé sur FastAPI pour des performances optimales
- 📂 Gestion des routes et des endpoints API
- 🛠️ Intégration avec des bases de données (si applicable)
- 🏗️ Architecture modulaire et évolutive

## 🚀 Installation et Utilisation

### Prérequis
- **Python 3.7+**
- **pip**

### Installation
```sh
# Clone du projet
git clone https://github.com/Dany-py/fast_api.git
cd fast_api

# Création et activation de l'environnement virtuel
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate

# Installation des dépendances
pip install -r requirements.txt
```

### Lancer le serveur FastAPI
```sh
uvicorn main:app --reload
```

L'API sera accessible sur : [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Documentation automatique
FastAPI génère automatiquement la documentation interactive :
- **Swagger UI** : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc** : [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🛠️ Structure du projet
```
fast_api/
│── main.py          # Point d'entrée de l'application
│── models.py        # Modèles de données (si applicable)
│── templates/       # Répertoire de fichier HTML
│── requirements.txt # Dépendances du projet
```

## ✅ Contribuer
Les contributions sont les bienvenues ! Pour proposer une amélioration :
1. **Fork** le projet
2. Crée une **branche** (`git checkout -b feature/ma-fonctionnalite`)
3. Fait tes modifications et **commit** (`git commit -m 'Ajout d'une nouvelle fonctionnalité'`)
4. **Push** la branche (`git push origin feature/ma-fonctionnalite`)
5. Ouvre une **Pull Request**

## 📜 Licence
Ce projet est sous licence **MIT**. Voir [LICENSE](LICENSE) pour plus de détails.

---

🚀 **Développé avec FastAPI par [Dany-py](https://github.com/Dany-py)**

