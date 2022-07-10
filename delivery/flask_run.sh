#!/bin/sh

export FLASK_APP=delivery/app.py
export FLASK_ENV=development

flask run
