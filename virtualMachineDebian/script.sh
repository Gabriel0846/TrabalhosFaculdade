#1/bin/bash

echo "SISTEMA:"
lsb_release -d 2>/dev/null
echo "----------------------"
echo "Usuário corrente: $USER"
echo "Processador:"
lscpu | grep "Model name"
echo "Memoria total:"
grep MemTotal /proc/meminfo

exit 0