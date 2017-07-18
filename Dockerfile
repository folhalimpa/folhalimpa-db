FROM mysql

ENV MYSQL_ALLOW_EMPTY_PASSWORD=true

COPY ./hackfestdumps/ /hackfestdumps
COPY ./bootstrap_database.sh /bootstrap_database.sh

EXPOSE 3306

RUN ./bootstrap_database.sh