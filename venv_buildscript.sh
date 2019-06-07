#!/usr/bin

# Build script for virtualenv

virtualenv --no-site-packages mhde
. mhde/bin/activate
pip3 install ipython3
pip3 install requests
pip3 install requests_oauthlib
pip3 install urllib3
deactivate
