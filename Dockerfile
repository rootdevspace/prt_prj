from python:slim-bullseye
RUN apt-get -y update \
&& apt-get -y install nginx \
&& apt-get install -y snmpd \
&& apt-get install -y snmp \
&& apt-get install -y libsnmp-dev \
&& apt-get install -y zabbix-agent \
&& pip install django
COPY printers /printers
WORKDIR /printers
CMD ["./manage.py", "runserver", "0.0.0.0:8080"]
