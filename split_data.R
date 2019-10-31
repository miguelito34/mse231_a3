#########################################################################################################
## Author: Michael Spencer, Andrew (Foster) Docherty, Jorge Nam Song
## Project: MS&E 231 A3
## Script Purpose: Downloads presidential tweet data and splits it into a training and a test set.
## Notes:
#########################################################################################################

## Setup

### Libraries
library(tidyverse)


### Parameters
path_data <- "https://5harad.com/mse231/assets/trump_data.tsv"

train_prc <- .8


### Load Data
data <- path_data %>% read_tsv


## Split Data

train_row_indexes <- sample(nrow(data), size = floor(train_prc*(nrow(data))))
                            
data[train_row_indexes,] %>% write_tsv(path = "training_data.tsv")

data[-train_row_indexes,] %>% write_tsv(path = "test_data.tsv")

