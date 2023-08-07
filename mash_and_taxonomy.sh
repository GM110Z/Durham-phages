#!/bin/bash

VAR=$(ls *.fasta)

for file in ${VAR}
   do
      mash sketch -o ${file}sketch ${file}
      mash dist  ${file}sketch.msh refseq.genomes.k21s1000.msh -d 0.04 >> ${file}.tab
      cut -d$'\t' -f 2 ${file}.tab |cut -d '_' -f1,2 >> ${file}_ids.tab
   done

VAR2=$(ls *_ids.tab)
#need the taxo_loop.sh in same directory
for i in ${VAR2}
   do
      ./taxo_loop.sh ${i}
   done

   
#combine results in one file
VAR3=$(ls *.tsv)
for x in ${VAR3}
   do
      echo ${x} | cat ${x} - >> combined_results.txt
      echo -e "\n" >> combined_results.txt
   done


