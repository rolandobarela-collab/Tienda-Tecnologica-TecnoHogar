#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python tecnohogar/manage.py collectstatic --no-input
python tecnohogar/manage.py migrate