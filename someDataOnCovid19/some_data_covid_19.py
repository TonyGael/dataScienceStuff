# cd /ruta/a/tu/proyecto        # Navega al directorio de tu proyecto
# python -m venv venv           # Crea un entorno virtual
# source venv/bin/activate      # Activa el entorno virtual (macOS/Linux)
# pip install pandas            # Instala pandas
# python -c "import pandas as pd; print(pd.__version__)"  # Verifica la instalación desde consola
# print(pd.__version__)         # Verifica la instalación desde el archivo py
# deactivate                    # Desactiva el entorno virtual

# link para descargar el archivo a explotar:
# https://covid.ourworldindata.org/data/owid-covid-data.csv

import pandas as pd
import os

def load_data(file_path):
    """
    Carga los datos de COVID-19 desde un archivo CSV local.
    
    Load COVID-19 data from a local CSV file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"El archivo {file_path} no existe.")
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df, country):
    """
    Preprocesa los datos para un país específico.
    Preprocesses data for a specific country.
    """
    
    # Convierte la columna 'date' a un formato de fecha y hora
    # Converts the 'date' column to a datetime format
    df['date'] = pd.to_datetime(df['date'])
    # Filtra el DataFrame para incluir solo las filas donde la columna 'location' es igual al país especificado
    # Filters the DataFrame to include only rows where the 'location' column matches the specified country
    country_df = df[df['location'] == country]
    # Llena los valores faltantes (NaN) con 0 en el DataFrame filtrado
    # Fills missing values (NaN) with 0 in the filtered DataFrame
    country_df.fillna(0, inplace=True)
    # Devuelve el DataFrame filtrado y preprocesado
    # Returns the filtered and preprocessed DataFrame
    return country_df

def analyze_data(df):
    """
    Realiza análisis de datos usando pandas.
    Perform data analysis using pandas.
    """
    results = {}

    # Total cases and deaths
    # Total de casos y muertes
    total_cases = df['total_cases'].max()
    total_deaths = df['total_deaths'].max()
    results['Total Cases'] = total_cases
    results['Total Deaths'] = total_deaths

    # New cases and deaths per day
    # Nuevos casos y muertes por día
    daily_cases = df.groupby('date')['new_cases'].sum()
    daily_deaths = df.groupby('date')['new_deaths'].sum()
    results['Daily Cases'] = daily_cases
    results['Daily Deaths'] = daily_deaths

    # Average new cases and deaths
    # Promedio de nuevos casos y muertes
    avg_new_cases = daily_cases.mean()
    avg_new_deaths = daily_deaths.mean()
    results['Average Daily Cases'] = avg_new_cases
    results['Average Daily Deaths'] = avg_new_deaths

    # Day with the most cases and deaths
    # Día con más casos y muertes
    max_cases_day = daily_cases.idxmax()
    max_deaths_day = daily_deaths.idxmax()
    results['Day with Most Cases'] = max_cases_day
    results['Day with Most Deaths'] = max_deaths_day

    # Cumulative cases and deaths per month
    # Casos y muertes acumulados por mes
    df['month'] = df['date'].dt.to_period('M')
    monthly_cases = df.groupby('month')['new_cases'].sum()
    monthly_deaths = df.groupby('month')['new_deaths'].sum()
    results['Monthly Cases'] = monthly_cases
    results['Monthly Deaths'] = monthly_deaths

    return results

def main():
    file_path = 'owid-covid-data.csv'
    country = 'Argentina'
    
    print("Cargando datos...")
    df = load_data(file_path)
    
    print(f"Preprocesando datos para {country}...")
    country_df = preprocess_data(df, country)
    
    print("Analizando datos...")
    results = analyze_data(country_df)
    
    print("Resultados del análisis:")
    print(f"Total de casos: {results['Total Cases']}")
    print(f"Total de muertes: {results['Total Deaths']}")
    print(f"Promedio diario de casos nuevos: {results['Average Daily Cases']}")
    print(f"Promedio diario de muertes nuevas: {results['Average Daily Deaths']}")
    print(f"Día con más casos: {results['Day with Most Cases']}")
    print(f"Día con más muertes: {results['Day with Most Deaths']}")
    print("Casos mensuales:")
    print(results['Monthly Cases'])
    print("Muertes mensuales:")
    print(results['Monthly Deaths'])

if __name__ == "__main__":
    main()
