#!/bin/sh
# File: /usr/local/bin/backup-sync.sh
## CLONE FILESYSTEM


SRC=/
DST=/home/nehe/backup/`hostname -s`
BLACKLIST=/home/nehe/etc/backup-blacklist.conf

# Sanity check
if [[ $EUID -ne 0 ]]; then
  echo "This script must be run as root"; exit 1
fi

logger -s "Starting filesystem sync"
rsync -aAXS --delete-after --exclude-from=$BLACKLIST $SRC $DST
logger -s "Finished filesystem sync"
