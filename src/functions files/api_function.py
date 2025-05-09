def film_data(imdb_id):
    """
    Fetches movie data from the OMDB API for a given IMDb ID.

    Args:
        imdb_id (str): The IMDb ID of the movie to fetch data for.

    Returns:
        dict: A dictionary containing the following movie details:
            - filmid (str): The IMDb ID of the movie.
            - title (str): The title of the movie.
            - runtime (str): The runtime of the movie.
            - genre (str): The genre(s) of the movie.
            - director (str): The director(s) of the movie.
            - actors (str): The main actors in the movie.
            - language (str): The language(s) of the movie.
            - country (str): The country/countries of production.
            - imdbRating (float): The IMDb rating of the movie.
            - metascore (str): The Metascore of the movie.
            - imdbVotes (str): The number of votes on IMDb.

    If the API request fails, it prints an error message and returns None.
    """
    url = 'http://www.omdbapi.com/'
    params = {
        'apikey': API_KEY,
        'i': imdb_id
    }
    
    response = requests.get(url, params=params)
    
    print(f"Consulting information for IMDb ID: {imdb_id}")
    
    if response.status_code == 200:
        print(f"Successful response received for IMDb ID: {imdb_id}")
        data = response.json()
        
        imdb_rating = float(data.get('imdbRating')) if data.get('imdbRating') != 'N/A' else None
        title = data.get('Title')  # Movie title
        runtime = data.get('Runtime')  # Movie runtime
        genre = data.get('Genre')  # Genre(s)
        director = data.get('Director')  # Director(s)
        actors = data.get('Actors')  # Main actors
        language = data.get('Language')  # Language(s)
        country = data.get('Country')  # Country/countries of production
        metascore = data.get('Metascore')  # Metascore
        imdb_votes = data.get('imdbVotes')  # Number of IMDb votes

        return {
            'filmid': imdb_id,
            'title': title,
            'runtime': runtime,
            'genre': genre,
            'director': director,
            'actors': actors,
            'language': language,
            'country': country,
            'imdbRating': imdb_rating,
            'metascore': metascore,
            'imdbVotes': imdb_votes
        }
    else:
        print(f"Error fetching data for IMDb ID: {imdb_id}, status code: {response.status_code}")
        return None
    

def films_df_imdb(df, archivo_salida='df_imdb.csv'):
    """
    Fetches movie data from the OMDb API for a list of IMDb IDs, creates a DataFrame, and saves it to a CSV file.

    Args:
        df (pd.DataFrame): DataFrame containing a column 'filmid' with IMDb IDs.
        archivo_salida (str): Path to save the resulting DataFrame as a CSV file.

    Returns:
        pd.DataFrame: DataFrame containing movie details fetched from the OMDb API.
    """
    datos = []
    ids = df['filmid'].unique()
    total = len(ids)

    print(f"📡 Starting query for {total} unique titles from OMDb...")

    for i, imdb_id in enumerate(ids, start=1):
        print(f"🔍 ({i}/{total}) Querying IMDb ID: {imdb_id}")
        datos.append(film_data(imdb_id))
        time.sleep(0.25)  # Pause to avoid API rate limits

    print("✅ Query completed. Generating DataFrame...")
    df_info = pd.DataFrame(datos)
    print(f"💾 Saving results to file: {archivo_salida}")
    df_info.to_csv(archivo_salida, index=False)
    return df_info