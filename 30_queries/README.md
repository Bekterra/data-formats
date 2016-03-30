# Tests

We automate the testing for the data formats tables in two scripts:
- 10_run_narrow.py for the narrow database
- 20_run_wide.py for the wide database

Below are instructions on how to adjust and run the tests.

## Instructions

1. 	Install the python packages by running the following command:

	```
	sudo pip install -r requirements.txt
	```

2. 	Modify the `config.ini` file.

	The connection options are `hive` OR `impala`.

	Change the host to reflect the server that hosts hive or impala and use the appropiate port.

	The default hive port is `port=10000` and the default impala port is `port=21050 impala`.

	The number of iterations is the number of times you would like a query to be tested.

3. 	Configure your queries and tables in the `10_run_narrow.py` and `20_run_wide.py`.  

	*NOTE:* Remember that impala does not support ORC, therefore if you are running the tests in impala you need to modify the tables to remove tests from the orc table.

	Run narrow or wide tests by:
	`python 10_run_narrow.py > results_narrow.csv`
	`python 20_run_wide.py > results_wide.csv`

4.	Analyze your results with your favorite tool or with a simple python script to observe the means, for example:
	```
	import pandas as pd

	df = pd.read_csv('results_narrow.csv')
	df = df.drop(' iteration', 1)

	grouped = df.groupby(['query', ' table'])
	results = grouped.mean()
	results.to_csv('final_results_narrow.csv')
	```


