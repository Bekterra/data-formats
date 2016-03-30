#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SQL_DIR=$SCRIPT_DIR/sql

source $SCRIPT_DIR/config.sh

exec_command() {
	cmd=$@
	echo $cmd
	output=`$cmd`
	error_code="$?"
	if [ "$error_code" != "0" ]
    then
       echo "$error_code"
       exit 1
    fi
}

copy_schemas_hdfs() {

	# Copy the narrow schema to the db location
	cmd="hdfs dfs -copyFromLocal schemas/narrow.avsc /user/hive/warehouse/strataca2016.db/"
	exec_command "$cmd"

	# Copy the wide schema to the db location
	cmd="hdfs dfs -copyFromLocal schemas/wide.avsc /user/hive/warehouse/strataca2016.db/"
	exec_command "$cmd"
}

create_tables() {
	
	# Create the database
	echo "Creating the database:"
	cmd="beeline -u $DB_URL -n $USERNAME -d $DRIVER_CLASS -f $SQL_DIR/create_database.sql --verbose=true"
	exec_command "$cmd"
	echo

	# Copy the avro schemas to the db folder
	echo "Coping schemas:"
	copy_schemas_hdfs
	echo

	# Create narrow table
	echo "Creating narrow table:"
	DATA="$DATAPATH/data_narrow.txt"
	cmd="beeline -u $DB_URL -n $USERNAME -d $DRIVER_CLASS -f $SQL_DIR/create_narrow_table.sql --hivevar datapath='$DATA' --verbose=true"
	exec_command "$cmd"
	echo

	# Create wide table
	echo "Creating wide table:"
	DATA="$DATAPATH/data_wide.txt"
	cmd="beeline -u $DB_URL -n $USERNAME -d $DRIVER_CLASS -f $SQL_DIR/create_wide_table.sql --hivevar datapath='$DATA' --verbose=true"
	exec_command "$cmd"
}

main() {
    create_tables
}

main
