# Who Tweeted It

### Overview
Per the [MS&E 231 class website](https://5harad.com/mse231/#hw3): Some people have hypothesized that Donald Trump's tweets can be classified into those written by Trump himself and those written by his staff by looking at the device from which the tweet was sent, with Trump tweeting from an Android phone and his staff tweeting from an iPhone. We'll use stochastic gradient descent to see how well we can classify Trump's tweets based on the text and timing information alone (i.e., without knowledge of the device from which the tweet was sent.)

### Getting Set Up
1. Clone the GitHub repo into a directory of your choosing. You can name the directory whatever you'd like.
```
mkdir <your new folder>
cd <your new folder>
git init
git remote add origin git@github.com:miguelito34/mse231_a3.git
git pull origin master
```

The first time you go to push a file, you may receive this note:
```
fatal: The current branch master has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin master
```

If you see that, push using the instructions as above:
```
git push --set-upstream origin master
```

From now on, anytime you need to make changes, you should be able to push using:
```
git push
```

2. Get set up with Vowpal Wabbit using the directions [here](https://docs.google.com/presentation/d/1OTrzdWq1WIGCayPYzANng3hb9FDALtBmJS8hBwPA5To/edit#slide=id.g26dc8f6064_0_0) or, if using a remote server, by cloning the open-source project using the code below. Note that the make step may take several minutes. This process and examples are covered in the slides above as well as [here](https://vowpalwabbit.org/tutorials.html).
```
git clone --recursive https://github.com/VowpalWabbit/vowpal_wabbit.git
make
```

### Replicate Steps
Assuming the above steps went well, all you need to replicate the steps below are `training_data.tsv`, `test_data.tsv`, and `vw_format.py`. These steps should be re-run anytime changes to `vw_format.py` are made to ensure the model is being trained on the most up-to-date set of features.

#### If only feature-related changes have been made
1. Run the following shell script, which will execute the neccessary training, predicting, and evaluation steps as below, where <model_number> corresponds to the relevant model you wish to test.
```
bash model_creator.sh <model_number>
```

#### If you wish to run the steps manually
1. Format the raw data into a vw readable format with the decided upon features
```
cat training_data.tsv | python3 vw_format_m#.py > vw_training_data.txt
cat test_data.tsv | python3 vw_format_m#.py > vw_test_data.txt
```

2. Train the model on the vw-formatted training data. For example, with simple logistic loss:
```
vw -d vw_training_data.txt -f predictor.vw --loss_function logistic
```

3. Create predictions for the training and test data
```
vw -d vw_training_data.txt -t -i predictor.vw -p training_predictions.txt --link=logistic
vw -d vw_test_data.txt -t -i predictor.vw -p test_predictions.txt --link=logistic
```

4. Inspect variable information
```
vw-varinfo --loss_function logistic vw_training_data.txt
```

5. Variable importance
```
vw-varinfo --loss_function logistic vw_training_data.txt
```

6. Evaluate in model_evaluation.R
```
Rscript model_evaluation.R
```

### Data
Data was provided by the teaching staff and can be found [here](https://5harad.com/mse231/assets/trump_data.tsv). Data is formatted with three columns as below:
```
source time_posted text
```

### Approach and Strategy
In order to train our logistic model and determine who actually tweeted a given tweet, we parsed the data into the following features:

#### Model 1
Format file: vw_format_m1.py
Training command: vw -d vw_training_data.txt -f predictor.vw --loss_function logistic
Terminal command: bash model_creator.sh 1
Test accuracy: 0.8393574
Test AUC: 0.8830275
Description: Hour and minute are both continuous, checks num_caps, num_ats, num_hash, has_https, is_retweet

#### Model 2
Format file: vw_format_m2.py
Training command: vw -d vw_training_data.txt -f predictor.vw --loss_function logistic
Terminal command: bash model_creator.sh 2
Test accuracy: 
Test AUC: 
Description: same as model 1, except time is only hour indicators (e.g. hour_1, hour2, etc.)

#### Model 3
Format file: vw_format_m3.py
Training command: vw -d vw_training_data.txt -f predictor.vw --loss_function logistic
Terminal command: bash model_creator.sh 3
Test accuracy: 
Test AUC: 
Description: same as model 1, except time is represented by four "parts of day", e.g. "morning" 

### Results

### Conclusions and Limitations
