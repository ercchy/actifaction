# ACTIFACTION

Our first serious project.

## Setup

```bash
virtualenv venv           # setting up virtual environment for the first time
source venv/bin/activate  # activating virtual environment

pip install -r requirements.txt         # install requirements
python actifaction/manage.py syncdb     # run Djangos DB sync
python actifaction/manage.py runserver  # run Django server
```

Open browser on [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
