#!/bin/bash

sed -i -r 's/<<Cookie_Name>>\s\s\s\sCookie:/<<Cookie_Name>>/' OUTPUT_file.txt

sed -i -r 's/;<<\/Cookie_Value>>/<<Cookie_Value>>/' OUTPUT_file.txt

