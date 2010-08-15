#!/bin/bash

[[ -f /home/dashline/.bash_profile ]] && source /home/dashline/.bash_profile

export DJANGO_SETTINGS_MODULE='dashline.settings'

ABSPATH=$(dirname $0)

python $ABSPATH/../manage.py update_index
