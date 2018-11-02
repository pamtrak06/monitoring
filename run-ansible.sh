#!/bin/bash

[ ! -d ansible/volumes ] && mkdir ansible/volumes
[ ! -d ansible/volumes/config ] && mkdir ansible/volumes/config

docker-compose -p ansible -f docker-compose.yml up --build -d
