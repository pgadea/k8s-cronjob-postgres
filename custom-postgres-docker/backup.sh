#!/bin/bash

file_name=backup.pgsql
current_time=$(date "+%Y-%m-%d:%H")

PGPASSWORD="password" pg_dump -U postgres postgres > /home/backups/$current_time-$file_name

echo "Backup successful"
