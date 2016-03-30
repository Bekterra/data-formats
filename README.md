# Data Formats

How do you choose the best data format for your project/environment?

We share a general approach here: <http://www.svds.com/how-to-choose-a-data-format> and share more information about the data formats and tests we ran in different environemnts here: <http://www.svds.com/dataformats> 

Here you can find the code used to run the tests.
We split into thre steps:
1. Data Creation - creates the fake data to use in tests
2. Table Creation - creates the tables stored in text, sequence, avro, orc, and parquet.
3. Queries - tests for reading data from tables

## Prerequisites

* Hadoop environment needed to run, in particular CDH for Impala examples. Tested under CDH 5.1.2.
* Python 2.7 or above.
* Pip or easyinstall to install the libraries.
