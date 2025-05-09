# Función para obtener recaudación internacional desde Box Office Mojo
def film_world_boxoffice(imdb_id):
    """
    Fetches the worldwide box office revenue for a given IMDb ID from Box Office Mojo.

    Args:
        imdb_id (str): The IMDb ID of the movie to fetch data for.

    Returns:
        str: The worldwide box office revenue as a string (e.g., "$20,000,000").
            Returns None if the revenue is not found or if an error occurs.
    """
    url = f'https://www.boxofficemojo.com/title/{imdb_id}/?ref_=bo_se_r_1'
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error accessing the page for IMDb ID: {imdb_id} - {e}")
        return 'Error accessing the page'

    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"✅ Successfully received response for IMDb ID: {imdb_id}")

    try:
        # Search all performance summary sections
        performance_sections = soup.select('div.mojo-performance-summary-table div.a-section.a-spacing-none')
        for section in performance_sections:
            if 'Worldwide' in section.get_text():
                money_span = section.find('span', class_='money')
                if money_span:
                    return money_span.get_text(strip=True)
        return None
    except Exception as e:
        print(f"❌ Error processing the HTML: {e}")
        return None
    
# Función para extraer IMDb ID, título y recaudación internacional
def worldwide_boxoffice_df(df):
    """
    Extracts worldwide box office revenue for a list of IMDb IDs, creates a DataFrame, and returns it.

    Args:
        df (pd.DataFrame): DataFrame containing a column 'filmid' with IMDb IDs and a column 'film' with movie titles.

    Returns:
        pd.DataFrame: A DataFrame containing the following columns:
            - 'IMDb ID': The IMDb ID of the movie.
            - 'title': The title of the movie.
            - 'Worlwide boxoffice': The worldwide box office revenue as a string (e.g., "$20,000,000").
    """
    datos = []
    ids = df['filmid'].unique()
    total = len(ids)

    for i, imdb_id in enumerate(ids, start=1):
        print(f"🌍 ({i}/{total}) Querying worldwide box office for IMDb ID: {imdb_id}")
        recaudacion = film_world_boxoffice(imdb_id)
        time.sleep(0.25)
        
        # Get the corresponding title from the original DataFrame
        titulo = df[df['filmid'] == imdb_id]['film'].values[0]

        # Save the data in the list
        datos.append({
            'IMDb ID': imdb_id,
            'title': titulo,
            'Worlwide boxoffice': recaudacion
        })

    # Create a DataFrame with the results
    df_worldwide = pd.DataFrame(datos)
    return df_worldwide

# Función para obtener recaudación domestic desde Box Office Mojo
def film_domestic_boxoffice(imdb_id):
    """
    Fetches the domestic box office revenue for a given IMDb ID from Box Office Mojo.

    Args:
        imdb_id (str): The IMDb ID of the movie to fetch data for.

    Returns:
        str: The domestic box office revenue as a string (e.g., "$20,000,000").
             Returns None if the revenue is not found or if an error occurs.
    """
    url = f'https://www.boxofficemojo.com/title/{imdb_id}/?ref_=bo_se_r_1'
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error accessing the page for IMDb ID: {imdb_id} - {e}")
        return 'Error accessing the page'

    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"✅ Successfully received response for IMDb ID: {imdb_id}")

    try:
        # Search all performance summary sections
        performance_sections = soup.select('div.mojo-performance-summary-table div.a-section.a-spacing-none')
        for section in performance_sections:
            if 'Domestic' in section.get_text():
                money_span = section.find('span', class_='money')
                if money_span:
                    return money_span.get_text(strip=True)
        return None
    except Exception as e:
        print(f"❌ Error processing the HTML: {e}")
        return None

# Función para extraer IMDb ID, título y recaudación domestic
def films_domestic_boxoffice_df(df):
    """
    Extracts domestic box office revenue for a list of IMDb IDs, creates a DataFrame, and returns it.

    Args:
        df (pd.DataFrame): DataFrame containing a column 'filmid' with IMDb IDs and a column 'film' with movie titles.

    Returns:
        pd.DataFrame: A DataFrame containing the following columns:
            - 'IMDb ID': The IMDb ID of the movie.
            - 'title': The title of the movie.
            - 'domestic boxoffice': The domestic box office revenue as a string (e.g., "$20,000,000").
    """
    datos = []
    ids = df['filmid'].unique()
    total = len(ids)

    for i, imdb_id in enumerate(ids, start=1):
        print(f"🌍 ({i}/{total}) Querying domestic box office for IMDb ID: {imdb_id}")
        recaudacion = film_domestic_boxoffice(imdb_id)
        time.sleep(0.25)
        
        # Get the corresponding title from the original DataFrame
        titulo = df[df['filmid'] == imdb_id]['film'].values[0]

        # Save the data in the list
        datos.append({
            'IMDb ID': imdb_id,
            'title': titulo,
            'domestic boxoffice': recaudacion
        })

    # Create a DataFrame with the results
    df_domestic_boxoffice = pd.DataFrame(datos)
    return 

