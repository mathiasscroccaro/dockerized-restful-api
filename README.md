# Simple Flask REST API, Postgres and Pgadmin integration through Docker

In this application, a REST API, developed with Flask Python library, get and insert data into a Postgres DB. All data can be administrated through Pgadmin web interface.

The Postgres DB container does not expose its port outside docker enclouser. Only the REST API and the PgAdmin web interface can be see outside.  

## Setup

`mkdir db`

`mkdir pgadmin`

`sudo chown -R 5050:5050 pgadmin`

`sudo docker-compose up`

or

`./setup.sh`

for mor information why 'pgadmin' folder is changed its ownership, see this [link](https://www.pgadmin.org/docs/pgadmin4/latest/container_deployment.html#mapped-files-and-directories)
