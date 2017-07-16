service mysql start
mysql -u root -e "CREATE DATABASE folha_limpa"

for sqlfile in $(ls hackfestdumps); do
    mysql -u root --password="" folha_limpa < hackfestdumps/$sqlfile
done
