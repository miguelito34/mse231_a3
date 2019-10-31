#########################################################################################################
## Author: Michael Spencer, Andrew (Foster) Docherty, Jorge Nam Song
## Project: MS&E 231 A3
## Script Purpose: Formats tweet data into a readable format for Vowpal Wabbit.
## Notes: Good features may include hour of day, minute of hour, number of capital letters...
#########################################################################################################

import sys
import datetime

for tweet in sys.stdin:
    
    # Parse tweet and format features