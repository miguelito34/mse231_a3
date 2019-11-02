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

3. The first time you go to push a file, you may receive this note:
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

1. Format the raw data into a vw readable format with the decided upon features
```
cat training_data.tsv | python3 vw_format.py > vw_training_data.txt
```

2. Train the model on the training data
```
vw -d vw_training_data.txt -f predictor.vw --loss_function logistic
```

### Data
Data was provided by the teaching staff and can be found [here](https://5harad.com/mse231/assets/trump_data.tsv). Data is formatted with three columns as below:
```
source time_posted text
```

### Approach and Strategy
In order to train our logistic model and determine who actually tweeted a given tweet, we parsed the data into the following features:
```
hour - (continuous) 
minute of hour - (continuous)
number of capital letters used - (continuous)
number of @'s present in the tweet - (continuous)
number of hashtags present in the tweet - (continuous)
whether any type of media was included (i.e. a link, photo, or video) - (discrete)
whether the tweet was a retweet of something else - (discrete)
length of the tweet in characters - (continuous)
```

### Results

### Conclusions and Limitations
