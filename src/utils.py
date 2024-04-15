import argparse
import logging
from icecream import ic
import json

def display_log(message:str) -> None:
    ic(message)
    logging.warning(msg=message)

def parse_args(description_text:str) -> argparse.Namespace:
    """
    La fución parse_argas usa el módulo 'argparse para definir y analizar los argumentos
    necesarios para correr la prueba técnica
    :retorna: La función 'parse_args()' returna el análisis de la línea de comandos como
    un objeto 'argparse.Namespace'
    """
    parser = argparse.ArgumentParser(description=description_text)
    parser.add_argument("--json-departamentos", help="información de departamentos", required=True)
    parser.add_argument("--db-connection", help="información de conección a la base de datos", required=True)
    parser.add_argument("--json-cargos", help="información de cargos", required=True)
    parser.add_argument("--json-empleados", help="información de empleados", required=True)

    args: argparse.Namespace = parser.parse_args()
    return args

def path_to_list(path:str, key:str|None=None) -> list[str]:
    """
    Esta función 'path_to_list' se encarga de leer archivos tipo json y convertirlos en lista
    filtrada por las llaves requeridas por el usuario
    :parámetro path: ruta del archivo en formato json 
    :parámetro key: llave del documento json por la cual se quiere filtrar la información 
    :retorna: La función 'path_to_list' retorna una lista de valores tipo string
    """

    with open(file=path) as f_in:
        if key == None:
            lista:list[str] = json.load(fp=f_in)
        else:
            lista:list[str] = json.load(fp=f_in)[key]
    return lista