echo "---tai thu vien---"
pip install -r requirements.txt

echo "---tai du lieu---"
python eapp/models.py

echo "---chay du lieu---"
python -m flash run eapp/index.py