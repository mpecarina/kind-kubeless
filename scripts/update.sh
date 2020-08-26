#!/bin/bash

kubeless function update get-event -f src/app.py -d src/requirements.txt -r python3.7 --handler app.get_event
kubeless function update put-event -f src/app.py -d src/requirements.txt -r python3.7 --handler app.put_event
