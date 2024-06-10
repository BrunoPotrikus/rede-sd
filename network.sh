#!/bin/bash

# Nome das redes
REDE_SD="rede_sd"

# Criar redes Docker
docker network create --driver bridge $REDE_SD

# Exibir redes criadas
echo "Redes Docker criadas:"
docker network ls

# Conectar os contêineres às redes (exemplo de comando)
# docker network connect $REDE_SD <nome_do_conteiner>

echo "Redes configuradas com sucesso."