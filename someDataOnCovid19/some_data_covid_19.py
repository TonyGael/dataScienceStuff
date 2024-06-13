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
    
    # if not os.path.exists(file_path): Utiliza os.path.exists() para verificar si el archivo especificado por file_path existe en el sistema de archivos.
    # if not os.path.exists(file_path): Uses os.path.exists() to check if the file specified by file_path exists in the filesystem.
    if not os.path.exists(file_path):
        # raise FileNotFoundError(f"El archivo {file_path} no existe."): Si el archivo no existe, se lanza una excepción FileNotFoundError con un mensaje que indica qué archivo no se encontró.
        # raise FileNotFoundError(f"El archivo {file_path} no existe."): If the file does not exist, it raises a FileNotFoundError with a message indicating which file was not found.
        raise FileNotFoundError(f"El archivo {file_path} no existe.")
    # df = pd.read_csv(file_path): Utiliza pd.read_csv() de Pandas para leer el archivo CSV especificado por file_path y cargarlo como un DataFrame df.
    # df = pd.read_csv(file_path): Uses Pandas' pd.read_csv() to read the CSV file specified by file_path and load it into a DataFrame df.
    df = pd.read_csv(file_path)
    # return df: Devuelve el DataFrame cargado como resultado de la función load_data.
    # return df: Returns the loaded DataFrame as the result of the load_data function.
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
    
    # Crea un diccionario vacío llamado results para almacenar los resultados del análisis.
    # Creates an empty dictionary called results to store the analysis results.
    results = {}

    # Total cases and deaths
    # Total de casos y muertes
    
    # df['total_cases'].max(): Selecciona la columna 'total_cases' del DataFrame df y encuentra el valor máximo, que representa el total de casos.
    # df['total_cases'].max(): Selects the 'total_cases' column from the DataFrame df and finds the maximum value, representing the total cases.
    total_cases = df['total_cases'].max()
    # df['total_deaths'].max(): Selecciona la columna 'total_deaths' del DataFrame df y encuentra el valor máximo, que representa el total de muertes.
    # df['total_deaths'].max(): Selects the 'total_deaths' column from the DataFrame df and finds the maximum value, representing the total deaths.
    total_deaths = df['total_deaths'].max()
    # results['Total Cases'] = total_cases: Almacena el valor de total_cases en el diccionario results con la clave 'Total Cases'.
    # results['Total Cases'] = total_cases: Stores the value of total_cases in the results dictionary with the key 'Total Cases'.
    results['Total Cases'] = total_cases
    # results['Total Deaths'] = total_deaths: Almacena el valor de total_deaths en el diccionario results con la clave 'Total Deaths'.
    # results['Total Deaths'] = total_deaths: Stores the value of total_deaths in the results dictionary with the key 'Total Deaths'.
    results['Total Deaths'] = total_deaths

    # New cases and deaths per day
    # Nuevos casos y muertes por día
    
    # df.groupby('date')['new_cases'].sum(): Agrupa el DataFrame df por la columna 'date' y suma los valores de 'new_cases' para cada fecha, obteniendo el total de nuevos casos por día.
    # df.groupby('date')['new_cases'].sum(): Groups the DataFrame df by the 'date' column and sums the 'new_cases' values for each date, obtaining the total new cases per day.
    daily_cases = df.groupby('date')['new_cases'].sum()
    # df.groupby('date')['new_deaths'].sum(): Agrupa el DataFrame df por la columna 'date' y suma los valores de 'new_deaths' para cada fecha, obteniendo el total de nuevas muertes por día.
    # df.groupby('date')['new_deaths'].sum(): Groups the DataFrame df by the 'date' column and sums the 'new_deaths' values for each date, obtaining the total new deaths per day.
    daily_deaths = df.groupby('date')['new_deaths'].sum()
    # results['Daily Cases'] = daily_cases: Almacena la serie daily_cases en el diccionario results con la clave 'Daily Cases'.
    # results['Daily Cases'] = daily_cases: Stores the daily_cases series in the results dictionary with the key 'Daily Cases'.
    results['Daily Cases'] = daily_cases
    # results['Daily Deaths'] = daily_deaths: Almacena la serie daily_deaths en el diccionario results con la clave 'Daily Deaths'.
    # results['Daily Deaths'] = daily_deaths: Stores the daily_deaths series in the results dictionary with the key 'Daily Deaths'.
    results['Daily Deaths'] = daily_deaths

    # Average new cases and deaths
    # Promedio de nuevos casos y muertes
    
    # daily_cases.mean(): Calcula el promedio de la serie daily_cases, obteniendo el promedio de nuevos casos diarios.
    # daily_cases.mean(): Calculates the mean of the daily_cases series, obtaining the average daily new cases.
    avg_new_cases = daily_cases.mean()
    # daily_deaths.mean(): Calcula el promedio de la serie daily_deaths, obteniendo el promedio de nuevas muertes diarias.
    # daily_deaths.mean(): Calculates the mean of the daily_deaths series, obtaining the average daily new deaths.
    avg_new_deaths = daily_deaths.mean()
    # results['Average Daily Cases'] = avg_new_cases: Almacena el valor de avg_new_cases en el diccionario results con la clave 'Average Daily Cases'.
    # results['Average Daily Cases'] = avg_new_cases: Stores the value of avg_new_cases in the results dictionary with the key 'Average Daily Cases'.
    results['Average Daily Cases'] = avg_new_cases
    # results['Average Daily Deaths'] = avg_new_deaths: Almacena el valor de avg_new_deaths en el diccionario results con la clave 'Average Daily Deaths'.
    # results['Average Daily Deaths'] = avg_new_deaths: Stores the value of avg_new_deaths in the results dictionary with the key 'Average Daily Deaths'.
    results['Average Daily Deaths'] = avg_new_deaths

    # Day with the most cases and deaths
    # Día con más casos y muertes
    
    # daily_cases.idxmax(): Encuentra el índice (fecha) donde daily_cases tiene su valor máximo, es decir, el día con más casos.
    # daily_cases.idxmax(): Finds the index (date) where daily_cases has its maximum value, i.e., the day with the most cases.
    max_cases_day = daily_cases.idxmax()
    # daily_deaths.idxmax(): Encuentra el índice (fecha) donde daily_deaths tiene su valor máximo, es decir, el día con más muertes.
    # daily_deaths.idxmax(): Finds the index (date) where daily_deaths has its maximum value, i.e., the day with the most deaths.
    max_deaths_day = daily_deaths.idxmax()
    # results['Day with Most Cases'] = max_cases_day: Almacena el valor de max_cases_day en el diccionario results con la clave 'Day with Most Cases'.
    # results['Day with Most Cases'] = max_cases_day: Stores the value of max_cases_day in the results dictionary with the key 'Day with Most Cases'.
    results['Day with Most Cases'] = max_cases_day
    # results['Day with Most Deaths'] = max_deaths_day: Almacena el valor de max_deaths_day en el diccionario results con la clave 'Day with Most Deaths'.
    # results['Day with Most Deaths'] = max_deaths_day: Stores the value of max_deaths_day in the results dictionary with the key 'Day with Most Deaths'.
    results['Day with Most Deaths'] = max_deaths_day

    # Cumulative cases and deaths per month
    # Casos y muertes acumulados por mes
    
    # df['date'].dt.to_period('M'): Convierte la columna 'date' en periodos mensuales.
    # df['date'].dt.to_period('M'): Converts the 'date' column to monthly periods.
    # df['month']: Crea una nueva columna en el DataFrame df llamada 'month', que contiene los periodos mensuales derivados de 'date'.
    # df['month']: Creates a new column in the DataFrame df called 'month', which contains the monthly periods derived from 'date'.
    df['month'] = df['date'].dt.to_period('M')
    # df.groupby('month')['new_cases'].sum(): Agrupa el DataFrame df por la columna 'month' y suma los valores de 'new_cases' para cada mes, obteniendo el total de nuevos casos por mes.
    # df.groupby('month')['new_cases'].sum(): Groups the DataFrame df by the 'month' column and sums the 'new_cases' values for each month, obtaining the total new cases per month.
    monthly_cases = df.groupby('month')['new_cases'].sum()
    # df.groupby('month')['new_deaths'].sum(): Agrupa el DataFrame df por la columna 'month' y suma los valores de 'new_deaths' para cada mes, obteniendo el total de nuevas muertes por mes.
    # df.groupby('month')['new_deaths'].sum(): Groups the DataFrame df by the 'month' column and sums the 'new_deaths' values for each month, obtaining the total new deaths per month.
    monthly_deaths = df.groupby('month')['new_deaths'].sum()
    # results['Monthly Cases'] = monthly_cases: Almacena la serie monthly_cases en el diccionario results con la clave 'Monthly Cases'.
    # results['Monthly Cases'] = monthly_cases: Stores the monthly_cases series in the results dictionary with the key 'Monthly Cases'.
    results['Monthly Cases'] = monthly_cases
    # results['Monthly Deaths'] = monthly_deaths: Almacena la serie monthly_deaths en el diccionario results con la clave 'Monthly Deaths'.
    # results['Monthly Deaths'] = monthly_deaths: Stores the monthly_deaths series in the results dictionary with the key 'Monthly Deaths'.
    results['Monthly Deaths'] = monthly_deaths

    # Este return devuelve el diccionario results que contiene todos los resultados del análisis.
    # This return returns the results dictionary containing all the analysis results.
    return results

