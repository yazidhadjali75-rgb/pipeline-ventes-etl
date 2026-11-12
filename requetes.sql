-- 1. Analyse globale des ventes
SELECT
    SUM(chiffre_affaires) AS chiffre_affaires_total,
    COUNT(*) AS nombre_ventes,
    SUM(quantite) AS quantite_totale
FROM `mon-projet-bigquery-511118.ventes_etl.ventes`;


-- 2. Chiffre d'affaires par ville
SELECT
    ville,
    SUM(chiffre_affaires) AS chiffre_affaires
FROM `mon-projet-bigquery-511118.ventes_etl.ventes`
GROUP BY ville
ORDER BY chiffre_affaires DESC;


-- 3. Analyse des ventes par produit
SELECT
    produit,
    SUM(quantite) AS quantite_vendue,
    SUM(chiffre_affaires) AS chiffre_affaires
FROM `mon-projet-bigquery-511118.ventes_etl.ventes`
GROUP BY produit
ORDER BY chiffre_affaires DESC;