# webfortune

<h3>Docker</h3>

Build Docker image:
 - docker build -t hamlvan/webfortune .

Run Docker image:
 - docker run -dp 8005:5000 hamlvan/webfortune

Debugging/Checking the logs:
 - docker logs \<container_id>

Delete the image:
 - docker rm -f \<container_id>

<h3>Local</h3>
Run App Locally:

 - python3 -m venv env (only first time or when in new directory)

 - pip install -r requirements.txt (only first time or when in new directory or if requirements have changed)
 
  - source env/bin/activate
 
  - python3 -m flask run --host=0.0.0.0 --port=8005 (on my group's specific port)

<h4>To see the application running:</h4>

- http://10.92.21.106:8005/

<h4>The Implemented Routes:</h4>

  - GET /fortune/ - should simply display the output of the 'fortune' command.
 
  - GET /cowsay/\<message>/ - should display the output of the 'cowsay' command given <message> as its command line input

 - GET /cowfortune/ - should pipe the output of fortune as the input to the cowsay command

 - GET / - redirects to GET /fortune/

<h4>Testing:</h4>

- pytest test_app.py (from the commandline)

- GitHub Actions Page to check if everything is working properly with commits
