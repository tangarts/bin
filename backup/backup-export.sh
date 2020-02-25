#!/bin/sh
# File: /usr/local/bin/backup-export.sh
EXTERNAL_DRIVE=/mnt
ARCHIVE_FILE="$1"

if [ -z "$1" ]; then
  echo "Please specify the full path of the archive file."
fi

if mount | grep $EXTERNAL_DRIVE > /dev/null; then
  logger -s "Exporting backup to external drive..."
  cp $ARCHIVE_FILE $EXTERNAL_DRIVE
  logger -s "Backup export complete."
else
  logger -s "External drive not mounted. Exiting..."
fi
