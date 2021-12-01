#!/bin/bash

if [[ -f "secrets" ]]; then
    echo "secrets file found. sourcing it."
    source secrets
else
    echo "secrets file not found. ignoring."
fi

export FLASK_APP=server/main.py
export FLASK_ENV=development

gunicorn -c gunicorn_config.py --reload server.main:app
