# ✈️ Segmentation de la Satisfaction Client dans l’Aviation avec SOM

## 🧠 Contexte

Dans le secteur aérien, la satisfaction client est un levier stratégique de fidélisation et de rentabilité.  
Ce projet vise à identifier des **segments homogènes de voyageurs** à partir de leurs retours d’expérience afin d’**améliorer les services proposés**.  
Pour cela, nous exploitons une base de données issue d’une enquête de satisfaction post-vol.

---

## 📊 Données

Le jeu de données utilisé est un fichier `.csv` contenant des **informations démographiques**, des **caractéristiques de voyage**, ainsi que des **évaluations de différents services** (wifi à bord, confort, nourriture, divertissement, etc.).

### Variables principales :

| Variable                       | Description |
|-------------------------------|-------------|
| `id`                          | Identifiant unique |
| `Gender`                      | Sexe du passager |
| `Customer Type`              | Type de client (loyal ou occasionnel) |
| `Age`                         | Âge du passager |
| `Type of Travel`              | Voyage personnel ou professionnel |
| `Class`                       | Classe de voyage (Eco, Business…) |
| `Flight Distance`             | Distance du vol |
| `Inflight wifi service`       | Note du wifi à bord |
| `Seat comfort`                | Confort du siège |
| `Food and drink`             | Qualité des repas |
| `Inflight entertainment`     | Divertissements à bord |
| `Checkin service`, `Baggage handling`, `Cleanliness`... | Autres services évalués |
| `Departure Delay in Minutes` | Retard au départ |
| `Arrival Delay in Minutes`   | Retard à l’arrivée |
| `satisfaction`               | Satisfaction globale (Positive / Negative) |

---

## 🎯 Objectifs

- 🔧 **Prétraitement** : Nettoyage, gestion des valeurs manquantes, normalisation, encodage.
- 🔍 **Sélection des variables** : Choix des variables les plus pertinentes pour le clustering.
- 🧬 **Clustering avec SOM** (Self-Organizing Maps) : Segmentation non-supervisée de profils similaires.
- 📈 **Analyse des clusters** : Caractérisation des groupes et mise en lumière de tendances.
- 🧾 **Rapport** : Présentation des méthodes, résultats, et recommandations stratégiques.

---

## 🛠️ Technologies utilisées

- Python 3.12
- Pandas, NumPy, Scikit-learn
- MiniSom (Self-Organizing Maps)
- Matplotlib / Seaborn
- Jupyter Notebook

---

## 🧪 Résultats attendus

- Une segmentation claire de profils clients basés sur leur niveau de satisfaction.
- Des **recommandations opérationnelles** pour l’amélioration des services aériens selon les segments détectés.

---

## 📁 Arborescence du projet


projet_segmentation_satisfaction/

├── data/ # Données brutes et nettoyées

├── notebooks/ # Analyses exploratoires (EDA)

├── models/ # SOM entraîné et paramètres

├── api/ # Code d'API pour intégrer les résultats (optionnel)

├── outputs/ # Graphiques et visualisations

├── requirements.txt # Dépendances Python

└── README.md # Documentation du projet


---

## 📄 Livrables

- ✅ Le **code source complet** (prétraitement, clustering SOM, visualisations).
- ✅ Un **rapport PDF** détaillant :
  - Méthodologie
  - Justifications des choix techniques
  - Interprétation des clusters
  - Recommandations pour améliorer la satisfaction client

---

## 📬 Contact

Pour toute question : [447578@etud.uco.fr](mailto:447578@etud.uco.fr)  
Projet réalisé par **Bouda Pascal** – Étudiant en Data Science – UCO Angers

---

