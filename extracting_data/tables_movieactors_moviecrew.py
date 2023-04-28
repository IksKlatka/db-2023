"""
Collecting data to tables:
- movie_actors
- movie_crew
"""
import pandas as pd
import json
from extracting_data.model import CastEntry, CrewEntry

# pd.set_option('display.max_columns', None)

def get_cast(index: int, cast_field: str):
    dicts = json.loads(cast_field)
    entries = []
    for d in dicts:
        entry = CastEntry(movie_index=index, **d)
        entries.append(entry)

    return entries

def get_crew(index: int, cast_field: str):
    dicts = json.loads(cast_field)
    entries = []
    for d in dicts:
        entry = CrewEntry(movie_index=index, **d)
        entries.append(entry)

    return entries


def create_movie_actors_table(df: pd.DataFrame):

    # list of cast (individually)
    all_cast_entries = []
    for i, movie in enumerate(df['cast']):
        entries = get_cast(i, movie)
        for e in entries:
            all_cast_entries.append(e)

    # renaming columns
    actor_entries = pd.DataFrame(all_cast_entries)
    actor_entries.rename(columns={'order': 'orders', 'id': 'actor_id'},
                         inplace=True)

    # changing order of columns
    actor_entries = actor_entries.set_index(['movie_index'])
    actor_entries = actor_entries[['credit_id', 'actor_id', 'cast_id',
                                   'character', 'gender', 'orders']]

    # adding extra column necessary in the table
    actor_entries['movie_id'] = mdf['id']
    actor_entries.insert(1, 'movie_id', actor_entries.pop('movie_id'))
    # actor_entries.info()

    #reset index (from movie_index) & set it to credit_id
    actor_entries = actor_entries.reset_index(drop=True)
    actor_entries = actor_entries.set_index('credit_id')

    return actor_entries
def create_movie_crew_table(df: pd.DataFrame):

    # list of crew (individually)
    all_crew_entries = []
    for i, movie in enumerate(df['crew']):
        entries = get_crew(i, movie)
        for e in entries:
            all_crew_entries.append(e)

    crew_table = pd.DataFrame(all_crew_entries)

    #enable inserting valid movie_id by setting index = movie_index
    crew_table = crew_table.set_index(['movie_index'])
    crew_table['movie_id'] = cdf['movie_id']

    #placing movie_id column on the right place in DF
    crew_table.insert(2, 'movie_id', crew_table.pop('movie_id'))

    #renaming column and changing their order in DF
    crew_table = crew_table.rename(columns={'id': 'person_id'})
    crew_table = crew_table[['credit_id', 'movie_id', 'person_id',
                             'job', 'department', 'gender']]

    crew_table = crew_table.reset_index(drop= True)
    crew_table = crew_table.set_index('credit_id')

    save_to_file(crew_table, 'table_moviecrew.csv')


def save_to_file(dataframe: pd.DataFrame, filename: str):
    dataframe.to_csv(rf'C:/Users/igakl/Desktop/db-2023/db-2023/datas/{filename}',
                     sep=';')


if __name__ == '__main__':
    credits = pd.read_csv(r'C:/Users/igakl/Desktop/MOVIES/datas/tmdb_5000_credits.csv')
    movies = pd.read_csv(r'C:/Users/igakl/Desktop/MOVIES/datas/tmdb_5000_movies.csv')
    mdf = pd.DataFrame(movies)
    cdf = pd.DataFrame(credits)


