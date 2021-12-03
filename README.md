# Sequence-manipulation-tools
Just a few linux commands/softwares that I find useful in handling sequencing based data or files (bed etc)

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

