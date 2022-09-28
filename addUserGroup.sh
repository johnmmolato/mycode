#!/bin/bash

# Prompting the user for the username that they want to provide and adding it to user
# In addition, the prompt also asks the user where the new user what groups it belongs to

echo "Please provide the username you want to add?"
   
read USER

echo "Please provide provide the group name you want to add?"

read GROUP

# Adding the new user and adding to group
sudo useradd $USER
sudo groupadd $GROUP
sudo usermod -aG $GROUP $USER   
