import sys, getopt
from faker import Factory
#----------------------------------------------------------------------
def main(argv):
    """"""
    delm = '|'
    num_rows = 10000000
    try: 
        opts, args = getopt.getopt(argv,"r:",["rows="])
    except getopt.GetoptError:
        print 'Usage: datacreation1.py -r "number_rows"'
        sys.exit(2)
    for opt, arg in opts:
        if opt in("-r", "--rows" ):
            num_rows = arg
        else:
            assert False, "unhandled option"
    fake = Factory.create()
    create_data(fake,delm,num_rows)
 
def create_data(fake,delm,num_rows):
    """"""
    for i in range(int(num_rows)):
        print fake.ipv4() \
        + delm + fake.user_name() \
        + delm + str(fake.unix_time()) \
        + delm + str(fake.date_time_between(start_date="-70y", end_date="-20y")) \
        + delm + fake.url() \
        + delm + fake.domain_name() \
        + delm + fake.uri_page() \
        + delm + str(fake.random_int(min = 0, max = 9999)) \
        + delm + fake.url() \
        + delm + fake.user_agent() 
 
if __name__ == "__main__":
    main(sys.argv[1:])
