#!/bin/bash

for file in $(cat $1)
   do
      esearch -db assembly -query ${file} | elink -target taxonomy | efetch -format native -mode xml | grep ScientificName | awk -F ">|<" 'BEGIN{ORS=", ";}{print $3;}'>>${1}.tsv
      printf "\n" >> ${1}.tsv
   done

