#!/bin/bash

docker build -t exam-app .

docker run -d -p 5050:5050 exam-app
