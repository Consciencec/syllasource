#!/bin/sh
[[ -f saved_value ]] || echo 0 > saved_value
# variable n is incremented each script execution
n=$(< saved_value) 
echo $(( n + 1 )) > saved_value

cd .. && hugo
printf "\033[0;32mDeploying updates to Firebase...\033[0m\n" 
firebase deploy -m "firebase deployment #$n"
printf "\033[0;32mApplying updates to GitLab...\033[0m\n"

# GitLab push with incremented commit message
git add . && git commit -m "firebase deployment #$n"
git push -u origin master