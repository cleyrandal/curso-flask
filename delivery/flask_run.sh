#!/bin/sh

export FLASK_APP=delivery/app.py

#export FLASK_ENV=development #deprecated
export FLASK_DEBUG=True

flask run
