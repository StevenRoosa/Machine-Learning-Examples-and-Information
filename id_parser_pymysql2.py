import re
import pymysql
import subprocess
import sys
import time 
 

def PARSER(textfile, operating_system, app_name):

    ## insert Transform to implement json_holder and hex_holder
    source_file = str(textfile)
    file = open(textfile, 'r')
    file_dump = []
    for line in file:
        file_dump.append(line)

    request_pattern = re.compile('^[0-9\.]*\s(?:(?:GET)|(?:POST)|(?:HEAD)|(?:PUT)|(?:DELETE)|(?:CONNECT)|(?:OPTIONS)|(?:TRACE)).*', flags=re.MULTILINE)
    host_pattern = re.compile('^\s*Host:.*', flags=re.MULTILINE)
    referer_pattern = re.compile('^\s*Referer:.*', flags=re.MULTILINE)
    response_pattern = re.compile('^\s<<\s[0-9][0-9].*', flags=re.MULTILINE)
    record_separator = re.compile('^<<@@@>>.*', flags=re.MULTILINE)
    unique_id_pattern = re.compile('^\t<Unique_ID>.*', flags=re.MULTILINE)

    unique_id = ''
    request_response_flag = 0
    record = 1
    host = ''
    request = ''
    referer = ''

    ## y = 0 -- Request_Response_Flag Request = 0 Response = 1
    for line in file_dump:
        if request_pattern.match(line):
            pre_request = str(line)
            request = pre_request[0:48]
            continue
        elif host_pattern.match(line):
            pre_host = str(line)
            host = pre_host[0:48]
            continue
        elif referer_pattern.match(line):
            pre_referer = str(line)
            referer = pre_referer[0:48]
            continue
        elif unique_id_pattern.match(line):
            pre_unique_id = str(line)
            unique_id = pre_unique_id[12:100]
            time_stamp = str(time.time())
            STORE(record, source_file, app_name, host, request, referer, request_response_flag, unique_id, operating_system, time_stamp) 
            continue
        elif response_pattern.match(line):
            request_response_flag = 1
            continue    

        ## elif response (build in response separator: <<
        ##     y = 1
        ##     continue      
        


        elif record_separator.match(line):
            time_stamp = str(time.time())
            STORE(record, source_file, app_name, host, request, referer, request_response_flag, unique_id, operating_system, time_stamp)
            host = ''
            request = ''
            referer = ''
            brand1 = ''
            brand2 = ''
            unique_id = ''
            request_response_flag = 0
            record = record + 1 

def STORE(record, source_file, app_name, host, request, referer, request_response_flag, unique_id, operating_system, time_stamp):
    conn = pymysql.connect(host='127.0.0.1.', unix_socket='/tmp/mysql.sock', user='root', passwd='None', db='mysql', charset='utf8')
    cur = conn.cursor()
    cur.execute("USE mobile")
    cur.execute("INSERT INTO network_traffic (record, source_file, app_name, host, request, referer, request_response_flag, unique_id, operating_system, time_stamp) VALUES (\"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\")", (record, source_file, app_name, host, request, referer, request_response_flag, unique_id, operating_system, time_stamp))
    cur.connection.commit()

### End of functions

source_file = (str(sys.argv[1]))

operating_system = (str(sys.argv[2]))

app_name = (str(sys.argv[3]))

## subprocess.call(['./head2head_mitmdump_conversion.bash'])

## mitm_prelist = open('LIST_of_TRANSFORM_FILES.txt', 'r')

## mitm_list = []

##for x in mitm_prelist:
##    mitm_list.append(x)

##for y in mitm_prelist:


PARSER(source_file, operating_system, app_name)
