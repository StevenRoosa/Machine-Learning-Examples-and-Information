import re
import sys
import subprocess

## Requires the 2 empty space bash files

the_file = str(sys.argv[1])

text = open(the_file, 'r')

list_transform_pattern = re.compile('^\s{1,4}\[\(\'.*?\)\]$', flags=re.MULTILINE)
target = re.compile('\',\s\'(.{0,16})\'\)', flags=re.MULTILINE)
hex_pattern = re.compile('[^[^0-9a-zA-Z]{1,4}\s{1,4}[a-f0-9]{10}\s{1,2}[\sa-f0-9]{47}\s(.{0,16})$', flags=re.MULTILINE)
record_separator_pattern = re.compile('^[0-9\.]{9,14}.*', flags=re.MULTILINE)
separator = re.compile('^<<@@@>>', flags=re.MULTILINE)
## cookie-send cookie names and records separated by "=" and ";" respectively
cookie_send = re.compile('^\s{1,4}Cookie:\s(.*)', flags=re.MULTILINE)
## separate cookie name and value pairs into separate lines per cookie
cookie_send_target1 = re.compile('([^;]*?;)')
## break off cookie names 
cookie_name = re.compile('^([^=]*?)=.*', flags=re.MULTILINE)
## break off cookie value 
cookie_value_long = re.compile('[^=]*=(.*)')
## constituent cookie values
cookie_sub_id = re.compile('([a-zA-Z0-9_\-=]*)[^a-zA-Z0-9_\-=]')

## Set-Cookie Regex:

## cookie-set cookies
cookie_set = re.compile('^\s{1,4}Set-Cookie:\s.*', flags=re.MULTILINE)
## cookie_set_name
cookie_set_name = re.compile('Set-Cookie:\s([^=]*?)=')
## long_cookie_set_value
long_cookie_set_value = re.compile('Set-Cookie:\s[^=]*?=([^;]*?);')
## constituent cookie values in composite set-cookies
cookie_set_sub_value = re.compile('([a-zA-Z0-9_\-=]*)[^a-zA-Z0-9_\-=]')



pre_output_file = open('pre_output_file.txt', 'w')

final_output_file = open('final_output_file.txt', 'w')

## Read lines from initial .txt file from sys arg into a list

input_file = []

for x in text:
    input_file.append(x)

## Insert record separators "<<@@@>>" before line with Request and IP address

for x in input_file:
    if record_separator_pattern.match(x): 
        p = ('<<@@@>>'+'\n'+x)
        print(p, file = pre_output_file)
    else:
        print(x, file = pre_output_file)

pre_output_file.close()

## convert JSON and Hex from pre_output_file

input_file = []

pre_output_file = open('pre_output_file.txt', 'r')

for x in pre_output_file:
    input_file.append(x)

hex_holder = []
for line in input_file:
    if list_transform_pattern.match(line):
        dump = line
        match = re.findall(target, dump)        
        g = ("\t<<Request_Hex>>" + (''.join(match)))
        print(g, file = final_output_file)
    elif hex_pattern.match(line):
        match = re.findall(hex_pattern, line)
        for z in match:
            hex_holder.append(z)
    elif separator.match(line):
        g = ("\t<<Response_Hex>>" + (''.join(hex_holder)))    
        print(g, file = final_output_file)
        print('<<@@@>>', file = final_output_file)
        hex_holder = []
    else:
        print(line, file = final_output_file)

final_output_file.close()

subprocess.call(['./EmptySpace.bash'])      

## cookie loop

file_dump = open('final_output_file.txt', 'r')

final_output = []

for line in file_dump:
    final_output.append(line)

OUTPUT_file = open('OUTPUT_file.txt', 'w')

for line in final_output:
    if cookie_send.match(line):
        dump = line
        match = re.findall(cookie_send_target1, dump)
        for x in match:
            long_cookie_string = x
            name_of_cookie = re.findall(cookie_name, long_cookie_string)
            c_name = (''.join(name_of_cookie))
            value_of_cookie = re.findall(cookie_value_long, long_cookie_string)            
            c_value = (''.join(value_of_cookie))
            print('\t<<Cookie_Name>>' + c_name + '<</Cookie_Name>>' + ' <<Cookie_Value>>' + c_value + '<</Cookie_Value>>', ' <<Cookie_Sub_Value_Flag>>0<</Cookie_Sub_Value_Flag>>', file = OUTPUT_file)
            sub_cookies = re.findall(cookie_sub_id, c_value)
            for q in sub_cookies:
                print('\t<<Cookie_Name>>' + c_name + '<</Cookie_Name>>' + ' <<Cookie_Value>>' + q + '<</Cookie_Value>>', ' <<Cookie_Sub_Value_Flag>>1<</Cookie_Sub_Value_Flag>>', file = OUTPUT_file)                
    elif cookie_set.match(line):
        match = re.findall(cookie_set_name, line)
        c_name = (''.join(match))
        match = re.findall(long_cookie_set_value, line)
        c_long_value = (''.join(match))         
        print('\t<<Cookie_Name>>' + c_name + '<</Cookie_Name>>' + ' <<Cookie_Value>>' + c_long_value + '<</Cookie_Value>>', ' <<Cookie_Sub_Value_Flag>>0<</Cookie_Sub_Value_Flag>>', file = OUTPUT_file)
        cookie_sub_value = re.findall(cookie_set_sub_value, c_long_value)
        for x in cookie_sub_value:
            print('\t<<Cookie_Name>>' + c_name + '<</Cookie_Name>>' + ' <<Cookie_Value>>' + x + '<</Cookie_Value>>', ' <<Cookie_Sub_Value_Flag>>1<</Cookie_Sub_Value_Flag>>', file = OUTPUT_file)      

    else:
        print(line, file = OUTPUT_file)

OUTPUT_file.close()

## NEED CLEAN UP !!!!

## eliminate the ";" at the end of full cookie strings - Use sed

## eliminate the "Cookie:"  that preceeds the very first cookie - USE sed

subprocess.call(['./OUTPUT_file_cleaner.bash'])


## sed -r 's/<<Cookie_Name>>\s\s\s\sCookie:/<<Cookie_Name>>/' OUTPUT_file.txt > test.txt

## sed -r 's/;<<\/Cookie_Value>>/<<Cookie_Value>>/' test.txt > testy.txt

print("OUTPUT_file.txt generated")    
  



          
