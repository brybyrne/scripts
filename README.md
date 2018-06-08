# scripts
This is a mix of expect and netconf scripts for interacting with devices.

# Ansible

# IOS

# Python

# Shell

Below you will find a collection of shell scripts that I use to automate common tasks typically done on my laptop. 

* Prep Env - The shell script in this directory will add a default gitignore and requirements file.
* clus18_bysh.sh - Shell script to automate positioning code repositories for Cisco Live 2018
* code_prompt.sh - Shell script to modify the bash shell prompt to minimize the prompt length.
  * When in a repo directory the prompt will color the name of the repo and current branch.
  * When in a repo the prompt will display the current state of the repo (up to date, changes to be committed, etc.
* default_prompt.sh - Shell script to set the shell prompt back to a default prompt.
  * When in a repo directory the prompt will color the name of the repo and current branch. 
  * When in a repo the prompt will display the current state of the repo (up to date, changes to be committed, etc.)
* install_python_centos.sh - This is a small shell script to automate updating Python on a new install of CentOS.
* suspend_vagrant.sh - Small shell script to stop all running vagrant images.
  