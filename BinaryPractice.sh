#!/bin/bash

# Generating the 8 digit binary number

while :
do
  a=$(( $RANDOM % 2 ))
  b=$(( $RANDOM % 2 ))
  c=$(( $RANDOM % 2 ))
  d=$(( $RANDOM % 2 ))
  e=$(( $RANDOM % 2 ))
  f=$(( $RANDOM % 2 ))
  g=$(( $RANDOM % 2 ))
  h=$(( $RANDOM % 2 ))

#converting the binary characters to a numeric
  aa=$((a*128))
  bb=$((b*64))
  cc=$((c*32))
  dd=$((d*16))
  ee=$((e*8))
  ff=$((f*4))
  gg=$((g*2))
  hh=$((h*1))

  binary=$a$b$c$d$e$f$g$h
  number=$((aa+bb+cc+dd+ee+ff+gg+hh))


  echo "Please enter the decimal number associated with $binary"
  read guess

  if [ $guess -ne $number ] ; then
    echo "Incorrect"
    break
  else
    echo "Correct"
    echo " "
  fi

done
