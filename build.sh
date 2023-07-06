#Install Dependencies
pip3 install -r deps.txt

#collect static files
python3 manage.py collectstatic --no-input

# Run Migrations
python3 manage.py migrate