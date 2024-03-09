echo "BUILD START"
pip install -r requirements.txt
python3.11.7 manage.py collectstatic
echo "BUILD END"