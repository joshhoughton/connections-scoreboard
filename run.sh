#!/bin/bash

exec python3 /app/bot/main.py &
exec python3 python3 -m flask run --host=0.0.0.0