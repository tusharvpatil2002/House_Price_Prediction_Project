echo " BUILD START"
# Install dependencies
python 3.12.2 -m pip install -r requirements.txt

# Collect static files
python 3.12.2 manage.py collectstatic --noinput --clear

echo " BUILD END"
