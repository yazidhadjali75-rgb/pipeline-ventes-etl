
import pandas as pd
from google.cloud import bigquery


# ==========================================
# 1. CHARGER LES DONNÉES
# ==========================================

df = pd.read_csv("data/ventes_brutes.csv")


# ==========================================
# 2. CRÉER UNE COPIE DES DONNÉES
# ==========================================

df_clean = df.copy()


# ==========================================
# 3. SUPPRIMER LES DOUBLONS
# ==========================================

df_clean = df_clean.drop_duplicates()


# ==========================================
# 4. NETTOYER LES NOMS DES PRODUITS
# ==========================================

df_clean["produit"] = df_clean["produit"].str.strip()


# ==========================================
# 5. UNIFORMISER LES NOMS DES VILLES
# ==========================================

df_clean["ville"] = df_clean["ville"].str.strip().str.title()


# ==========================================
# 6. REMPLACER LES VILLES MANQUANTES
# ==========================================

df_clean["ville"] = df_clean["ville"].fillna("Inconnue")


# ==========================================
# 7. CALCULER LE CHIFFRE D'AFFAIRES
# ==========================================

df_clean["chiffre_affaires"] = (
    df_clean["quantite"] * df_clean["prix_unitaire"]
)


# ==========================================
# 8. AFFICHER LES DONNÉES NETTOYÉES
# ==========================================

print("Données après nettoyage :")
print(df_clean)

print("\nDimensions finales :", df_clean.shape)

print("\nValeurs manquantes :")
print(df_clean.isnull().sum())


# ==========================================
# 9. ENREGISTRER LE FICHIER NETTOYÉ
# ==========================================

df_clean.to_csv("data/ventes_nettoyees.csv", index=False)

print("\nFichier nettoyé enregistré avec succès !")


# ==========================================
# 10. SE CONNECTER À BIGQUERY
# ==========================================

client = bigquery.Client(
    project="mon-projet-bigquery-511118"
)

print("\nConnexion à BigQuery réussie !")


# ==========================================
# 11. AFFICHER LES DATASETS
# ==========================================

datasets = list(client.list_datasets())

for dataset in datasets:
    print("Dataset :", dataset.dataset_id)


# ==========================================
# 12. PRÉPARER L'ENVOI VERS BIGQUERY
# ==========================================

table_id = "mon-projet-bigquery-511118.ventes_etl.ventes"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=True,
    write_disposition="WRITE_TRUNCATE"
)


# ==========================================
# 13. ENVOYER LES DONNÉES VERS BIGQUERY
# ==========================================

with open("data/ventes_nettoyees.csv", "rb") as fichier:

    job = client.load_table_from_file(
        fichier,
        table_id,
        job_config=job_config
    )


# ==========================================
# 14. ATTENDRE LA FIN DU CHARGEMENT
# ==========================================

job.result()

print("\nDonnées envoyées avec succès dans BigQuery !")


# ==========================================
# 15. VÉRIFIER LE NOMBRE DE LIGNES ET COLONNES
# ==========================================

table = client.get_table(table_id)

print("Nombre de lignes :", table.num_rows)
print("Nombre de colonnes :", len(table.schema))
