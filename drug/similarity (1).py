from rdkit import Chem
from rdkit import DataStructs
from rdkit.Chem.Fingerprints import FingerprintMols
import pandas as pd
import numpy as np
import sys


# read and Conconate the csv's
df_1 = pd.read_csv('data.csv')
df_2 = pd.read_csv('resv.csv')
df_3 = pd.concat([df_1, df_2],axis=0)

# proof and make a list of SMILES
df_smiles = df_3['Smiles']
c_smiles = []
for ds in df_smiles:
    try:
        cs = Chem.CanonSmiles(ds)
        c_smiles.append(cs)
    except:
        print('Invalid SMILES:', ds)

print()

# make a list of mols
ms = [Chem.MolFromSmiles(x) for x in c_smiles]

# make a list of fingerprints (fp)
fps = [FingerprintMols.FingerprintMol(x) for x in ms]


# compare all fp pairwise without duplicates
for n in range(len(fps)-1): # -1 so the last fp will not be used
    s = DataStructs.BulkTanimotoSimilarity(fps[-1], fps[:len(fps)-1]) # +1 compare with the last fp
	
r=c_smiles[:len(c_smiles)-1]
dg=pd.DataFrame()
dg["target"]=r
dg["sim"]=s
dg.to_csv("final.csv",index=None)	
	
	
	
	
	
	
 