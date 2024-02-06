#!/bin/bash

export FLASK_APP=/app/connections_scoreboard/app
export PYTHONPATH=$PYTHONPATH:/app/

python3 -u /app/connections_scoreboard/bot/main.py &
python3 -m flask run --host=0.0.0.0
