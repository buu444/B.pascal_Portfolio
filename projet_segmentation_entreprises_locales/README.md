# Segmentation Client DIGNAMIK


📌 **Contexte du projet**  
Dans un marché en constante évolution, DIGNAMIK — entreprise spécialisée dans l'accompagnement digital des acteurs économiques locaux — souhaite mieux comprendre ses clients pour proposer des services plus personnalisés. Ce projet a pour but de segmenter les entreprises clientes à l’aide de techniques de clustering non supervisé afin d’identifier des groupes homogènes d’entreprises.

⚠️ **Projet réel**  
Ce projet est issu d'un cas réel réalisé dans un cadre professionnel. Les données complètes ne sont pas disponibles publiquement pour des raisons de confidentialité.

---
## 🎯 Objectifs

- Segmenter les entreprises selon des critères comportementaux et sectoriels ;
- Proposer des recommandations marketing ciblées pour chaque segment ;
- Améliorer la fidélisation et l’acquisition client ;
- Fournir un accès centralisé aux résultats via une API dédiée.

---

## 🏢 À propos de DIGNAMIK

Fondée en **2020**, DIGNAMIK accompagne les commerçants, artisans et prestataires dans leur transformation digitale, à travers :

- Des services de communication digitale (SEO, réseaux sociaux, sites web) ;
- Le média de proximité **Viemaville** ;
- Un accompagnement personnalisé à plus de **1500 clients** dans toute la France.

---

## 🔍 Données

- **Source** : Base de données interne DIGNAMIK enrichie avec l’ORM Prisma.
- **Effectif analysé** : 421 clients actifs (sur ~1600).
- **Variables clés** :
  - Type d’entreprise (boutique, service, restaurant, etc.)
  - Secteur d’activité
  - Engagement réseaux sociaux (nombre d’abonnés par plateforme)
  - Chiffre d’affaires (via la table `turnover`)
  - Ville / localisation

---

## ⚙️ Prétraitement

- Suppression des doublons et gestion des valeurs manquantes ;
- Imputation des données (moyenne ou valeur modale) ;
- Encodage des variables catégorielles (`category_name`) ;
- Normalisation des variables continues (`followers_*`, `turnover`) ;
- Construction de pipelines avec `scikit-learn` (`ColumnTransformer`, `Pipeline`).

---

## 🧠 Méthodologie

- **Modèle** : KMeans (`scikit-learn`)
- **Nombre optimal de clusters** : déterminé par la méthode du coude et le **coefficient de silhouette** → `n_clusters = 4`
- **Réduction de dimension** : PCA pour la visualisation 2D
- **API** : Intégration du modèle dans une API permettant de :
  - Visualiser dynamiquement les segments
  - Filtrer les entreprises par secteur, localisation…
  - Accéder à des recommandations personnalisées

---

## 📊 Visualisation et Interprétation

- **PCA** utilisée pour la projection 2D des clusters
- **Visualisation interactive** via l’API (tableau + carte)
- **Profils-types identifiés** :
  - **Cluster 1** : Restauration, forte notoriété digitale
  - **Cluster 2** : Jeunes services peu visibles numériquement
  - **Cluster 3** : Commerces de proximité à fidéliser
  - **Cluster 4** : Petites structures multi-sectorielles, peu engagées

---

## 🗂️ Structure du dépôt

```bash
segmentation-client-dignamik/
├── data/                  # Données utilisées (nettoyées / originales)
├── notebooks/             # Analyses exploratoires & visualisation
├── models/                # Sauvegarde des modèles KMeans / pipelines
├── api/                   # Code API (FastAPI / Flask)
├── utils/                 # Scripts de transformation / helpers
├── outputs/               # Graphiques, cluster summaries, résultats
├── README.md              # Ce fichier
└── requirements.txt       # Dépendances Python
```

---

## 🧪 Reproductibilité

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/ton-projet/segmentation-client-dignamik.git
   cd segmentation-client-dignamik
   ```

2. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

3. Lancer l’analyse :
   - Via les notebooks dans le dossier `notebooks/`
   - Puis déployer l’API via `api/`

---

## 🛠️ Technologies utilisées

- Python
- scikit-learn
- pandas, numpy
- matplotlib, seaborn
- FastAPI (ou Flask)
- PostgreSQL
- Prisma ORM

---

## 📬 Contact

**Pascal Bouda**  
Étudiant en Data Science — Université Catholique de l’Ouest  
📧 bouda.pascal@uco.fr
