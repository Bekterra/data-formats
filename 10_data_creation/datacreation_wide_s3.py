import sys, getopt, uuid
import smart_open
from faker import Factory
#----------------------------------------------------------------------
def main(argv):
    """"""
    delm = '|'
    num_rows = 2000
    s3_bucket = 's3://path/'
    try: 
        opts, args = getopt.getopt(argv,"r:s:",["rows=","s3bucket="])
    except getopt.GetoptError:
        print 'Usage: datacreation1.py -r "number_rows" -s "s3://path/"'
        sys.exit(2)
    for opt, arg in opts:
        if opt in("-r", "--rows" ):
            num_rows = arg
        elif opt in("-s", "--s3bucket"):
            s3_bucket = arg
        else:
            assert False, "unhandled option"
    fake = Factory.create()
    create_data(fake,delm,num_rows,s3_bucket)

def create_data(fake,delm,num_rows,s3_bucket):
    """"""
    filename = s3_bucket + str(uuid.uuid1()) + '.csv'

    with smart_open.smart_open(filename, 'wb') as fout:
        for i in range(int(num_rows)):
            record = ""
            firstRecord = True

            # Add some user data at the beginning of each record
            record += str(uuid.uuid1()) \
            + delm + fake.first_name() \
            + delm + fake.last_name() \
            + delm + fake.email() \
            + delm + fake.company() \
            + delm + fake.job() \
            + delm + fake.street_address() \
            + delm + fake.city() \
            + delm + fake.state_abbr() \
            + delm + fake.zipcode_plus4() \
            + delm + fake.url() \
            + delm + fake.phone_number() \
            + delm + fake.user_name() \

            # Repeats the same 3 columns 329 times = 987 cols + 13 initial = 1000
            for j in range(329):
                record += delm + fake.random_letter() \
                + delm + str(fake.random_int(min=0,max=1000)) \
                + delm + str(fake.boolean(chance_of_getting_true=50)) 

            fout.write(record + '\n')


if __name__ == "__main__":
    main(sys.argv[1:])