# Function to obtain international box office revenue from Box Office Mojo
def film_internacional_boxoffice(imdb_id):
    """
    Fetches the international box office revenue for a given IMDb ID from Box Office Mojo.

    Args:
        imdb_id (str): The IMDb ID of the movie to fetch data for.

    Returns:
        str: The international box office revenue as a string (e.g., "$20,000,000").
            Returns None if the revenue is not found or if an error occurs.
    """
    url = f'https://www.boxofficemojo.com/title/{imdb_id}/?ref_=bo_se_r_1'
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        for section in performance_sections:
            if 'International' in section.get_text():
                money_span = section.find('span', class_='money')
                if money_span:
                    return money_span.get_text(strip=True)
        return None
    except Exception as e:
        print(f"❌ Error procesando el HTML: {e}")
        return None
    
# Función para extraer IMDb ID, título y recaudación international
def films_international_boxoffice_df(df):
    """
    Extracts international box office revenue for a list of IMDb IDs, creates a DataFrame, and returns it.

    Args:
        df (pd.DataFrame): DataFrame containing a column 'filmid' with IMDb IDs and a column 'film' with movie titles.

    Returns:
        pd.DataFrame: A DataFrame containing the following columns:
            - 'IMDb ID': The IMDb ID of the movie.
            - 'title': The title of the movie.
            - 'international boxoffice': The international box office revenue as a string (e.g., "$20,000,000").
    """
    datos = []
    ids = df['filmid'].unique()
    total = len(ids)

    for i, imdb_id in enumerate(ids, start=1):
        print(f"🌍 ({i}/{total}) Querying international box office for IMDb ID: {imdb_id}")
        recaudacion = film_internacional_boxoffice(imdb_id)
        time.sleep(0.25)
        
        # Get the corresponding title from the original DataFrame
        titulo = df[df['filmid'] == imdb_id]['film'].values[0]

        # Save the data in the list
        datos.append({
            'IMDb ID': imdb_id,
            'title': titulo,
            'international boxoffice': recaudacion
        })

    # Create a DataFrame with the results
    df_international_boxoffice = pd.DataFrame(datos)
    return df_international_boxoffice

def film_url_fixed(film_name):
    """
    Converts a film name into a URL-friendly format by applying the following transformations:
    - Removes leading articles ("The ", "A ") and appends them at the end (e.g., "The Matrix" -> "Matrix, The").
    - Replaces special characters such as "&" with "and".
    - Replaces spaces, colons, commas, question marks, slashes, and parentheses with hyphens ("-").
    - Removes periods, apostrophes, and exclamation marks.

    Args:
        film_name (str): The original name of the film.

    Returns:
        str: The transformed, URL-friendly film name.
    """
    film_name = film_name.strip()

    if film_name.startswith("The "):
        film_name = film_name[4:] + ", The"
    elif film_name.startswith("A "):
        film_name = film_name[2:] + ", A"

    film_name = film_name.replace("&", "and")
    for char in [" ", ":", ",",  "?","/", "(", ")"]:
        film_name = film_name.replace(char, "-")
    for char1 in [".", "'", "!",]:
        film_name = film_name.replace(char1, "")
    return film_name

def film_budget(film_name):
    """
    Fetches the production budget of a film from The Numbers website.

    Args:
        film_name (str): The name of the film.

    Returns:
        int: The production budget of the film in dollars, or None if not found or an error occurs.
    """
    film_url = film_url_fixed(film_name)
    url = f'https://www.the-numbers.com/movie/{film_url}#tab=summary'

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        b_tags = soup.find_all('b', string='Production Budget:')
        for b in b_tags:
            td_parent = b.find_parent('td')
            if td_parent:
                td_siguiente = td_parent.find_next_sibling('td')
                if td_siguiente:
                    texto_completo = td_siguiente.text.strip()
                    texto_dinero = texto_completo.split(' (')[0]  # "$2,000,000"
                    # Clean and convert to int
                    presupuesto = int(texto_dinero.replace('$', '').replace(',', ''))
                    print(f"   ✅ Budget found: {presupuesto}")
                    return presupuesto
        print("   ⚠️ Budget not found")
        return None
    else:
        print("   ❌ Error accessing the page")
        return None
    
def films_budget_df(df):
    """
    Creates a DataFrame containing the budget information for a list of films.

    Args:
        df (pd.DataFrame): DataFrame containing a column 'filmid' with IMDb IDs and a column 'title' with movie titles.

    Returns:
        pd.DataFrame: A DataFrame containing the following columns:
            - 'IMDb ID': The IMDb ID of the movie.
            - 'title': The title of the movie.
            - 'budget': The production budget of the movie.
    """
    datos = []
    ids = df['filmid'].unique()
    total = len(ids)

    for i, imdb_id in enumerate(ids, start=1):
        print(f"🎬 ({i}/{total}) Consulting budget for IMDb ID: {imdb_id}")
        
        # Get the corresponding title from the original DataFrame
        titulo = df[df['filmid'] == imdb_id]['title'].values[0]

        # Get the budget
        presupuesto = film_budget(titulo)
        time.sleep(0.25)

        # Save the data in the list
        datos.append({
            'IMDb ID': imdb_id,
            'title': titulo,
            'budget': presupuesto
        })

    # Create a DataFrame with the results
    df_budget = pd.DataFrame(datos)
    return df_budget