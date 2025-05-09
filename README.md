# Project Oscar Insight  
**Do public ratings and profits influence the Academy's decisions?**

## 🎯 Objective

The goal of this project is to analyze whether public opinion — based on **Metacritic scores (Metascore)**, **IMDb ratings**, and the **ROI (Return on Investment)** of each film — has a measurable influence on the decisions made by the **Academy Awards (Oscars)**.

This study is motivated by the observation that many critically acclaimed and commercially successful films often do **not receive significant recognition** at the Oscars. The project aims to explore potential patterns or discrepancies between public reception and award outcomes.



## Functionality ⚙️

- 🌐 **Web Scraping**: Extract data from websites using automated scripts.  
- 🔗 **API Integration**: Collect structured data from public or private APIs.  
- 🧹 **Data Cleaning**: Process raw data to remove inconsistencies and prepare it for analysis.  
- 🧠 **Data Enrichment**: Combine multiple data sources to create a more comprehensive dataset.  
- 📊 **Exploratory Data Analysis**: Understand data distributions, relationships and anomalies.  
- 📈 **Data Visualization**: Create visual representations of the data to identify trends and patterns.  
- 📝 **Reporting**: Generate summary reports and figures to present findings


## Tools Used 🛠️

- 🐍 **Python**: Main programming language used for data processing and analysis.
- 🐼 **Pandas**: Library for data manipulation and analysis.
- 📡 **request**: Library for API managing.
- 🕸️ **Beautifulsoup**:Library for web scrapping. 
- 📊 **Matplotlib & Seaborn**: Libraries for data visualization.
- 📓 **Jupyter Notebooks**: Interactive environment for data cleaning and visualization.
- 🌐 **Git**: Version control system for tracking changes and collaboration.


## Development Process 🚀

1. 📥 **Data Collection**:  
   - Web scraping from **Box Office Mojo** for box office revenue data.  
   - Web scraping from **The Numbers** to extract production budgets.  
   - API requests to the **OMDb API** for ratings (IMDb, Metascore) and movie details.  
   - Initial dataset sourced from **Kaggle**, including Oscar nominations and wins.

2. 🧹 **Data Cleaning**:  
   - Filtered out unnecessary years and irrelevant entries.  
   - Handled missing values (NaNs).  
   - Selected and standardized relevant categories for the analysis.  
   - Calculated **ROI (Return on Investment)**.  
   - Merged and integrated all data into a unified DataFrame.

3. 🔍 **Data Analysis**:  
   - Explored relationships between ratings, ROI, and Oscar nominations/wins.  
   - Identified trends, outliers, and patterns in public reception versus Academy outcomes.

4. 📊 **Data Visualization**:  
   - Created graphs and charts to visualize correlations, distributions, and differences.  
   - Highlighted cases where high public approval did not align with Oscar recognition.

5. 📝 **Reporting**:  
   - Summarized findings and insights.  
   - Discussed limitations and suggested possible future research directions.


## Project Structure 📁

- `csv/`: Folder to keep main data cleaned for work with it.
  - `boxoffice_data.csv`: Dataset with the national, international and worldwide box office receipts for each film.
  - `final_dataset.csv`: Dataset with all data using for the project. 
  - `financial_data.csv`: Dataset with budgets,boxoffice and roi for each film. 
    - `raw/`: raw data extrac from kaggle, api and web scrapping.
      - `domestic_boxxoffice.csv`: data of domestic boxoffice for each film extracted from webscraping. 
      - `international_boxxoffice.csv`:data of international boxoffice for each film extracted from webscraping. 
      - `worldwide_boxxoffice.csv`:data of worldwide boxoffice for each film extracted from webscraping. 
      - `imbd_data.csv`: data from api request of OMDB API. 
      - `full_data.csv`: original dataset from kaggle.
      - `movie budget`: Data from www.the-numbers.com web scraping. 
      -  
- `visualizations/`: Folder with all grahps creates to analyse. All of them have been created in `visualization.ipynb` Jupyter Notebook.
- `src/`:  
  - `api_omdb.ipynb`: Jupyter Notebook where extract the data from api request to OMDB API. 
  - `data_wrangling.ipynb`: Jupyter Notebooks where data is cleaning.
  - `main.ipynb`: Jupyter Notebooks where all the workflow was done.
  - `web_scrapping.ipynb`: Jupyther Notebooks where the web scraping process takes place from www.boxofficemojo.com and www.the-numbers.com.
  - `visualizacion.ipynb`: Jupyter Notebook where the wisualization was done. 
- `function files/`:Python scripts with utility functions.
  - `api_function.py`: Python scripts for api request.
  - `data_function.py`: Python scripts for cleaning datasets.
  - `web_scraping_functions.py`: Python scripts for web scrapping process. 
- `presentation/`: Folder to store PDF presentations.
- `README.md`: File to describe the project and how to set it up.
- `requirements.txt`: File to list the project dependencies.

## Project Members 👥

| **Andrés Muñoz** |
| **César Méndez** | 
| **Francisco Bretones** | 
| **Jon McGowan** | 
| **Sergio Blázquez** |
