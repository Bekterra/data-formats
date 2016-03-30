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

write_dataformats() {
	
	# Create formats table for narrow table
	cmd="beeline -u $DB_URL -d $DRIVER_CLASS -n $USERNAME -f $SQL_DIR/create_formats.sql --hivevar table=narrow --hivevar avroschema='hdfs:///user/hive/warehouse/strataca2016.db/narrow.avsc' --verbose=true"
	exec_command "$cmd"

	# create formats table for wide table
	cmd="beeline -u $DB_URL -d $DRIVER_CLASS -n $USERNAME -f $SQL_DIR/create_formats.sql --hivevar table=wide --hivevar avroschema='hdfs:///user/hive/warehouse/strataca2016.db/wide.avsc' --verbose=true"
	exec_command "$cmd"
}

main() {
	write_dataformats
}

main