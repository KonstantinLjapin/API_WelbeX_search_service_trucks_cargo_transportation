#!/bin/bash
# need chmod +
sleep 10s
cd api_app/
uvicorn main:app --host 0.0.0.0;