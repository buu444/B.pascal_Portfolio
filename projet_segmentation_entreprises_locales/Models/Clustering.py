# Importation des bibliothèques nécessaires
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.cluster import KMeans
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
import json


# Chargement du fichier CSV contenant les données des entreprises
df = pd.read_csv("C:/Users/buupa/Desktop/PORTOFOLIO/PROJET_X/entreprise.csv")

# Définition des variables numériques et catégorielles à utiliser
numerical_features = ['followers_total', 'followers_facebook', 'followers_instagram', 'followers_tiktok']
categorical_features = ['category_name']

# Pipeline pour les variables numériques : imputation des valeurs manquantes + standardisation
numerical_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

# Pipeline pour les variables catégorielles : imputation + encodage one-hot
categorical_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Combinaison des deux pipelines via ColumnTransformer
preprocessor = ColumnTransformer([
    ('num', numerical_pipeline, numerical_features),
    ('cat', categorical_pipeline, categorical_features)
])

# Pipeline complet : prétraitement + clustering KMeans
pipeline = Pipeline([
    ('prep', preprocessor),
    ('kmeans', KMeans(n_clusters=4, random_state=42))
])

# Entraînement du pipeline sur les données
pipeline.fit(df)

# Ajout des labels de cluster au DataFrame
df['cluster'] = pipeline.named_steps['kmeans'].labels_

# Sauvegarde du DataFrame enrichi
df.to_csv("entreprises_clusterisées.csv", index=False)

# Aperçu rapide
print(df[['category_name', 'cluster']].head())

# Moyenne des followers par cluster
followers_columns = ['followers_total', 'followers_facebook', 'followers_instagram', 'followers_tiktok']
moyennes = df.groupby('cluster')[followers_columns].mean().round(1)
print("\nMoyenne des followers par cluster :\n", moyennes)

# Top 3 catégories d'activité par cluster
principales_categories = df.groupby('cluster')['category_name'].value_counts().groupby(level=0).head(3)
print("\nPrincipales catégories par cluster :\n", principales_categories)

# Réduction de dimension via PCA pour visualisation
X_transformed = pipeline.named_steps['prep'].transform(df)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_transformed)

plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=df['cluster'], cmap='viridis')
plt.title('Visualisation des clusters (PCA)')
plt.xlabel('Composante 1')
plt.ylabel('Composante 2')
plt.colorbar(label='Cluster')
plt.grid(True)
plt.show()

# Fonction de recommandation par cluster et ville
def recommander_par_cluster_ville(df):
    recommandations = {}

    for (cluster, city), group in df.groupby(['cluster', 'city_id']):
        moy = group[['followers_facebook', 'followers_instagram', 'followers_tiktok']].mean()
        top_cat = group['category_name'].value_counts().idxmax().lower()

        reco = []

        # Réseau dominant
        if moy['followers_instagram'] > moy[['followers_facebook', 'followers_tiktok']].max():
            reco.append("Renforcer les campagnes Instagram : jeux concours, reels engageants, partenariats avec influenceurs locaux.")
        elif moy['followers_facebook'] > moy[['followers_instagram', 'followers_tiktok']].max():
            reco.append("Mettre l'accent sur Facebook : publications régulières, groupes locaux, publicités ciblées.")
        else:
            reco.append("Explorer TikTok : vidéos tendances, challenges, contenu divertissant lié à l’activité.")

        # Catégorie dominante
        if "restaurant" in top_cat:
            reco += [
                "Partager des photos de plats du jour, stories en cuisine.",
                "Promouvoir les avis clients et les événements spéciaux.",
                "Utiliser les plateformes de livraison avec des offres exclusives sur les réseaux."
            ]
        elif any(cat in top_cat for cat in ["coiffure", "beauté", "esthétique"]):
            reco += [
                "Publier des avant/après clients avec autorisation.",
                "Créer des tutos vidéo (coiffures, soins).",
                "Lancer des offres fidélité via des stories ou publications sponsorisées."
            ]
        elif any(cat in top_cat for cat in ["mode", "vêtements"]):
            reco += [
                "Collaborer avec des micro-influenceurs locaux pour des shootings.",
                "Mettre en avant les nouveautés via des lookbooks sur Instagram.",
                "Organiser des live try-on sur Instagram ou TikTok."
            ]
        elif any(cat in top_cat for cat in ["service", "auto"]):
            reco += [
                "Valoriser l'expertise via des témoignages clients.",
                "Partager les coulisses du service ou des réalisations concrètes.",
                "Créer des guides pratiques ou astuces en vidéo courte."
            ]
        elif any(cat in top_cat for cat in ["boutique", "commerce", "épicerie"]):
            reco += [
                "Présenter les produits stars en photo ou vidéo.",
                "Organiser des jeux concours pour booster l'engagement.",
                "Mettre en avant la proximité et les horaires via des stories fréquentes."
            ]
        else:
            reco += [
                "Créer du contenu visuel expliquant l’activité.",
                "Utiliser les outils Meta pour cibler une audience locale.",
                "Analyser les heures d'engagement pour optimiser les publications."
            ]

        if cluster not in recommandations:
            recommandations[cluster] = {}

        recommandations[cluster][city] = {
            "catégorie dominante": top_cat,
            "followers moyens": moy.round(0).to_dict(),
            "recommandations": reco
        }

    return recommandations

# Appel de la fonction
resultats = recommander_par_cluster_ville(df)

# Affichage des résultats
for cluster, villes in resultats.items():
    for city_id, infos in villes.items():
        print(f"\n🔹 Cluster {cluster} | Ville : {city_id}")
        print(f"Catégorie dominante : {infos['catégorie dominante']}")
        print("Followers moyens :", infos['followers moyens'])
        print("Recommandations :")
        for r in infos['recommandations']:
            print(" -", r)

# Générer les recommandationsq
resultats = recommander_par_cluster_ville(df)

# Sauvegarder dans un fichier JSON
with open("recommandations_par_cluster_et_ville.json", "w", encoding="utf-8") as f:
    json.dump(resultats, f, ensure_ascii=False, indent=4)
