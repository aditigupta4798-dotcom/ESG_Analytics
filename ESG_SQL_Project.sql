USE ESG_PROJECT;
SELECT DATABASE();
SELECT*FROM BRSR_DATA;
SELECT COUNT(*) AS Total_Companies
FROM BRSR_DATA;
SELECT DISTINCT Sector
FROM BRSR_DATA;
SELECT Company,
`Renewable Energy %`
FROM BRSR_DATA
ORDER BY `Renewable Energy %` DESC
LIMIT 5;
SELECT Company,
`Renewable Energy %`
FROM BRSR_DATA
ORDER BY `Renewable Energy %` ASC
LIMIT 5;
SELECT Sector,
ROUND(AVG(`Renewable Energy %`),2) AS Avg_Renewable
FROM BRSR_DATA
GROUP BY Sector
ORDER BY Avg_Renewable DESC;
SELECT Company,
`Scope 1 ( tCO2e)`
FROM BRSR_DATA
ORDER BY `Scope 1 ( tCO2e)` DESC
LIMIT 1;
SELECT Company,
`Scope 1 ( tCO2e)`
FROM BRSR_DATA
ORDER BY `Scope 1 ( tCO2e)` ASC
LIMIT 1;
SELECT Sector,
SUM(`Total Employees`) AS Employees
FROM BRSR_DATA
GROUP BY Sector;





SELECT Company,
Sector,
`Renewable Energy %`,
RANK() OVER(ORDER BY `Renewable Energy %` DESC) AS Renewable_Rank
FROM BRSR_DATA;

SELECT * FROM (SELECT Company, Sector, `Renewable Energy %`, Rank() OVER (PARTITION BY Sector ORDER BY `Renewable Energy %` DESC)
AS Rankings FROM BRSR_DATA)AS x WHERE Rankings = 1;

SELECT Company, Sector, `Renewable Energy %` FROM BRSR_DATA WHERE `Renewable Energy %`> (SELECT AVG (`Renewable Energy %`) FROM BRSR_DATA);

SELECT Company, `Renewable Energy %`, CASE 
WHEN `Renewable Energy %`>=0.70 THEN 'Excellent'
WHEN `Renewable Energy %`>=0.40 THEN 'Good'
WHEN `Renewable Energy %`>=0.20 THEN 'Average'
Else 'Poor'
end as Performance from BRSR_DATA;

SELECT Company, `Scope 1 ( tCo2e)`,
CASE
WHEN `Scope 1 ( tCo2e)`<5000 THEN 'Low'
WHEN `Scope 1 ( tCo2e)`<20000 THEN 'Medium'
ELSE 'High'
END AS Emission_Level
FROM BRSR_DATA;

SELECT Sector,
Avg(`Renewable Energy %`) AS Avg_Renewable
FROM BRSR_DATA
GROUP BY Sector
ORDER BY Avg_Renewable Desc;

SELECT Sector,
AVG(`Total Employees`) AS Avg_Employees
FROM BRSR_DATA
GROUP BY Sector;

SELECT Company,Sector,`Renewable Energy %`
FROM BRSR_DATA b
WHERE `Renewable Energy %` >(SELECT AVG(`Renewable Energy %`)
FROM BRSR_DATA
Where Sector = b.Sector);

SELECT Company, `Women Directors %` FROM BRSR_DATA
ORDER BY `Women Directors %` Desc
Limit 5;


SELECT Sector,
COUNT(*) AS Company,
AVG(`Renewable Energy %`) AS Avg_Renewable,
AVG(`Women Directors %`) AS Avg_Women_Directors,
AVG(`Employee Turnover %`) AS Avg_Turnover
FROM BRSR_DATA
GROUP BY Sector;

SELECT
    Company,
    `Renewable Energy %`,
    DENSE_RANK() OVER(ORDER BY `Renewable Energy %` DESC) AS Dense_Ranking
FROM BRSR_DATA;

SELECT Company,
    ROW_NUMBER() OVER(ORDER BY `Renewable Energy %` DESC) AS Row_No
FROM BRSR_DATA;

SELECT Sector,
    ROUND(AVG(`Renewable Energy %`),2) AS Avg_Renewable,
    ROUND(AVG(`Women Directors %`),2) AS Avg_Women_Directors,
    COUNT(*) AS Total_Companies
FROM BRSR_DATA
GROUP BY Sector;

SELECT Company, `ESG Performance Index`
FROM BRSR_DATA
ORDER BY `ESG Performance Index` DESC
LIMIT 5;

SELECT Company, `ESG Performance Index`
FROM BRSR_DATA
ORDER BY `ESG Performance Index` ASC
LIMIT 5;

SELECT Sector,
ROUND(AVG(`ESG Performance Index`),2) AS Average_ESG
FROM BRSR_DATA
GROUP BY Sector
ORDER BY Average_ESG DESC;

SELECT Company,
ROUND(`Environmental Score`,2) AS Environmental_Score
FROM BRSR_DATA
ORDER BY `Environmental Score` DESC
LIMIT 5;

SELECT Company,
ROUND(`Carbon Intensity`,4) AS Carbon_Intensity
FROM BRSR_DATA
ORDER BY `Carbon Intensity`ASC
LIMIT 5;

SELECT Company,
ROUND(`Employee Diversity Index`,2) AS Diversity
FROM brsr_data
ORDER BY `Employee Diversity Index` DESC
LIMIT 5;

SELECT Company,
ROUND(`Employee Stability Index`,2) AS Stability
FROM brsr_data
ORDER BY `Employee Stability Index` DESC
LIMIT 5;

SELECT Company,
ROUND(`Governance Score`,2) AS Governance
FROM brsr_data
ORDER BY `Governance Score` DESC;

SELECT `ESG Category`,
COUNT(*) AS Total_Companies
FROM brsr_data
GROUP BY `ESG Category`;


SELECT Sector, `ESG Category`,
COUNT(*) AS Total_Companies
FROM brsr_data
GROUP BY Sector, `ESG Category`
ORDER BY Sector;



SELECT Sector,
COUNT(*) AS Total_Companies,
ROUND(AVG(`ESG Performance Index`),2) AS Avg_ESG,
ROUND(AVG(`Environmental Score`),2) AS Avg_Environmental,
ROUND(AVG(`Social Score`),2) AS Avg_Social,
ROUND(AVG(`Governance Score`),2) AS Avg_Governance
FROM brsr_data
GROUP BY Sector
ORDER BY Avg_ESG DESC;

SELECT Company, Sector,
ROUND(`ESG Performance Index`,2) AS ESG_Score
FROM brsr_data
WHERE `ESG Performance Index` >( SELECT AVG(`ESG Performance Index`)
FROM brsr_data)
ORDER BY ESG_Score DESC;