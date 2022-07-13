#!/usr/bin/env bash

source wmt_env/bin/activate

export FLASK_APP=src/__init__
export FLASK_ENV=development

cd db
python3 set_up_db.py
cd ..

flask run

deactivate

rm -rf db/tables.db
