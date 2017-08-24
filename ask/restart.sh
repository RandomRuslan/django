#!/bin/bash
n=(`sudo ps -ea | grep gunicorn`)
sudo kill ${n[0]}
sudo gunicorn -b "0.0.0.0:8000" ask.wsgi:application &

