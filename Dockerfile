FROM mysql

COPY ./hackfestdumps/ /hackfestdumps
COPY ./bootstrap_database.sh /bootstrap_database.sh

EXPOSE 3306
