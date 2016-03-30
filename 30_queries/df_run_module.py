import sys
import time
import pyhs2
import impala.dbapi 

def config_section_map(config,section):
    config_dict = {}
    options = config.options(section)
    for option in options:
        try:
            config_dict[option] = config.get(section, option)
            if config_dict[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            config_dict[option] = None
    return config_dict

def get_connection(db_conn_conf, use_default_db):

    # Set up which database to use
    if use_default_db:
        db_name = "default"
    else:  # Set it to be the one specief in the config file
        db_name = db_conn_conf['database']

    # Create the connection
    if db_conn_conf['connector'] == 'hive':
        conn = pyhs2.connect(host=db_conn_conf['host'],
                 port=int(db_conn_conf['port']), 
                 authMechanism="PLAIN",
                 user=db_conn_conf['user'],
                 database=db_name)
        return conn
    elif db_conn_conf['connector'] == 'impala':
        conn = impala.dbapi.connect(host=db_conn_conf['host'],
                 port=db_conn_conf['port'], 
                 user=db_conn_conf['user'],
                 database=db_name)
        return conn
    else:
        print "Can't find connector"
        sys.exit(0)

def invalidate_metadata(db_conn_conf):
    conn = get_connection(db_conn_conf,True)
    cursor = conn.cursor()
    cursor.execute("invalidate metadata")
    cursor.close()
    conn.close()

def execute_tests(db_conn_conf, queries, tables):

    print "Starting queries with connector: " + db_conn_conf['connector']
    print("query, iteration, table, execution_time(seconds)")

    if db_conn_conf['connector'] == 'impala':
        invalidate_metadata(db_conn_conf)

    for q in queries:

        for i in xrange(int(db_conn_conf['iterations'])):

            conn = get_connection(db_conn_conf,False)
            cursor = conn.cursor()

            for table in tables:
                    query = queries[q].format(table_name=table)
                    start_time = time.time()
                    cursor.execute(query)
                    end_time = time.time() - start_time

                    print("%s,%d,%s,%s" % (q,i,table,end_time))

            cursor.close()
            conn.close()