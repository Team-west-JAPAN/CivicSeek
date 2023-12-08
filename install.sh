#!/bin/bash
# Author : Yoshiyuki Kurose
# This is install bash shell script

timeout_max=15

echo "start(._.)b!" # print start message 

# install required system packages
sudo apt update && sudo apt upgrade -y # update your system
sudo apt install python3 git python3-venv python3-pip # install required packages
# download git repository
timeout $timeout_max git clone https://github.com/Team-west-JAPAN/Backend.git \
    || timeout $timeout_max git clone git@github.com:Team-west-JAPAN/Backend.git \
    || echo "Maybe you're messing with your proxy settings...(._.)b"

# configure your environment
cd Backend # move to Backend dir
python3 -m venv venv # create virtual environment for python
source ./venv/bin/activate # activate venv
pip install -r requirements.txt # install required packages
python3 ./manage.py migrate # migrate DB

echo "done(._.)b!..." # print end message
