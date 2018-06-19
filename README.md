## Prerequisites and execution of the project files:
1. Install [Python3](https://www.python.org/)
1. Install [Vagrant](https://www.vagrantup.com/)
1. Install [VirtualBox](https://www.virtualbox.org/)
1. Download the vagrant setup files from [Udacity's Github](https://github.com/udacity/fullstack-nanodegree-vm)
These files configure the virtual machine and install all the tools needed to run this project.
1. Download the database setup: [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
1. Unzip the data to get the newsdata.sql file.
1. Put the newsdata.sql file into the vagrant directory
1. Download this project: [log analysis](https://github.com/eatie/log-analysis)
1. Upzip as needed and copy all files into the vagrant directory into a folder called log_analysis

## Start the Virtual Machine:
1. Open Terminal and navigate to the project folders we setup above.
1. cd into the vagrant directory
1. Run ``` vagrant up ``` to build the VM for the first time.
1. Once it is built, run ``` vagrant ssh ``` to connect.
1. cd into the correct project directory: ``` cd /vagrant/log_analysis ```

## Load the data into the database:
1. Load the data using the following command: ``` psql -d news -f newsdata.sql ```

## Run The Project Already!
1. You should already have vagrant up and be connected to it.
1. If you aren't already, cd into the correct project directory: ``` cd /vagrant/log_analysis ```
1. Run ``` python loganalysis.py ```
