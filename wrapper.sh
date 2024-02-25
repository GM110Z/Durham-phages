#!/bin/bash 


FILELIST=$(cat input.txt)

for i in ${FILELIST}
   do
      python TheNewBrexScript.py ${i}.faa ${i}.gb
   done
