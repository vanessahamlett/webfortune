# webfortune


Build Docker image:
docker build -t webfortune .

docker run -dp 8005:5000 hamlvan/webfortune

docker logs <container_id>

docker rm -f <container_id>


Run App Locally:
python3 -m venv env
source env/bin/activate
pip install -r requirments.txt

python3 -m flask run --host=0.0.0.0 --port=8005
http://10.92.21.106:8005/
