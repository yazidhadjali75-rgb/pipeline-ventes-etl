# 📊 Analyse des ventes — Pipeline ETL & Data Analytics

## Présentation

Ce projet consiste à développer un pipeline ETL permettant de collecter, nettoyer, transformer et analyser des données commerciales.

L'objectif est de transformer des données brutes en informations exploitables grâce à Python, SQL et aux outils Google, puis de créer un tableau de bord interactif.

## Technologies utilisées

- **Python & Pandas** : nettoyage et transformation des données.
- **Google BigQuery** : stockage des données dans le cloud.
- **SQL** : analyse et agrégation des ventes.
- **Google Sheets** : conservation des données nettoyées.
- **Looker Studio** : création du tableau de bord interactif.
- **Git & GitHub** : gestion et partage du projet.

## Pipeline ETL

1. **Extract** : importation des données depuis un fichier CSV.
2. **Transform** : suppression des doublons, nettoyage des produits, uniformisation des villes, traitement des valeurs manquantes et calcul du chiffre d'affaires.
3. **Load** : chargement des données nettoyées dans Google BigQuery.

Les données sont ensuite analysées avec SQL, conservées dans Google Sheets et visualisées avec Looker Studio.

## Analyses réalisées

- Chiffre d'affaires total.
- Nombre de ventes et quantités vendues.
- Performance des ventes par ville.
- Analyse du chiffre d'affaires par produit.

## Résultats

| Indicateur | Résultat |
|---|---:|
| Nombre de ventes | 9 |
| Quantité totale vendue | 24 |
| Chiffre d'affaires total | 3 465 |

**Meilleur produit en chiffre d'affaires :** Ordinateur (2 250).

**Ville avec le chiffre d'affaires le plus élevé :** Paris (2 130).

## Dashboard

Tableau de bord interactif réalisé avec Looker Studio.

- **Dashboard :** À compléter
- **Google Sheets :** À compléter

## Installation et exécution

Installer les dépendances :

```bash
pip install pandas google-cloud-bigquery
```

Configurer l'authentification Google Cloud :

```bash
gcloud auth application-default login
```

Exécuter le pipeline :

```bash
python pipeline-ventes-etl.py
```

## Compétences développées

Python, Pandas, ETL, SQL, Google BigQuery, Google Sheets, Looker Studio, Data Cleaning, Data Analytics et GitHub.

## Auteur

Projet personnel réalisé dans le cadre de mon apprentissage du Data Engineering et de l'analyse de données.