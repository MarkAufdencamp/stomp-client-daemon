#!/bin/bash
echo "------------ Starting provisioning script -------------------------------------"
# We'll be running as the default 'vagrant' user
# The 'vagrant' user has sudo privileges via /etc/sudoers.d/vagrant
#
# All other user context will need to be encased in either:
# 	sudo COMMAND (root)
# -or-
# 	sudo su - USERRNAME -c "COMMAND"
#
# This is specifically utilized in this script to accommodate ActiveMQ and StompClientDaemon
# running in a defined user context of activemq and stompclientd respectively
 
# include config variables
. /vagrant/devops/config

sudo apt-get update > /dev/null 2>&1 && sudo apt-get -y upgrade > /dev/null 2>&1

echo "------------ NTP (time sync) --------------------------------------------------"
sudo apt-get install -y ntp
sudo cp /vagrant/devops/ntp-skeleton.conf /etc/ntp.conf
sudo /etc/init.d/ntp restart

echo "------------ Git & Node -------------------------------------------------------"
sudo apt-get install -y git nodejs
sudo update-alternatives --install /usr/bin/node nodejs /usr/bin/nodejs 100
sudo apt-get install -y npm

echo "------------ Install MySQL ------------------------------------------------------------"
sudo apt-get install -y libmysqlclient-dev
echo "mysql-server mysql-server/root_password password password" | sudo debconf-set-selections
echo "mysql-server mysql-server/root_password_again password password" | sudo debconf-set-selections
sudo apt-get install -y mysql-server-5.5
mysql -uroot -ppassword -e "CREATE DATABASE host_mgmt_dev"
mysql -uroot -ppassword -e "CREATE DATABASE host_mgmt_test"
mysql -uroot -ppassword -e "grant all privileges on host_mgmt_dev.* to 'host_mgmt'@'localhost' identified by 'password'"
mysql -uroot -ppassword -e "grant all privileges on host_mgmt_test.* to 'host_mgmt'@'localhost' identified by 'password'"
mysql -uroot -ppassword -e "ALTER DATABASE host_mgmt_dev DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;"
mysql -uroot -ppassword -e "ALTER DATABASE host_mgmt_test DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;"
echo "------------ MySQL Installed ------------------------------------------------------------"

echo "------------ /opt ------------------------------------------------------"
sudo mkdir /opt

echo "------------ JRE/JVM ------------------------------------------------------"
sudo apt-get install -y default-jre default-jdk
sudo update-alternatives --config java



echo "------------ Install ActiveMQ ------------------------------------------------------"
echo "------------ http://archive.apache.org/dist/activemq/5.14.3/apache-activemq-5.14.3-bin.tar.gz -------"
# Note: http://servicebus.blogspot.com/2011/02/installing-apache-active-mq-on-ubuntu.html
echo "Downloading and extracting ActiveMQ from the Apache Project" 
sudo wget -q http://archive.apache.org/dist/activemq/5.14.3/apache-activemq-5.14.3-bin.tar.gz
sudo tar -xzvf apache-activemq-5.14.3-bin.tar.gz
sudo mv apache-activemq-5.14.3 /opt
sudo ln -sf /opt/apache-activemq-5.14.3 /opt/activemq
echo "Adding activemq user account and setting directory ownership"
sudo adduser -system activemq
# TODO: addgrp ?
sudo chown -R activemq: /opt/activemq/
echo "Configuring Upsart sysem init scripts"
sudo ln -sf /opt/activemq/bin/activemq /etc/init.d/
sudo update-rc.d activemq defaults
# Note: http://activemq.apache.org/unix-shell-script.html
# Note difference in existence of bin/env from activemq setup /etc/defaults in versions >= 5.11.0
sudo /etc/init.d/activemq setup /etc/default/activemq
echo "Configuring ActiveMQ"
# TODO: Modify /opt/activemq/bin/env - ACTIVEMQ_USER="activemq"
#sudo cp /vagrant/devops/activemq-skeleton.xml /opt/activemq-5.14.3/conf/activemq-host-mgmt.xml
echo "Starting ActiveMQ Service"
sudo service activemq start
echo "------------ ActiveMQ Installed ------------------------------------------------------"





echo "------------ Install Stomp Client Daemon ------------------------------------------------------"
echo "------------ https://github.com/MarkAufdencamp/stomp-client-daemon.git ------------------------"
echo "------------ Stomp Client Daemon User Account --------------------------------"
echo "Adding stompclientd user account"
sudo useradd stompclientd -m -s /bin/bash

echo "------------ Stomp Client Daemon Source --------------------------------"
sudo git clone https://github.com/MarkAufdencamp/stomp-client-daemon.git /opt/stomp-client-daemon
sudo chown -R stompclientd:stompclientd /opt/stomp-client-daemon

