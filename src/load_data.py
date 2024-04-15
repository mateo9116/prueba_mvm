from pandas import DataFrame
import psycopg

from utils import path_to_list, display_log

def dataframe_to_posgres(company_data:DataFrame, args:str) -> None:
    """
    La función 'dataframe_to_posgres' se encarga de tomar un dataframe, realizar la conexión a la base de datos
    y hacer el poblado de la misma fila por fila del dataframe
    :parámetro company_data: es el datafram con la información
    :parámetro args: es el namespace que se generó con la información de conexión a la base de datos
    """
    postgres_settings: list[str] = path_to_list(path=args) 
    try:
        conn:psycopg.connect = psycopg.connect(conninfo=" ".join(postgres_settings["authentication"]))
    except:
        display_log(message="Error en la conexión a la base de datos")
    with conn.cursor() as cur:
        try:
            with cur.copy(statement=f"COPY {postgres_settings['table']} (nombre, cargo, departamento, id) FROM STDIN") as copy:
                for record in company_data.to_records(index=False):
                    copy.write_row(record)
        except:
            display_log(message="Error al escribir en la base de datos")

