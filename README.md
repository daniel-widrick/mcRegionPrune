Simple Script to list region files outside a given block radius. The script may be useful in identifying region files which were accidentally generated.

   Usage:

    python3 mcRegionPrune.py -p /home/mc/myWorld/region -b 7000

To remove region files, ** FIRST BACKUP YOUR WORLD ** Then run:

    python3 mcRegionPrune.py -p /home/mc/myWorld/region -b 7000 | xargs /usr/bin/rm

USE WITH EXTREME CAUTION.