echo "------------ Python/PIP ------------------------------------------------------"
sudo apt-get install -y python-pip
# bzip2, readline, sqlite3 needed to compile python
sudo apt-get install -y libbz2-dev
sudo apt-get install -y libreadline-dev
sudo apt-get install -y libsqlite3-dev
sudo pip install virtualenv

echo "------------ Install pyenv ---------------------------------"
#https://github.com/pyenv/pyenv
sudo su - stompclientd -c 'git clone https://github.com/pyenv/pyenv.git ~/.pyenv'
sudo su - stompclientd -c "echo export PYENV_ROOT='\$HOME/.pyenv' >> ~/.bash_profile"
sudo su - stompclientd -c "echo export PATH='\$PYENV_ROOT/bin:\$PATH' >> ~/.bash_profile"
sudo su - stompclientd -c "echo 'eval \"\$(pyenv init -)\"' >> ~/.bash_profile"

echo "------------ Install pyenv-virtualenv --------------------------------------------------"
#https://github.com/pyenv/pyenv-virtualenv
sudo su - stompclientd -c 'git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv'
sudo su - stompclientd -c "echo 'eval \"\$(pyenv virtualenv-init -)\"' >> ~/.bash_profile"

echo "------------ Install python 3.6.3 -----------------------------------------"
sudo su - stompclientd -c "cd /opt/stomp-client-daemon && pyenv install 3.6.3"
sudo su - stompclientd -c "cd /opt/stomp-client-daemon && pyenv rehash"
sudo su - stompclientd -c "cd /opt/stomp-client-daemon && pyenv local 3.6.3"

echo "------------ Stomp Client Daemon pyenv/pip install------------------------------------------------------"
sudo su - stompclientd -c "cd /opt/stomp-client-daemon && pyenv virtualenv stompclientd"
sudo su - stompclientd -c "cd /opt/stomp-client-daemon && pyenv local stompclientd"
sudo su - stompclientd -c "cd /opt/stomp-client-daemon && pip install --upgrade setuptools"
sudo su - stompclientd -c "cd /opt/stomp-client-daemon && pip install -r requirements.txt"
sudo printf "127.0.0.1\tdev-msg-broker.tiwaz.cloud\tdev-msg-broker\n" >> /etc/hosts
sudo su - stompclientd -c "cd /opt/stomp-client-daemon && cp dev-cntlr-srvr-config.json config.json"
# Tech Debt - Need init script - /opt/stomp-client-daemon/stomp_daemon.py start/stop/status/restart
# Tech Debt - Need StompClientDaemon puppet class for deployment on dev-inet-srvr-01.tiwaz.cloud and dev-inet-srvr-02.tiwaz.cloud
echo "------------ Stomp Client Daemon Installed ------------------------------------------------------"










echo "------------ Install Puppet ---------------------------------------------"
sudo apt-get install -y puppetmaster puppetmaster-common subversion
echo "------------ Puppet Installed ---------------------------------------------"

echo "------------ Install Puppet Scripts---------------------------------------------"
echo "------------ https://iluviya.net/svn/iluviya.net/puppet-manifests/trunk ---------------------------------------------"
echo "------------ https://iluviya.net/svn/iluviya.net/puppet-files/trunk ---------------------------------------------"
sudo svn co https://iluviya.net/svn/iluviya.net/puppet-manifests/trunk /etc/puppet/manifests --username maaufden --password jester007
sudo svn co https://iluviya.net/svn/iluviya.net/puppet-files/trunk /etc/puppet/files --username maaufden --password jester007
echo "------------ Puppetmaster Configuration Files---------------------------------------------"
echo "------------ /etc/puppet/puppet.conf ---------------------------------------------"
sudo printf "127.0.0.1\tdev-cntlr-srvr.tiwaz.cloud\tdev-cntlr-srvr\n" >> /etc/hosts
sudo printf "[master]\n" >> /etc/puppet/puppet.conf
sudo printf "certname=dev-cntlr-srvr.tiwaz.cloud\n" >> /etc/puppet/puppet.conf
echo "------------ /etc/puppet/fileserver.conf ---------------------------------------------"
sudo cp /vagrant/devops/puppet-fileserver-skeleton.conf /etc/puppet/fileserver.conf
echo "------------ /etc/puppet/manifests/nodes.pp ---------------------------------------------"


sudo service puppetmaster restart
echo "------------ Puppet Installed ---------------------------------------------"


echo "------------ Install vhostmgmt Scripts ---------------------------------------------"
echo "------------ https://iluviya.net/svn/iluviya.net/iluviya.net/vhost-scripts - svn ---------------"
sudo svn co https://iluviya.net/svn/iluviya.net/iluviya.net/vhost-scripts /etc/vhost-mgmt-scripts  --username maaufden --password jester007
echo "------------ vhostmgmt Scripts Installed ---------------------------------------------"