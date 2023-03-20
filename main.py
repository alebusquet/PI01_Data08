from fastapi import FastAPI , Path, UploadFile, File
from typing import Optional, Union
from pydantic import BaseModel
import shutil
import uvicorn
import pandas as pd
import numpy as np


app = FastAPI(Title="Consultas a Plataformas", 
              description="API para Amazon, Disney, Hulu y Netflix",
              version="1.0.1")


# Cargo los dataframes necesarios.
df_actors = pd.read_csv("actors.csv")
df_unico = pd.read_csv("unico.csv")
df_completo = pd.read_csv("completo.csv")


# Funcion 1
@app.get("/Maxima Duracion Pelicula/")
#async def get_max_duration(year:int, platform:str, duration_type:str):
async def get_max_duration(year: Union[int, None] = 0, platform: Union[str, None] = None, duration_type: Union[str, None] = None):
    
    if (year != 0) & (platform != None) & (duration_type != None):
        data = df_unico[(df_unico["release_year"] == year) & (df_unico["platform"] == platform) & (df_unico["duration_type"] == duration_type)]["duration_int"].max()
    elif (year != 0) & (platform == None) & (duration_type == None):
        data = df_unico[(df_unico["release_year"] == 2020)]["duration_int"].max()
    elif (year != 0) & (platform != None) & (duration_type == None):
        data = df_unico[(df_unico["release_year"] == year) & (df_unico["platform"] == platform)]["duration_int"].max()
    elif (year != 0) & (platform == None) & (duration_type != None):
        data = df_unico[(df_unico["release_year"] == year) & (df_unico["duration_type"] == duration_type)]["duration_int"].max()
    elif (year == 0) & (platform != None) & (duration_type != None):
        data = df_unico[(df_unico["platform"] == platform) & (df_unico["duration_type"] == duration_type)]["duration_int"].max()
    elif (year == 0) & (platform == None) & (duration_type != None):
        data = df_unico[(df_unico["duration_type"] == duration_type)]["duration_int"].max()
    elif (year == 0) & (platform != None) & (duration_type == None):
        data = df_unico[(df_unico["platform"] == platform)]["duration_int"].max()
    else:
        data = df_unico["duration_int"].max()
    if platform == None:
        platform = "Sin especificar"
    if duration_type == None:
        duration_type = "Sin especificar"

    message = f"Máximo para plataforma: {platform}, para el año: {year} en tipo de duracion: {duration_type} es"
    return {message:int(data)}


# Funcion 2.
@app.get('/Peliculas por Puntajes/')
async def get_score_count(platform:str, scored:float, year:int):

    df_filtrado = df_completo.loc[(df_completo['platform'] == platform) & (df_completo['release_year'] == year)]
    df_filtrado = df_filtrado.loc[df_filtrado['rating_prom'] > scored]
    cantidad_pelis = len(df_filtrado)
    
    message = f"Cantidad de películas en {platform}, con un puntaje mayor a {scored}, para el año {year} es"
    return {message: cantidad_pelis}


# Funcion 3
@app.get('/Peliculas y Series por Plataforma/')
async def get_count_plataform(platform:str):

    message = f"Cantidad de películas en {platform} es"
    return {message:df_unico[(df_unico["platform"] == platform) & (df_unico["type"] == "movie")]["type"].count().tolist(),
    f"Cantidad de series en {platform} es":df_unico[(df_unico["platform"] == platform) & (df_unico["type"] == "tv show")]["type"].count().tolist()}


# Funcion 4
@app.get('/Actor mas Repetido/')
async def get_actor(plataforma:str, año:int):

    data = df_actors[(df_actors["año"] == año) & (df_actors["plataforma"] == plataforma)]["actor"]
    message = f"Actor que mas se repite en {plataforma} en el año {año}"
    return {message:data.value_counts().index[0]}