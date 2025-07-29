# app.py

from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import FileResponse
from fastapi.encoders import jsonable_encoder
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import pandas as pd



app = FastAPI()

# ======== CHARGEMENT DES DONNÉES ========
df = pd.read_csv("entreprises_clusterisées.csv")
df = df.fillna("Inconnu")

# ======== ROUTES DE BASE ========

@app.get("/")
def welcome():
    return {"message": "Bienvenue sur l'API de segmentation des entreprises !"}

@app.get("/data")
def get_data():
    try:
        return jsonable_encoder(df.to_dict(orient="records"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur interne : {str(e)}")

# ======== FILTRAGE & RECHERCHE ========

@app.get("/entreprises")
def get_all_entreprises():
    return df.to_dict(orient="records")

@app.get("/cluster/{cluster_id}")
def get_by_cluster(cluster_id: int):
    result = df[df['cluster'] == cluster_id]
    return result.to_dict(orient="records")

@app.get("/clusters")
def get_cluster_counts():
    counts = df['cluster'].value_counts().to_dict()
    return {"répartition_par_cluster": counts}

@app.get("/secteur")
def get_by_secteur(secteur: str = Query(...)):
    if 'category_name' not in df.columns:
        raise HTTPException(status_code=400, detail="Colonne 'category_name' non trouvée.")
    
    result = df[df['category_name'].str.lower() == secteur.lower()]
    if result.empty:
        raise HTTPException(status_code=404, detail=f"Aucune entreprise trouvée pour le secteur : {secteur}")
    
    return result.to_dict(orient="records")

@app.get("/filtre")
def filtre_secteur_cluster(secteur: str = Query(...), cluster: int = Query(...)):
    if 'category_name' not in df.columns:
        raise HTTPException(status_code=400, detail="Colonne 'category_name' non trouvée.")
    
    result = df[
        (df['category_name'].str.lower() == secteur.lower()) &
        (df['cluster'] == cluster)
    ]
    return result.to_dict(orient="records")

@app.get("/export")
def export_by_secteur(secteur: str = Query(...)):
    result = df[df['category_name'].str.lower() == secteur.lower()]
    if result.empty:
        raise HTTPException(status_code=404, detail=f"Aucune donnée pour le secteur '{secteur}'")
    
    export_path = f"export_{secteur.lower()}.csv"
    result.to_csv(export_path, index=False)
    return FileResponse(export_path, media_type="text/csv", filename=export_path)

# ======== GRAPHIQUES ========

def save_plot(fig, path):
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)

@app.get("/graph/cluster")
def show_cluster_plot():
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x="cluster", data=df, palette="pastel", ax=ax)
    ax.set(title="Répartition par cluster", xlabel="Cluster", ylabel="Nombre d’entreprises")
    path = "graph_cluster.png"
    save_plot(fig, path)
    return FileResponse(path, media_type="image/png")

@app.get("/graph/secteur")
def show_secteur_plot():
    if 'category_name' not in df.columns:
        raise HTTPException(status_code=400, detail="Colonne 'category_name' non trouvée.")
    
    sns.set(style="whitegrid")

    # Optionnel : top 30 secteurs les plus fréquents
    top_categories = df['category_name'].value_counts().head(30).index

    # Taille dynamique selon le nombre de catégories affichées
    fig, ax = plt.subplots(figsize=(12, len(top_categories) * 0.4))

    sns.countplot(
        y="category_name",
        data=df[df['category_name'].isin(top_categories)],
        palette="Set2",
        order=top_categories,
        ax=ax
    )

    ax.set(
        title="Répartition des entreprises par secteur",
        xlabel="Nombre d’entreprises",
        ylabel="Secteur"
    )
    ax.tick_params(axis='y', labelsize=9)
    fig.tight_layout()

    path = "graph_secteur.png"
    save_plot(fig, path)
    return FileResponse(path, media_type="image/png")


@app.get("/graph/ville")
def show_ville_plot():
    if 'city_name' not in df.columns:
        raise HTTPException(status_code=400, detail="Colonne 'city_name' non trouvée.")
    
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(y="city_name", data=df, palette="cool", order=df['city_name'].value_counts().index, ax=ax)
    ax.set(title="Répartition par ville", xlabel="Nombre d’entreprises", ylabel="Ville")
    path = "graph_ville.png"
    save_plot(fig, path)
    return FileResponse(path, media_type="image/png")




@app.get("/recommandation/cluster/{cluster_id}")
def get_reco_by_cluster(cluster_id: int):
    result = df[df['cluster'] == cluster_id]
    if result.empty:
        raise HTTPException(status_code=404, detail="Cluster non trouvé.")

    # Combine les deux colonnes de recommandations
    recommandations = pd.concat([result['recommandation_1'], result['recommandation_2']])
    counts = recommandations.value_counts().to_dict()

    return {"cluster": cluster_id, "recommandations": counts}

@app.get("/recommandations/export")
def export_recommandations():
    reco_data = df[['company_id', 'company_name', 'cluster', 'recommandation_1', 'recommandation_2']]
    reco_data.to_json("recommandations.json", orient="records", force_ascii=False)
    return FileResponse("recommandations.json", media_type="application/json", filename="recommandations.json")
