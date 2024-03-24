#!/bin/bash
# need chmod +
sleep 10s;

uvicorn api_app.main:app --host 0.0.0.0;