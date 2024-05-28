echo "build start"
python -m pip install requirements.txt
python manage.py collectstatic --noinput --clear
echo "build end"