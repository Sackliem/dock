#!/bin/bash
set -e 

exec python Recept/menu_upd.py &
exec python Recept/tgbot.py
