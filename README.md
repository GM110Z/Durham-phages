**hhmscan-prep**: starting from a snippy table, it prepares a multifasta files of proteins that were found to carry a snp in it. Uses efetch and biopython and SeqIO

**TheBrexNewScript.py**: Uses a gb and faa file to find instances of genomes where two genes are co-localised. Colocalised genes are found using hmm profiles. Name derives from the fact it was written for BREX analysis..might change

**wrapper.sh** : wrapper script for running TheBrexNewScript.py on more genomes

**SNPs-graphics-Jupyter**: Jupyter book to annotate SNPs predicted with Snippy in a graphic output

**mash_and_taxonomy.sh**: runs mash dist against a refseq database and retrieves the taxonomy of the hits

**taxo-loop.sh** loops mash_and_taxonomy.sh on more genomes
