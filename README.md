# flask-crud-api
Simple flask api to create, get, update and delete users. Uses SQLite.
## Installation
#### Clone the project.
```
git clone https://.....
```
#### Create a virtual environment to install packages (optional but recommended)
```
python3 -m venv env
source env/bin/activate
```
If Python returns an error for `venv`, read about [Installing packages using pip and virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).
#### Install packages.
```
pip install -r requirements.txt

```
Export
```
export FLASK_APP=app.py export FLASK_DEBUG=True
```

Create DB
```

python
from app import db 
db.create_all() 
exit()
```



#### Run server.
```
python3 app.py
```





POST 
curl --request POST \
  --url http://localhost:5000/api/dates \
  --header 'Content-Type: application/json' \
  --data '{
	"pub_date": "2023-03-08 09:53:53"
}'

curl --request DELETE \
  --url 'http://localhost:5000/api/dates?id=32%2C34' \
  --header 'Content-Type: application/json'




