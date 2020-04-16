## Setup django app

1) Create local.py in test_task/test_task/settings similar to local.py.dist
2) Create virtualenv ```virtualenv --python=`which python3` <env_dir>```
3) Activate virtualenv ```source <env_dir>/bin/activate```
4) Install requirements ```pip install -r requirements.txt```
5) Run  ```./manage.py migrate```


## Run django app

1) execute:
    1) `export DJANGO_SETTINGS_MODULE="test_task.settings.local"`
    2) `export WERKZEUG_DEBUG_PIN=off`
2) execute `python manage.py runserver_plus 0.0.0.0:8000`

## Run Test Bot app
1) Run ``` python test_bot/bot.py```