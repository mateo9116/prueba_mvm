#!/bin/bash

python3 /opt/prueba_mvm/bin/main.py

uvicorn api:app --host 0.0.0.0 --port 80