def main():
    
    # file_path = 'owid-covid-data.csv': Define la ruta del archivo CSV que contiene los datos de COVID-19.
    # file_path = 'owid-covid-data.csv': Defines the path to the CSV file containing the COVID-19 data.
    file_path = 'owid-covid-data.csv'
    # country = 'Argentina': Especifica el país de interés para el análisis.
    # country = 'Argentina': Specifies the country of interest for the analysis.
    country = 'Argentina'
    
    # print("Cargando datos..."): Imprime un mensaje en la consola indicando que se está cargando el archivo de datos.
    # print("Cargando datos..."): Prints a message to the console indicating that the data file is being loaded.
    print("Cargando datos...")
    # df = load_data(file_path): Llama a la función load_data con file_path como argumento y asigna el DataFrame resultante a la variable df.
    # df = load_data(file_path): Calls the load_data function with file_path as an argument and assigns the resulting DataFrame to the variable df.
    df = load_data(file_path)
    
    # print(f"Preprocesando datos para {country}..."): Imprime un mensaje en la consola indicando que se están preprocesando los datos para el país especificado.
    # print(f"Preprocesando datos para {country}..."): Prints a message to the console indicating that the data is being preprocessed for the specified country.
    print(f"Preprocesando datos para {country}...")
    # country_df = preprocess_data(df, country): Llama a la función preprocess_data con df y country como argumentos y asigna el DataFrame resultante a la variable country_df.
    # country_df = preprocess_data(df, country): Calls the preprocess_data function with df and country as arguments and assigns the resulting DataFrame to the variable country_df.
    country_df = preprocess_data(df, country)
    
    # print("Analizando datos..."): Imprime un mensaje en la consola indicando que se está realizando el análisis de datos.
    # print("Analizando datos..."): Prints a message to the console indicating that data analysis is being performed.
    print("Analizando datos...")
    # results = analyze_data(country_df): Llama a la función analyze_data con country_df como argumento y asigna el diccionario resultante a la variable results.
    # results = analyze_data(country_df): Calls the analyze_data function with country_df as an argument and assigns the resulting dictionary to the variable results.
    results = analyze_data(country_df)
    
    # print("Resultados del análisis:"): Imprime un encabezado para los resultados del análisis.
    # print("Resultados del análisis:"): Prints a header for the analysis results.
    # print(f"Total de casos: {results['Total Cases']}"): Imprime el total de casos desde el diccionario results.
    # print(f"Total de casos: {results['Total Cases']}"): Prints the total cases from the results dictionary.
    # print(f"Total de muertes: {results['Total Deaths']}"): Imprime el total de muertes desde el diccionario results.
    # print(f"Total de muertes: {results['Total Deaths']}"): Prints the total deaths from the results dictionary.
    # print(f"Promedio diario de casos nuevos: {results['Average Daily Cases']}"): Imprime el promedio diario de casos nuevos desde el diccionario results.
    # print(f"Promedio diario de casos nuevos: {results['Average Daily Cases']}"): Prints the average daily new cases from the results dictionary.
    # print(f"Promedio diario de muertes nuevas: {results['Average Daily Deaths']}"): Imprime el promedio diario de muertes nuevas desde el diccionario results.
    # print(f"Promedio diario de muertes nuevas: {results['Average Daily Deaths']}"): Prints the average daily new deaths from the results dictionary.
    # print(f"Día con más casos: {results['Day with Most Cases']}"): Imprime el día con más casos desde el diccionario results.
    # print(f"Día con más casos: {results['Day with Most Cases']}"): Prints the day with the most cases from the results dictionary.
    # print(f"Día con más muertes: {results['Day with Most Deaths']}"): Imprime el día con más muertes desde el diccionario results.
    # print(f"Día con más muertes: {results['Day with Most Deaths']}"): Prints the day with the most deaths from the results dictionary.
    # print("Casos mensuales:"): Imprime un encabezado para los casos mensuales.
    # print("Casos mensuales:"): Prints a header for the monthly cases.
    # print(results['Monthly Cases']): Imprime la serie de casos mensuales desde el diccionario results.
    # print(results['Monthly Cases']): Prints the monthly cases series from the results dictionary.
    # print("Muertes mensuales:"): Imprime un encabezado para las muertes mensuales.
    # print("Muertes mensuales:"): Prints a header for the monthly deaths.
    # print(results['Monthly Deaths']): Imprime la serie de muertes mensuales desde el diccionario results.
    # print(results['Monthly Deaths']): Prints the monthly deaths series from the results dictionary.
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

# if name == "main": Esta línea verifica si el script está siendo ejecutado directamente. En Python, cuando un script se ejecuta directamente, Python establece la variable especial __name__ en "__main__". Esto permite diferenciar si el archivo se está ejecutando como un programa principal o si está siendo importado como un módulo en otro script.
# if name == "main": This line checks if the script is being executed directly. In Python, when a script is run directly, Python sets the special variable __name__ to "__main__". This allows distinguishing whether the file is being run as a main program or if it's being imported as a module in another script.
if __name__ == "__main__":
    # main(): Si la condición if __name__ == "__main__" se cumple (es decir, el script se está ejecutando directamente), se llama a la función main(). Esto inicia la ejecución del programa según lo definido en la función main, que incluye cargar datos, preprocesarlos, analizarlos y mostrar resultados.
    # main(): If the if __name__ == "__main__" condition is true (meaning the script is being executed directly), it calls the main() function. This initiates the program's execution as defined within the main() function, which typically includes tasks such as loading data, preprocessing, analysis, and displaying results.
    main()
