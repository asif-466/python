#!/bin/bash

cd /home/asif/python || { echo "Failed to change directory"; exit 1; }

status_output=$(git status --porcelain|wc -l)

if [[ $status_output -eq 0 ]]
	then	
	git pull origin main > /dev/null 2>&1
	echo "git pull succesfull"

elif [[ $status_output -ge 1 ]]
	then
	git add . > /dev/null 2>&1
	git commit -m "change in repo" > /dev/null 2>&1
	git push origin main > /dev/null 2>&1
	echo "git push succesfull"
fi

