# Coupling fraction calculation
<b>This script calculates the coupling fraction from raw read counts</b><br/>
<b>Author</b>: Mudra Hegde  
<b>Email</b>: mhegde@broadinstitute.org  
<b>Version: 1.0 </b> 

<b>Required packages</b>
1. pandas

<b>Inputs</b><br/>
<b>Input File</b>: .txt file with raw read counts for all possible combinations <br/>
<b>Reference File</b>: .csv reference file with all possible construct combinations in the first column; no header. Reference files for our experiments included in this folder<br/>
<b>Output File</b><br/>

<b>To run this script, type the following on the terminal:</b><br/>
python calc_couplingfraction_v1.0.py --input-file \<Path to inputfile\> --ref \<Path to reference file\> --outputfile \<.txt output file name\> 