#!/bin/sh

export FLASK_APP=delivery/app.py
export FLASK_DEBUG=True

flask run
