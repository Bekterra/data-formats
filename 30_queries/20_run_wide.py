import df_run_module
import ConfigParser

query1 = "SELECT COUNT(*) FROM {table_name}"

query2 = """SELECT COUNT(*) FROM {table_name}
                        WHERE first_name NOT LIKE 'a%'
                        AND phone_number LIKE '%5%'
                        AND letter_43 NOT LIKE 'b'
                        AND number_102 > 60
                        AND bool_200 = false""";

query3 = """SELECT COUNT(*) FROM {table_name}
                        WHERE last_name NOT LIKE 'w%'
                        AND email LIKE '%com%'
                        AND letter_77 LIKE 'r'
                        AND number_106 < 300
                        AND bool_143 = true
                        AND letter_252 NOT LIKE 'o'
                        AND number_311 > 400
                        AND bool_323 = false
                        AND letter_326 NOT LIKE 's'
                        AND number_326 < 200"""

query4 = """SELECT COUNT(*) FROM {table_name}
                        WHERE url NOT LIKE '%biz%'
                        AND user_name LIKE 't%'
                        AND letter_93 LIKE 'q'
                        AND number_102 < 350
                        AND bool_117 = true
                        AND letter_138 NOT LIKE 'd'
                        AND number_174 > 460
                        AND bool_215 = false
                        AND letter_238 NOT LIKE 'i'
                        AND number_269 < 250
                        AND user_agent NOT LIKE '%Chrome%'
                        AND zipcode_plus4  LIKE '%44%'
                        AND letter_247 LIKE 'j'
                        AND number_253 > 400
                        AND bool_256 = true
                        AND letter_314 NOT LIKE 'f'
                        AND number_316 < 110
                        AND bool_319 = false
                        AND letter_320 NOT LIKE 'c'
                        AND number_320 > 200"""

tables = ["wide_text","wide_sequencefile","wide_avro","wide_avro_snappy","wide_parquet","wide_orc"]
queries = {'q1':query1, 'q2':query2, 'q3':query3, 'q4':query4}
iterations = 10

def main():

    config = ConfigParser.ConfigParser()
    config.read("config.ini")

    db_conn_conf = df_run_module.config_section_map(config,"db_connection")

    df_run_module.execute_tests(db_conn_conf,queries,tables)

main()