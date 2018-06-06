#!/bin/bash
N=${1:-10}

a=0
b=1

echo "The Fibonacci series is : "

for (( i=0; i<N; i++ ))
do
    echo -n "$a "
    sleep 10
    fn=$((a + b))
    a=$b
    b=$fn
done
