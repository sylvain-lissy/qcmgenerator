#Folder for kubernetes




# how to start routes for now (because we didnt have time to make a Dockerfile)


kubectl exec -ti nginxpodname -- bash

apt-get update
apt-get install gnupg 
apt-get install lsb-release
apt-get install docker.io
curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
apt-get install python3-pip
pip3 install Flask gunicorn
apt-get install libmariadb3
export FLASK_APP=app.py
apt-get install libmariadb-dev
pip3 install mariadb

cd /usr/share/nginx/html/
flask run


dans le conteneur nginx 
curl localhost:5000/addquestion
ça ajoutera une question à la bdd
(petit bemol, la database data n'est pas encore créée automatiquement dans mariadb + les tables non plus du coup donc il y aura une erreur)


