# Simple Flask Application

  Flask Installation Guide and Docs : https://flask.palletsprojects.com/en/3.0.x/installation/#python-version

  
  Flask Documentation : https://flask.palletsprojects.com/en/3.0.x/

  flask run --help [ To take help from the flask run commands ]

  flask run -h 0.0.0.0 -p 5001 --debug [ To run the flask app with host , port , debug on mode ]

         (or)

  python app.py

  pip3 freeze [ To see list of softwares and dependencies ]

  pip3 freeze > requirements.txt [ To store the list of softwares into the requirements.txt ]

  pip3 install -r requirements.txt [ To install all softwares and dependencies require for application using requirements file ]

  curl <website-url>

  curl http://127.0.0.1:5001/hello

  curl -I <website-url>

  curl -I http://127.0.0.1:5001/hello

 

### Code of Url & Routes in Flask

  from flask import Flask, request, make_response

  app = Flask(__name__)

  @app.route('/')
  def index():
    return "<h1>Welcome to the Python Flask Application</h1>"

  '''
  @app.route('/hello', methods=["GET","POST"])
  def hello():
    if (request.method == "GET"):
      return "You made a GET request\n"
    elif (request.method == "POST"):
      return "You made a POST request\n"
    else:
      return "You will never see this message\n"
  '''

  @app.route('/hello')
  def hello():
    response = make_response('Hello World\n')
    response.status_code = 202
    response.headers['content-type'] = 'application/octet-stream'
    return response

  # url params
  @app.route('/greet/<name>')
  def greet(name):
    return f"<h1>Hello {name}</h1>"

  # url params
  @app.route('/add/<int:num1>/<int:num2>')
  def add(num1,num2):
    return f"<h2>{num1} + {num2} = {num1 + num2}</h2>"

  # url query params
  @app.route('/handle_url_params')
  def handle_params():
    if ('greeting' in request.args.keys() and 'name' in request.args.keys()):
      greeting = request.args['greeting']
      name = request.args.get('name')
      return f'{greeting}, {name}'
    else:
      return 'Some parameters are missing'

  if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)




   
==============================================
   Dockerizing a real-world web application
==============================================

1. Download the postgresql docker image from docker registry 

$ docker image pull postgres

2. Create a docker volume

$ docker volume --help
$ docker volume create pgdata
$ docker volume ls

3. Create a docker network

$ docker network --help
$ docker network create library-network
$ docker network ls

4. Run the Database docker image

$ docker container --help

$ docker container run --rm --name=dev-postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=books -v pgdata:/var/lib/postgresql/data --network=library-network postgres

$ docker container ls 

$ docker container ls -a

5. Build the Flask App with Postgresql DB [simple-flask-application-with-postgresql]

$ docker image build -t library-app:1.0 .

6. Run the Docker Container using Docker Image [library-app:1.0]

$ docker container run --rm -p 5000:5000 --network=library-network library-app:1.0

7. Go to the Docker Postgresql DB Container using interative mode execute some commands

$ docker exec -it <container-id/container-name> /bin/bash

$ docker exec -it 2aff1f2b2a3c /bin/bash

  root@2aff1f2b2a3c:/app# python

  >> from app import db

  >> db.create_all()

  >> exit()

  root@2aff1f2b2a3c:/app# exit
  exit

$

8. Run the application in web browser using ip-address and port number

   http://localhost:5000/

9. To the stop the docker containers

   $ docker container stop 2aff1f2b2a3c

   $ docker container stop dev-postgres


10. Again the run the docker containers of postgresql and library-app.


    Note: Test the app existing books are present or not.