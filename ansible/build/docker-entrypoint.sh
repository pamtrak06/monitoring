#!/bin/bash
 
OS_NAME=$(cat /etc/os-release|grep NAME|cut -d '=' - f 2)
 
if [ "$DATABASE_TYPE" == "SQLITE" ]; then
  
  echo "[INFO]: local database Sqlite used"
  export ARA_DATABASE="sqlite:////tmp/ara.sqlite"
  
elif [ "$DATABASE_TYPE" == "MYSQL" ]; then
  
  echo "[INFO]: installing Mysql driver..."
  if [ "$OS_NAME" == "Debian" ] || [ "$OS_NAME" == "Ubuntu" ]; then
    # For Debian or Ubuntu
    apt-get install -y python-pymysql
  elif [ "$OS_NAME" == "Centos" ]; then
    # For RHEL derivatives
    yum install -y python-PyMySQL
  else
    # From pypi
    pip install pymysql
  fi
  
  echo "[INFO]: create ara database and it’s credentials..."
  python /docker-entrypoint/db_mysql.py
  
  echo "[INFO]: setup the database connection..."
  cmd="database = mysql+pymysql://$DATABASE_USER:$DATABASE_PASSWORD@$DATABASE_HOST/$DATABASE_NAME"
  echo "[DEBUG]: command - \"$cmd\""
  echo $cmd >> /etc/ansible/ansible.cfg
  export ARA_DATABASE=$(echo $cmd)
    
elif [ "$DATABASE_TYPE" == "POSTGRES" ]; then
  
  echo "[INFO]: installing Postgres driver..."
  if [ "$OS_NAME" == "Debian" ] || [ "$OS_NAME" == "Ubuntu" ]; then
    # For Debian or Ubuntu
    apt-get install -y python-psycopg2
  elif [ "$OS_NAME" == "Centos" ]; then
    # For RHEL derivatives
    yum install -y python-psycopg2
  else
    # From pypi
    pip install psycopg2
  fi
  
  echo "[INFO]: create ara database and it’s credentials..."
  python /docker-entrypoint/db_postgres.py
  
  echo "[INFO]: setup the database connection..."
  cmd="database = postgresql+psycopg2://$DATABASE_USER:$DATABASE_PASSWORD@$DATABASE_HOST:$DATABASE_PORT/$DATABASE_NAME"
  echo "[DEBUG]: command - \"$cmd\""
  echo $cmd >> /etc/ansible/ansible.cfg
  export ARA_DATABASE=$(echo $cmd)
  
else
  echo "[ERROR]: unknown database [$DATABASE_TYPE], exiting..."
  exit
fi

echo "[INFO]: running ara server..."
ara-manage runserver -h 0.0.0.0 -p 8080
 