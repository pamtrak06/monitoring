FROM centos:centos7
MAINTAINER Janecek Jean-Philippe <pamtrak06@gmail.com>

# Install Ansible and ara
RUN yum clean all && \
    yum -y install epel-release && \
    yum -y install PyYAML python-jinja2 python-httplib2 python-keyczar python-paramiko python-setuptools git python-pip \
                   gcc python-devel libffi-devel openssl-devel redhat-rpm-config
RUN mkdir /etc/ansible/
RUN echo -e '[local]\nlocalhost' > /etc/ansible/hosts

RUN pip install ansible ara
RUN python -m ara.setup.ansible | tee /etc/ansible/ansible.cfg

# Local sqlite (SQLITE, default) or Mysql (MYSQL) or Postgres (POSTGRES)
ARG DATABASE_TYPE=SQLITE
ENV DATABASE_TYPE=

ENV DATABASE_NAME=ara
ENV DATABASE_USER=
ENV DATABASE_PASSWORD=
ENV DATABASE_HOST=
ENV DATABASE_PORT=

ADD scripts /docker-entrypoint
RUN chmod a+x /docker-entrypoint/*.py

ADD docker-entrypoint.sh /
RUN chmod a+x /docker-entrypoint.sh
ENTRYPOINT [ "/docker-entrypoint.sh" ]