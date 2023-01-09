# Etl de Twitter con airflow


## 1️⃣ ETL
_Nos conectamos a Twitter a través de la API https://developer.twitter.com/en/docs/twitter-api con el fin de extraer información de los tweets más populares de un termino que puede ser relevante en la industria: "energíaRenovable", se cumplen los pasos del ETL, "extrayendo" algunos campos, en cuanto a la "transformación" se pasa de json a lista y se da formato a la fecha, posteriormente se "carga" o exporta el dataframe a un archivo csv._

💻 [Archivo .py - etl_twitter.py](https://github.com/pipeduke/etl_Twitter/blob/main/Etl_twitter.py)

💻 [Archivo .py - twitter_dag.py](https://github.com/pipeduke/etl_Twitter/blob/main/twitter_dag.py)

_Se usó Python en VsCode para crear el código y los DAG, también airflow para ejecutarlos, adjunto algunos pantallazos como evidencia_

🖼️ [Airflow ETL_Completo](https://github.com/pipeduke/etl_Twitter/blob/main/Captura%20de%20pantalla_20230109_015602.png) 

🖼️ [Airflow Log](https://github.com/pipeduke/etl_Twitter/blob/main/Captura%20de%20pantalla_20230109_015723.png)

🗒️ [dataframe .csv](https://github.com/pipeduke/etl_Twitter/blob/main/dataTweets.csv)

## 2️⃣ Dashboard 
_Como herramienta de visualización elegí PowerBI, se crearon tres gráficas utilizando los datos generados en el punto anterior_

📊 [Gráficos en .pdf](https://github.com/pipeduke/etl_Twitter/blob/main/Tablero%20Visualizaci%C3%B3n%20Tweets.pdf)

📊 [Pantallazo PowerBI](https://github.com/pipeduke/etl_Twitter/blob/main/Captura%20de%20pantalla_20230109_012609.png)

📊 [Archivo original PowerBI](https://github.com/pipeduke/etl_Twitter/blob/main/Tablero%20Visualizaci%C3%B3n%20Tweets.pbix)

*_______________________________*
* **✒️ Presentado por:** 

**Felipe Duque**

📧 [felipeduque9@gmail.com](mailto:felipeduque9@gmail.com)

📲 [310 3846185](tel://+573103846185)
