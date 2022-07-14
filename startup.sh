#!/usr/bin/env bash

source wmt_env/bin/activate

export FLASK_APP=src/flaskp
export FLASK_ENV=development

python3 src/set_up_db.py

flask run

deactivate

rm -rf db/tables.db
