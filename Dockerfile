FROM mysql

ENV MYSQL_ALLOW_EMPTY_PASSWORD=true

COPY ./hackfestdumps/ /hackfestdumps
