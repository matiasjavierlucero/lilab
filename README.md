
# [WIP] Project to analyze personal credits

## Run docker compose for up Postgres and Nginx
 - *docker-compose up -d*

## Run project
 - clone this repository
 - create a virtual environt with *pipenv shell*
 - run *pip install -r requierements.txt*
 - run *export FLASK_SETTINGS='config'*
 - run *flask db init*
 - run *flask db migrate*
 - run *flask db upgrade*
 
