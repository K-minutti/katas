#!/bin/bash

# Set the API endpoint
endpoint="http://localhost:8080/files/mem"

# Set the path to the zip file
zipFile="./resources/terraform.zip"

# Send the POST request with the zip file payload
curl -X POST -H "Content-Type: application/zip" --data-binary "@$zipFile" $endpoint -o "tf.zip"

