# webfortune


Build Docker image:

- docker build -t hamlvan/webfortune .

docker run -dp 8005:5000 hamlvan/webfortune

docker logs \<container_id>

docker rm -f \<container_id>


Run App Locally:
 - python3 -m venv env (only first time or when in new directory)
 - pip install -r requirements.txt (only first time or when in new directory or if requirements have changed)
 
  - source env/bin/activate
  - python3 -m flask run --host=0.0.0.0 --port=8005 (on my group's specific port)

To see the application running:
 - http://10.92.21.106:8005/

The Implemented Routes:
  - GET /fortune/ - should simply display the output of the 'fortune' command.
  - GET /cowsay/\<message>/ - should display the output of the 'cowsay' command given <message> as its command line input
  - GET /cowfortune/ - should pipe the output of fortune as the input to the cowsay command
  - GET / - redirects to GET /fortune/

Testing:
  - pytest-3 test_app.py
