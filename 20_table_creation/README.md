# Table Creation

These scripts use hive to create the database we will be using, the initial tables that load the data, and finally re-writing the data in the different formats we will be testing:

1. Avro - deflate
2. Avro - snappy
2. Parquet - snappy
3. ORC - snappy
4. Sequence files - snappy
5. Text -snappy

## Instructions

First you need to set the config.sh file with the configurations pertinent to your system:

```
SERVER="localhost" <-- Server where hive can be run
USERNAME="user" <-- Username for hive
DATAPATH="/user/hadoop/" <-- Directory where the data generated was saved
```

The name of the new database that stores the data format tables is: `strataca2016`


To create the initial tables with the data we generated use:
```
sh 10_create_load_initial_tables.sh
```

To create all the different data formats tables with the inital data:
```
sh 20_write_format_tables.sh
```