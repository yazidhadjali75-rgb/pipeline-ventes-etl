# 📊 Analyse des ventes — Projet Data Engineering

## Présentation

Développement d'un pipeline ETL permettant de nettoyer, transformer et analyser des données commerciales.

L'objectif est de transformer des données brutes en informations exploitables et de créer un dashboard interactif.

## Technologies utilisées

- **Python & Pandas** : nettoyage et transformation des données.
- **SQL & Google BigQuery** : stockage et analyse des ventes.
- **Google Sheets** : conservation des données nettoyées.
- **Looker Studio** : visualisation des résultats.
- **Git & GitHub** : gestion du projet.

## Pipeline ETL

1. Extraction des données depuis un fichier CSV.
2. Nettoyage et transformation avec Python et Pandas.
3. Suppression des doublons et traitement des valeurs manquantes.
4. Calcul du chiffre d'affaires.
5. Chargement des données dans BigQuery.
6. Analyse SQL et création d'un dashboard.

## Résultats

| Indicateur               | Résultat |
| ------------------------ | -------: |
| Nombre de ventes         |        9 |
| Quantité vendue          |       24 |
| Chiffre d'affaires total |    3 465 |

- Ville la plus performante : Paris.
- Produit avec le chiffre d'affaires le plus élevé : Ordinateur.

## Dashboard et données

- **Dashboard Looker Studio :** [https://datastudio.google.com/reporting/b8082a49-dade-4e74-8bb1-5e8cd9e59f36](https://datastudio.google.com/reporting/b8082a49-dade-4e74-8bb1-5e8cd9e59f36)
- **Google Sheets :**[https://docs.google.com/spreadsheets/d/1qQ6CcTyout0fI5x84Q06CiWcyEDm2abytYig_AM0Dqs/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1qQ6CcTyout0fI5x84Q06CiWcyEDm2abytYig_AM0Dqs/edit?usp=sharing)

## Installation

```bash
pip install pandas google-cloud-bigquery
```

Authentification Google Cloud :

```bash
gcloud auth application-default login
```

Exécution :

```bash
python pipeline-ventes-etl.py
```

## Compétences développées

ETL · Python · Pandas · SQL · BigQuery · Data Cleaning · Data Analytics · Looker Studio · GitHub

## Auteur

Projet personnel réalisé dans le cadre de mon apprentissage du Data Engineering et de l'analyse de données.
