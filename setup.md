# Project Setup - Contents

0. [Laptop Setup](#laptop-setup)
1. [Getting the Repository](#getting-the-repository)
2. [Backend Setup](#backend-setup)
3. [Frontend Setup](#frontend-setup)

## Laptop Setup

These sub-projects can be run on either a VMware or it can be locally setup. The base operating system required here is Linux, which can be accessed via the Windows Subsystem for Linux on a Windows Machine.

#### Linux subsystem for Windows

```
Enable feature in windows settings
Go to Windows store and get Ubuntu.
Install and set up local user + password – NOTE IT DOWN
To open the ubuntu. Either search for “ubuntu” or “wsl” in start menu.
Wsl – Windows Subsytem For Linux (Ubuntu)
To verify installed version:
lsb_release -a

Update Linux
sudo apt update
sudo apt upgrade
sudo apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev
```

#### Python, Pip & Virtualenv

```
python3 –-version (should be 3.6 or greater)
sudo apt install python3-pip
pip3 --version
pip3 install virtualenv

Refer to https://stackoverflow.com/questions/49943410/pip-ssl-error-on-windows
in case of errors.
USE THIS IN CASE OF ERROR > pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org <PACKAGE>
```

#### Export DISPLAY to your local machine

```
echo "export DISPLAY=localhost:0.0" >> ~/.bashrc
source ~/.bashrc
Install and launch Xserver (Must ALWAYS be running before starting Pgadmin, pycharm etc)
On Windows desktop, download and install VcXsrv server
Launch it and choose preferences – use multiple windows as we are not installing a Linux Desktop environment (a very time consuming and failure prone operation)
sudo apt install xterm
```

#### Postgres

```
m. sudo apt install postgresql postgresql-contrib
> sudo apt-get install postgresql
> sudo apt-get install python-psycopg2
> sudo apt-get install libpq-dev
Refer to https://stackoverflow.com/questions/28253681/you-need-to-install-postgresql-server-dev-x-y-for-building-a-server-side-extensi

start server: sudo /etc/init.d/postgresql restart
validate that the server is running with: sudo –u postgres psql; you should see a psql prompt; quit the postgres shell with \q
set the password for the postgres user with the \password postgres command at the postgres command prompt
install pgadmin3: sudo apt install pgadmin3
launch pgadmin3: pgadmin3 (Requires VcScrv (XLaunch) to be running in the background)
Connect to postgres server.
New Server Registration>
Name – localhost
Host – localhost
Port – 5432 Or to know the port use command – “service postgresql status”
Username, password – postgres, postgres
*If you don’t remember the username, password or it is not set. Use below commands.
Postgres Reference Commands
	1. User Commands
		$ sudo -u postgres createuser postgres
		$ sudo -u postgres psql
		$ alter user postgres with password 'postgres' (Refer to https://stackoverflow.com/questions/24917832/how-connect-postgres-to-localhost-server-using-pgadmin-on-ubuntu)
		psql=# alter user postgres with encrypted password postgres;

	2. Create New DB
		$ sudo -u postgres psql
		psql=# create database django-angular-skeleton;
```

#### Pycharm

```
Download pycharm using the windows browser (download using the browser on the Linux subsystem is unlikely to succeed). This is available at: https://www.jetbrains.com/pycharm/download/?#section=linux
From your Ubuntu prompt, copy the downloaded file to the home directory
> cp /mnt/c/Users/<user-name>/Downloads/pycharm-community-2019.2.3.tar.gz /home/<user-name/
> format of cp is – “cp source-file destination-file”

NOTE – this is now copied to the home/username folder
Unzip pycharm:
tar –xvf pycharm-community-2019.2.3.tar.gz
/home/usernamepycharm-community-2019.2.3/bin/pycharm.sh &
```

#### Git

```
(Can be installed either in windows or wsl)

Install Git for windows. Google it. Will show GIT Bash installed.
OR
sudo apt install git #(on wsl)

git --version
Generate ssh public key to access this repository.
Enter ‘ls -al ~/.ssh’ to see if existing SSH keys are present: If not, use the below command to generate new ones.
ssh-keygen -t rsa -b 4096 -C [your email address]
gets saved in /home/username/.ssh/id_rsa
Add your public key to Git Local and to your GIT settings>SSH&GPG Keys.
```

## Getting the Repository

```
Open Git Terminal.
	LOCAL
	# start the ssh-agent in the background
	eval $(ssh-agent -s)
	> Agent pid 59566
	# Add key to ssh-agent
	$ ssh-add ~/.ssh/id_rsa

	> git clone <INSERT GIT SSH CLONE URL HERE>
```

## Backend Setup

#### Install dependencies On the Pycharm/ubuntu Terminal console

```
cd django-angular-skeleton/django-angular-skeleton/venv_django-angular-skeleton/
virtualenv –python=python3 .
source bin/activate
cd ./../ (get back to django-angular-skeleton directory)
pip install –r backend/requirements.txt
```

#### On the ubuntu terminal

```
sudo service postgresql start
pgadmin3 &
Double click on localhost and connect to it. The DB django-angular-skeleton would be present there.
```

#### Open Pycharm

```
/home/username/pycharm-community-2019.2.3/bin/pycharm.sh &
File> Open> choose folder django-angular-skeleton
Attach in same window (this option will be provided when other repo’s are opened, this will come later while setting up core, common etc.)
File
	> Settings
	> Python Interpreter
	> Click on Hexagon Symbol
	> Show All
	> Click on + sign on the right vertical toolbar
	> Under Virtualenv Environment
	> Existing Environment
	> Choose Interpreter by selecting the path
	/mnt/……../django-angular-skeleton/venv_django-angular-skeleton/bin/python3.6

Rename the venv – Give it an appropriate name like django-angular-skeleton-venv.
Apply, Save etc.
pycharm will begin indexing the folders.
```

### Run these commands, with the venv activated.

Refer [DB Migrations Command File](./db-migration-commands.md) to bring the latest changes to your local DB.

#### Frontend - Open the terminal which can access NPM (Complete [Frontend Setup](#frontend-setup) first.

```
cd /django-angular-skeleton/django-angular-skeleton/frontend/
npm install
ng build
```

Now go to http://127.0.0.1:8000 to start the project.
