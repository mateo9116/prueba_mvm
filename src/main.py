from argparse import Namespace
from uuid import uuid4
import awswrangler as wr
import logging
from pandas import DataFrame
import random

from load_data import dataframe_to_posgres
from utils import display_log, parse_args, path_to_list
from interface import app

LOG_FILE = LOGFILE = './prueba_tecnica.log'

def main():
    '''
    Esta funición es la base principal de código, desde acá se hace la citación y ejeción principal del programa, de tal forma
    que modularmente se permita tener una mayor trazabilidad de la información y la ejecución, además hacer más fácil le depuración
    '''

    logging.basicConfig(filename=LOGFILE, filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.WARNING)
    display_log(message='[Bienvenido al desarrollo de la prueba técnica realizada por Mateo Restrepo]')

    # Se analiza la información de entrada
    args: Namespace = parse_args(description_text="Información parcial de la empresa")

    departamentos:list[str] = path_to_list(path=args.json_departamentos, key='nombre')
    cargos:list[str] = path_to_list(path=args.json_cargos, key='nombre')
    empleados:list[str] = path_to_list(path=args.json_empleados, key='nombre')
    
    #Se crea un dataframe solo con las columnas necesarias
    company_data:DataFrame = DataFrame(columns=["nombre", "cargo", "departamento", "id"])
    company_data['nombre'] = empleados

    #Se realizan funciones que eligen valores aleatorios de listas para asignarle a los empleados
    company_data['cargo'] = company_data['cargo'].apply(func=lambda x: random.choice(seq=cargos))
    company_data['departamento'] = company_data['departamento'].apply(func=lambda x: random.choice(seq=departamentos))
    company_data['id'] = company_data['id'].apply(func=lambda x: uuid4())

    company_data.to_csv(path_or_buf='informacion_de_la_empresa.csv')
    bucket = 'prueba_mvm'
    wr.s3.to_csv(
        df=company_data,
        path=f's3://{bucket}/prefix/my_file.csv',
    )

    dataframe_to_posgres(company_data=company_data, args=args.db_connection)
    app()

if __name__ == "__main__":
    main()