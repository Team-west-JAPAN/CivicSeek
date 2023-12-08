# setup powershell script
python -m venv venv
./venv/Scripts/Activate.ps1 # activate virtual environment

pip install -r ./requirements.txt

python -m pip install --upgrade pip

python ./regenerateSecretKey.py

python ./manage.py migrate

python ./manage.py loaddata ./sample_db.json

python ./manage.py runserver

