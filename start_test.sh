#!/bin/bash
# need chmod +
sudo docker compose up;
sudo docker stop $(sudo docker ps -a -q);
sudo docker rm $(sudo docker ps -a -q);
sudo docker rmi $(sudo docker images --format="{{.Repository}} {{.ID}}" |
                  grep "^api_welbex_search_service_trucks_cargo_transportation-api_fast_api" | cut -d' ' -f2);