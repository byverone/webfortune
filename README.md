# webfortune
Dev ops final project

To just run the flask app. Run the following:
(Must have python3 installed and virtualenv)

virtualenv -p python3 env

source env/bin/activate

pip install -r requirements.txt

./runlocal.sh

# preferred method
To run the flask app with Docker. Run the following
docker build -t webfortune .
docker run -dp 5000:5000 webfortune

Routes are:

/

redirects to /fortune


/fortune

runs the fotune command in bash and gives a fortune as output


/cowsay/<message>

runs the cowsay command in bash and gives the <message> as the part of cowsay in output


/cowfortune

runs the fortune | cowsay command in bash


/cmd/<command>

run any bash command, from input <command>


Note

pytests is ran as a github action


if manual testing wanted:

pytest tests.py

![Pytests](https://github.com/byverone/webfortune/actions/workflows/python-app.yml/badge.svg)
