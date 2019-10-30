# Who Tweeted It

### Overview
Per the [MS&E 231 class website](https://5harad.com/mse231/#hw3): Some people have hypothesized that Donald Trump's tweets can be classified into those written by Trump himself and those written by his staff by looking at the device from which the tweet was sent, with Trump tweeting from an Android phone and his staff tweeting from an iPhone. We'll use stochastic gradient descent to see how well we can classify Trump's tweets based on the text and timing information alone (i.e., without knowledge of the device from which the tweet was sent.)

### Getting Set Up
1. Clone the GitHub repo into a directory of your choosing. You can use mkdir within bash to create a new directory. While this can be done on your local machine, it is recommended to use a remote server.
```
mkdir <your new directory>
cd <your new directory>
git init
git remote add origin git@github.com:miguelito34/mse231_a3.git
git pull origin master
(Enter your GitHub credentials if prompted)
```

2. Get set up with Vowpal Wabbit using the directions [here](https://docs.google.com/presentation/d/1OTrzdWq1WIGCayPYzANng3hb9FDALtBmJS8hBwPA5To/edit#slide=id.g26dc8f6064_0_0) or, if using a remote server, by cloning the open-source project using the code below. Note that the make step may take several minutes. This process and examples are covered in the slides above as well as [here](https://vowpalwabbit.org/tutorials.html).
```
git clone --recursive https://github.com/VowpalWabbit/vowpal_wabbit.git
make
```

### Data
Data was provided by the teaching staff and can be found [here](https://5harad.com/mse231/assets/trump_data.tsv). Data is formatted with three columns as below:
```
source time_posted text
```

### Approach and Strategy

### Results

### Conclusions and Limitations
