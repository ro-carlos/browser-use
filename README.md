# browser-use

# Upgrade de Python3.10 a Python3.11

 Check python version use python and python3
 The first comman will Not show version info.
 The second one show 3.10 as version as it is provided by ubuntu as default
python --version
python3 --version

 Add additional repository to download python 3.11
sudo add-apt-repository ppa:deadsnakes/ppa

 This might take more than few minutes
sudo apt update
sudo apt upgrade

 Install python 3.11
sudo apt-get install python3.11

 python3 shows 3.10 and python3.11 shows 3.11 as version
python3 --version
python3.11 --version

sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 2

 EXECUTE THE COMMAND AND PRESS 2 THEN ENTER
sudo update-alternatives --config python3


 In case if you have problem with open terminal later when you restarted 
 Ubuntu (due to command update-alternatives before), please
 open PyCharm or VS Code IDE, then open terminal from there
 cd /usr/bin
 sudo cp gnome-terminal gnome-terminal-backup
 sudo cp gnome-terminal.real gnome-terminal

 3.11 will be shown as version
python3 --version

sudo apt install python-is-python3

 3.11 will be shown as version
python --version
