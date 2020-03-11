CREATE OR ALTER   VIEW [dbo].[VW_DESCRIPTION] AS 
SELECT CONCAT(CONCAT(title_id, '_'),news_id) as news_title,
REPLACE(keyword,',','') AS keyword,
keyword_count
FROM description
WHERE KEYWORD NOT IN ('-','')