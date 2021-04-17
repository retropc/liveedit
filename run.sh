#!/bin/bash
source venv/bin/activate

# if I complain about route-run make sure libpcre3-dev is installed before running venv

exec uwsgi --socket 127.0.0.1:4080 --master --file liveedit.py --route-run="fixpathinfo:"
