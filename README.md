# Sequence-manipulation-tools
Just a few linux commands or python based scripts that I tend to use a lot

## Mutating a DNA sequence at a known rate
You can use the script MutateDNAString.py to introduce n number of mutations in a given DNA sequence. For example if you give the code the DNA string 'AACA' and want 1 mutation in the string you might get 'TACA' as the string that is returned. Each base has an equal chance of getting picked to be mutated and a base can be converted to 3 other bases with equal probability. If you want to introduce multiple mutations (n>1), the code is written is such a way that each position can only be mutated once, but this is easily modifiable in the code. 

To write this script I modified code obtained from this fantastic resource https://hplgit.github.io/bioinf-py/doc/pub/html/main_bioinf.html to fit my needs.

To run the code simply use the command and provide it with the string of your choice and the number of mutations you want to introduce:

`python MutateDNAString.py --String AACA --nMut 2` 

To mutate all sequences in a fasta file at a given substitution rate, you will need BioPython to read the file. Also here please provide number of mutations you want as a percentage value and simply run the code:

`python MutateDNAFasta.py --fasta test.fa --nMut 50 --output testOutput.fa` 


## Sorting bed file 
sort -k1,1 -k2,2n input.bed > input.sorted.bed

## Extending or reducing coordinates in bed file
awk '{ print $1"\t"$2+50"\t"$3-50 }' Input.bed > InputExtended.bed (Extends by 50)

## Counting # of sequences in fasta file
grep -c ">" seq.fa

## Selecting only certain chromosomes from bed file for ML training/testing tasks
awk 'BEGIN{OFS="\t";} { if($1 == "chr4" || $1 == "chr2" || $1 == "chr18" || $1 == "chr20" || $1 == "chr9" || $1 == "chr13" ) { print }}' input.bed > inputTrain.bed

## dinucleotide shuffle fasta 
Check out the fasta-dinucleotide-shuffle-py3.py script in Meme-Suite

## Concatenate fasta files with similar ID
seqkit concat function is really fast https://bioinf.shenwei.me/seqkit/usage/#concat

## Apply some function to multiple files with common extension in linux (multiple peak/bed files)
for sample in `ls /filelocation/*.peaks`;
do
dir="/filelocation/"
dir2="/Outputfilelocation/"
base=$(basename $sample ".peaks")
awk '{print $1"\t"$4 -50"\t"$4 + 50}' ${dir}/${base}.peaks > ${dir2}/${base}.peaks
done

