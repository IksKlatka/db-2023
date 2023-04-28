"""
Collecting data to tables:
- movies
- actors
- crew
"""

import pandas as pd
import json
from functions import get_crew_of_movie
from extracting_data.model import CastEntry

def get_cast(index: int, cast_field: str):
    dicts = json.loads(cast_field)
    entries = []
    for d in dicts:
        entry = CastEntry(movie_index=index, **d)
        entries.append(entry)

    return entries

def create_table_actors(df: pd.DataFrame):

    #extracting data from object 'cast'
    entries = []
    for i, movie in enumerate(df['cast']):
        entry = get_cast(i, movie)
        for e in entry:
            entries.append(e)

    #creating DF from extracted data
    actors = pd.DataFrame(entries)
    #extracting id and name of an actor from DF above
    actors_table = actors[['id', 'name']]
    actors_table = actors_table.set_index('id')

    save_to_file(actors_table, 'table_actors.csv')

def create_table_movies(df: pd.DataFrame):

    # creating new DF containing movies id and title
    movies_table = df[['movie_id', 'title']]
    movies_table = movies_table.rename(columns={'movie_id':'id'})
    movies_table = movies_table.set_index('id')
    save_to_file(movies_table, 'table_movies.csv')

def create_table_crew(df: pd.DataFrame):
    # TABLE CREW
    # list of crew (individually)
    all_crew_entries = []
    for i, movie in enumerate(df['crew']):
        entry = get_crew_of_movie(i, movie)
        for e in entry:
            all_crew_entries.append(e)

    crew = pd.DataFrame(all_crew_entries)
    crew_table = crew[['id', 'name']]
    crew_table = crew_table.drop_duplicates('id')
    crew_table = crew_table.set_index('id')

    save_to_file(crew_table, 'table_crew.csv')

def save_to_file(df: pd.DataFrame, filename: str):
    df.to_csv(rf'C:/Users/igakl/Desktop/db-2023/db-2023/datas/{filename}',
                     sep=';')


if __name__ == "__main__":

    # importing csv files
    c = pd.read_csv(r'C:/Users/igakl/Desktop/MOVIES/datas/tmdb_5000_credits.csv')
    m = pd.read_csv(r'C:/Users/igakl/Desktop/MOVIES/datas/tmdb_5000_movies.csv')
    # creating DataFrames from csv files
    mdf, cdf = pd.DataFrame(m), pd.DataFrame(c)
    # Checking if all movie ids match in both DFs
    # all(cdf['movie_id'] == mdf['id']) -> True


