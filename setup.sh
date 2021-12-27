#!/bin/bash

mkdir db
mkdir pgadmin
sudo chown -R 5050:5050 pgadmin

sudo docker-compose build
sudo docker-compose up &

sleep 5

python3 ./rest_api/db_tool.py
