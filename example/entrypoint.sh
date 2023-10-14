#!/bin/sh

echo ' '
echo 'Plugin Example:'
python -m plugin.main "{\"first\": \"foo\", \"last\": \"bar\"}" 

echo ' '
echo 'Plugin Metadata:'
cat /plugin/git-metadata.json