def cleaning_kaggle_info(df):
    """
    Cleans and transforms the Kaggle DataFrame.

    Args:
        df (pd.DataFrame): Original Kaggle DataFrame.

    Returns:
        pd.DataFrame: Cleaned and transformed DataFrame.
    """
    # Convert column names to lowercase
    df.columns = df.columns.str.lower()
    
    # Convert all in lowercase
    df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
    
    # Drop unnecessary columns
    df.drop(columns=[ 
        'class', 
        'ceremony', 
        'nomid', 
        'name', 
        'nominees', 
        'nomineeids', 
        'detail', 
        'note', 
        'citation', 
        'multifilmnomination'
    ], inplace=True)
    
    # Filter out invalid years
    df = df[~df['year'].str.contains(r'/', regex=True)]
    df['year'] = df['year'].astype(int)
    
    # Filter the last 10 years
    df = df[df['year'] >= 2000]
    
    # Filter specific film categories
    film_categories = [
        'best picture',
        'animated feature film',
        'international feature film'
    ]
    df = df[df['canonicalcategory'].isin(film_categories)]
    
    # Convert 'winner' to 0 (no) and 1 (yes)
    df['winner'] = df['winner'].fillna(0).astype(int)
    
    # Convert 0 to 'no' and 1 to 'yes' in the 'winner' column
    df['winner'] = df['winner'].replace({0: 'no', 1: 'yes'})
    
    return df



def create_boxoffice_dataset(df_domestic_boxoffice, df_international_boxoffice, df_worldwide):
    """
        Creates a combined DataFrame of box office revenues from three sources:
        domestic, international, and worldwide.

        Args:
            df_domestic_boxoffice (pd.DataFrame): Domestic box office revenue data.
            df_international_boxoffice (pd.DataFrame): International box office revenue data.
            df_worldwide (pd.DataFrame): Worldwide box office revenue data.

        Returns:
            pd.DataFrame: Combined and cleaned DataFrame.
        """
    # Eliminar columna 'title' si existe
    for df in [df_international_boxoffice, df_worldwide]:
        if 'title' in df.columns:
            df.drop(columns='title', inplace=True)

    # Establecer 'IMDb ID' como índice
    df_domestic_boxoffice.set_index('IMDb ID', inplace=True)
    df_international_boxoffice.set_index('IMDb ID', inplace=True)
    df_worldwide.set_index('IMDb ID', inplace=True)

    # Unir los tres DataFrames
    df_boxoffice = df_domestic_boxoffice.join(
        [df_international_boxoffice, df_worldwide], how='outer'
    ).reset_index()

    # Limpiar y convertir columnas monetarias
    columnas_recaudacion = [
        'domestic boxoffice', 'international boxoffice', 'Worlwide boxoffice'
    ]
    
    for col in columnas_recaudacion:
        df_boxoffice[col] = (
            df_boxoffice[col]
            .replace(r'[\$,]', '', regex=True)
            .replace('', np.nan)
            .fillna(0)
            .astype(int)
        )

    # Renombrar columna 'IMDb ID' a 'filmid'
    df_boxoffice.rename(columns={'IMDb ID': 'filmid'}, inplace=True)

    return df_boxoffice




def clean_budget(df_budget, presupuestos, ruta_salida='movie_budgets_clean.csv'):
    """
        Replaces budget values in the DataFrame based on the `presupuestos` dictionary,
        fills missing values with 0, renames 'IMDb ID' to 'filmid', and saves the result to a CSV.

        Args:
            df_budget (pd.DataFrame): DataFrame with columns 'title' and 'budget'.
            presupuestos (dict): Dictionary with budgets by title.
            ruta_salida (str): Path to the output CSV file.
        """
    df_budget=pd.read_csv('csv/raw/movie_budgets.csv')
    # Reemplazar presupuestos donde haya valores en el diccionario
    df_budget['budget'] = df_budget['title'].map(presupuestos).fillna(df_budget['budget'])
    df_budget['budget'] = df_budget['budget'].fillna(0)
    df_budget['title'] = df_budget['title'].str.lower()

    # Renombrar columna IMDb ID si existe
    if 'IMDb ID' in df_budget.columns:
        df_budget.rename(columns={'IMDb ID': 'filmid'}, inplace=True)

    # Guardar el archivo actualizado
    df_budget.to_csv(ruta_salida, index=False)
    print(f"✅ Archivo guardado como: {ruta_salida}")





def create_financial_data(df_budget, df_boxoffice, ruta_salida='financial_data.csv'):
    """
    Creates a financial dataset containing the revenue and budget of the movies,
    calculates the ROI, and saves the result to a CSV file.

    Args:
        df_budget (pd.DataFrame): DataFrame with information about the movie budgets.
        df_boxoffice (pd.DataFrame): DataFrame with the revenue of the movies.
        ruta_salida (str): Path to the output CSV file.
    """
    df_budget=pd.read_csv('csv/movie_budgets_clean.csv')
    # Eliminar la columna 'title' si existe
    for df in [df_budget]:
        if 'title' in df.columns:
            df.drop(columns='title', inplace=True)

    # Establecer 'IMDb ID' como índice
    df_budget.set_index('filmid', inplace=True)
    df_boxoffice.set_index('filmid', inplace=True)

    # Unir los DataFrames de presupuesto y recaudación por 'IMDb ID'
    df_financial_info = df_boxoffice.join(
        df_budget,
        how='inner'
    ).reset_index()

    # Calcular el ROI
    df_financial_info['ROI'] = (
        (df_financial_info['Worlwide boxoffice'] - df_financial_info['budget']) / df_financial_info['budget']
    ).round(2)

    # Guardar el archivo actualizado
    df_financial_info.to_csv(ruta_salida, index=False)
    print(f"✅ Archivo guardado como: {ruta_salida}")




def create_final_dataset(df_imdb, df_financial_data, df_kaggle, ruta_salida='final_dataset.csv'):
    """
    Creates the final dataset by merging IMDb, revenue, and awards data, 
    cleaning unnecessary columns, and saving the resulting CSV file.

    Args:
        df_imdb (pd.DataFrame): DataFrame with IMDb information.
        df_financial_data (pd.DataFrame): DataFrame with financial information (revenue, budget, ROI).
        df_kaggle (pd.DataFrame): DataFrame with awards and category information.
        ruta_salida (str): Path to the output CSV file.
    """
    # Eliminar columnas si existen en df_financial_data
    columnas_a_eliminar = {'title', 'domestic boxoffice', 'international boxoffice'}
    if columnas_a_eliminar.issubset(df_financial_data.columns):
        df_financial_data.drop(columns=columnas_a_eliminar, inplace=True)

    # Eliminar la columna 'filmid' de df_financial_data si existe (para evitar duplicados)
    if 'filmid' in df_financial_data.columns:
        df_financial_data.drop(columns='filmid', inplace=True)

    # Hacer inner join entre IMDb y la información financiera
    df_final = df_imdb.join(df_financial_data, how='inner')

    # Unir con el DataFrame de Kaggle (filmid como índice)
    df_final = df_final.join(df_kaggle.set_index('filmid')[['year', 'winner', 'category']], on='filmid', how='inner')

    df_final['genre'] = df_final['genre'].str.split(',').str[0].str.strip()
    df_final['country'] = df_final['country'].str.split(',').str[0].str.strip()
    # Guardar el archivo final
    df_final.to_csv(ruta_salida, index=False)
    print(f"✅ Archivo final guardado como: {ruta_salida}")