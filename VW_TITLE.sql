CREATE OR ALTER   VIEW [dbo].[VW_TITLE] AS 
SELECT CONCAT(CONCAT(title_id, '_'),news_id) as news_title,
author,
link,
SUBSTRING(publish_date,0,CHARINDEX('2020',publish_date)+13) AS publish_date,
title, 
news_channel,
sentiment_value from title