#!/bin/bash

if [ ! -f ./test_ivan.txt ]
then
    touch test_ivan.txt
fi
echo run >> test_ivan.txt