'''
Calculates coupling fraction for construct combinations
Author: Mudra Hegde
Email: mhegde@broadinstitute.org
'''

import pandas as pd
import csv, argparse

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-file',
        type=str,
        help='File with read counts for all combinations with all experimental conditions')
    parser.add_argument('--ref',
        type=str,
        help='Reference file of combinations')
    parser.add_argument('--outputfile',
        type=str,
        help='Output file')
    return parser

if __name__ == '__main__':
    args = get_parser().parse_args()
    input_df = pd.read_table(args.input_file)
    ref = pd.read_csv(args.ref,header=None)
    ref.columns = ['Combinations']
    cond = list(input_df.columns)[1:]
    output_df = pd.DataFrame(columns=list(input_df.columns))
    for i,r in ref.iterrows():
        comb = r['Combinations']
        row = [comb]
        sg_df = input_df[input_df['Combinations'].str.startswith(comb.split(':')[0])]
        sg_df.index = range(0,len(sg_df))
        max_pcts = []
        for c in cond:
            c_sum = sg_df[c].sum()
            if c_sum != 0:
                pct = [x/float(c_sum) for x in sg_df[c]]
                max_pct = max(pct)
                pct_index = pct.index(max_pct)
            else:
                max_pct = 'NA'
            max_pcts.append(max_pct)
        row.extend(max_pcts)
        output_df.loc[i,:] = row
    output_df.to_csv(args.outputfile,sep='\t',index=False)

