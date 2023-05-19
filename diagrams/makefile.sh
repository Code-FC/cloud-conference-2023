#!/bin/bash

for python_file_name in $(find ./ -name *.py)
do
   echo $python_file_name
   python3 $python_file_name
done