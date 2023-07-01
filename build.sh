#Install Dependencies
pip install -r deps.txt

#collect static files
python manage.py collectstatic --no-input

# Run Migrations
python3 manage.py migrate