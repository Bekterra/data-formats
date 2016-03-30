# Data Creation	

In order to run the data formats tests, we need some data.
We are generating two different types of datasets:

1. Narrow : 10 columns and 10,000,000 rows.
2. Wide: 1000 columns and 4,000,000 rows.

We also provide an script that can be used to generate and the wide dataset into an S3 bucket. The S3 script was used to generate data in parallel therefore the schema includes an UUID.
The S3 script also assumes that you have configured your environment with the appropiate AWS key to access S3.

## Requirements

- Python 2.7 or above to run the scrips.
- To install the python requirements you can run:
```
sudo pip install -r requirements.txt
```

OR install the individual components:

- fake-factory (Used to generate fake data) 
```
pip install fake-factory
```
- open_smart (Used to save files to S3):
```
pip install open_smart
```

Additionaly, if you want to monitor the progress of the file generation:
- pv (Pipe Viewer): To install depending on your OS:
```
Fedora: yum install pv
Debian-Ubuntu: apt-get install pv
Mac: brew install pv
```

## Usage

If you would like to modify the number of rows you can add the option -r to specify the new number of rows.

`python datacreation_narrow.py -r 10000000| pv -s 10000000 -l | hadoop fs -put - data_narrow.txt`

`python datacreation_wide.py -r 4000000| pv -s 4000000 -l | hadoop fs -put - data_wide.txt`


To generate the widedataset and save to S3:
`python datacreation_wide_s3.py -r 200000 -s s3://bucketname/`