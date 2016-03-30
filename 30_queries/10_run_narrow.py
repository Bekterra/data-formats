import df_run_module
import ConfigParser

query1 = "SELECT COUNT(*) FROM {table_name}"

query2 = """SELECT COUNT(*) FROM {table_name} 
                        WHERE user_name NOT LIKE 'a%'
                        AND ip LIKE '%65%'
                        AND url NOT LIKE '%biz%'
                        AND referer LIKE '%com%'
                        AND agent LIKE '%Firefox%'"""

query3 = """SELECT COUNT(*) FROM {table_name}
                        WHERE ip NOT LIKE '%12%'
                        AND user_name LIKE 's%'
                        AND unix_time LIKE '%12%'
                        AND time LIKE '%2%'
                        AND url LIKE '%com%'
                        AND domain NOT LIKE '%org%'
                        AND page NOT LIKE '%privacy%'
                        AND port LIKE '%5%'
                        AND referer NOT LIKE '%biz%'
                        AND agent LIKE '%Safari%'"""

tables = ["narrow_text","narrow_sequencefile","narrow_avro","narrow_avro_snappy","narrow_parquet","narrow_orc"]
queries = {'q1':query1, 'q2':query2, 'q3':query3}
iterations = 10

def main():

    config = ConfigParser.ConfigParser()
    config.read("config.ini")

    db_conn_conf = df_run_module.config_section_map(config,"db_connection")

    df_run_module.execute_tests(db_conn_conf,queries,tables)

main()