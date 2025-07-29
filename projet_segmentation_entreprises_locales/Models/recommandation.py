import pandas as pd

# Charger les données
df = pd.read_csv("entreprises_clusterisées.csv")

# Recommandations par cluster
reco_dict = {
    0: {
        "recommandation_1": "Mettre l'accent sur Facebook (groupes locaux, pubs...)",
        "recommandation_2": "Partager des photos de plats du jour, stories..."
    },
    1: {
        "recommandation_1": "Mettre l'accent sur Facebook (groupes locaux, pubs...)",
        "recommandation_2": "Mettre en avant l’activité avec du contenu vidéo court"
    },
    2: {
        "recommandation_1": "Renforcer les campagnes Instagram (reels, concours...)",
        "recommandation_2": "Mettre en avant l’activité avec du contenu vidéo court"
    },
    3: {
        "recommandation_1": "Mettre l'accent sur Facebook (groupes locaux, pubs...)",
        "recommandation_2": "Mettre en avant l’activité avec du contenu vidéo court"
    }
}

# Ajouter les colonnes recommandation_1 et recommandation_2
df["recommandation_1"] = df["cluster"].map(lambda x: reco_dict.get(x, {}).get("recommandation_1", ""))
df["recommandation_2"] = df["cluster"].map(lambda x: reco_dict.get(x, {}).get("recommandation_2", ""))

# Sauvegarder le fichier enrichi
df.to_csv("entreprises_clusterisées.csv", index=False)
