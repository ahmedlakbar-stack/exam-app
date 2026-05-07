#!/bin/bash

docker build -t exam-app .

docker run -d -p 8080:8080 exam-app
