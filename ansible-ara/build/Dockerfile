FROM centos:centos7

# Install Ansible
RUN yum clean all && \
    yum -y install epel-release && \
    yum -y install gcc python-devel libffi-devel openssl-devel redhat-rpm-config
RUN pip install ara

# Install ara



ENTRYPOINT [ "./docker-entrypoint.sh" ]