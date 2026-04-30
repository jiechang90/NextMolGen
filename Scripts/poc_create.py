from glob import glob
from os import path
from pymol import stored
from pymol import cmd
from pathlib import Path
from my_toolset.my_utils import mapper,imapper
import os,sys

# pdbDir="/home/data/jay/Vue-molOpt/Codes/rscbPDB/divided/pdb"
# pdbFile="/mnt/public-bg6/jay.zhang/Projects-public/rscbPDB/pdb/g2/pdb6g20.ent.gz"

# def process_pdb(pdbFile):
#     ''' Process the file name and path  '''
#     pdbPath=Path(pdbFile)
#     parentPath=pdbPath.parent
#     pdbID=pdbPath.name.split('.')[0][-4:]
#     # print(pdbID, parentPath)

#     cmd.delete('all')
#     cmd.load(pdbFile)
#     cmd.remove("solvent")
#     cmd.select("het1", "hetatm")
#     cmd.select("input", "organic")
#     cmd.select("protein1", "polymer")
#     cmd.select("processed", "none")
#     mol_cnt = 0
#     # cmd.save( f"{parentPath}/{pdbID}_{mol_cnt}_all.pdb", 'all' ) 
#     # print(cmd.count_atoms("input"))
#     # cmd.iterate("bymolecule input",'print(resn, resi)')
#     while cmd.count_atoms("input"):
#         # filter through the selections, updating the lists
#         cmd.select("current","bymolecule first input")
#         # cmd.iterate("bymolecule current",'print(resn, resi)')
#         cmd.select("processed","processed or current")
#         cmd.select("input","input and not current")

#         # save the ligand
#         resCommon=['CYS', 'ALA', 'PRO',  'SER', 'MET', 'THR',  'TYR', 'TRP', 'HIS', 'ASN', 'LYS', 'GLN', 'ASP', 'ILE', 'LEU', 'GLY', 'VAL', 'PHE', 'GLU', 'ARG']
        
#         ## some ligand have bond with the protein and will be selected by pymol
#         stored.resList=[]
#         cmd.iterate("byresidue current",'stored.resList.append(resn)')
#         ligandName='peptide'
#         for ires in set(stored.resList):
#             if ires not in resCommon:
#                 ligandName=ires
#                 if cmd.count_atoms("current")>60:
#                     cmd.select(f"current",f"resn {ires} and current")
#                 break
        
#         curOut = f"{parentPath}/{pdbID}_{mol_cnt}_{ligandName}_ligand.pdb"
#         curSel = "current"
#         cmd.save( curOut, curSel )

#         # save the pocket
#         cmd.select("pocket","byres protein1 within 7 of current")
#         curOut = f"{parentPath}/{pdbID}_{mol_cnt}_{ligandName}_pocket.pdb"
#         curSel = "pocket"
#         cmd.save( curOut, curSel ) 

#         mol_cnt = mol_cnt + 1

# pdbDir="/home/data/jay/Vue-molOpt/Codes/rscbPDB/divided/pdb"
# pdbFiles=glob(f"{pdbDir}/**/*.ent.gz")

def process_pdb(pdbFile):
    ''' Process the file name and path  '''
    os.system(f"python /home/data/jay/Vue-molOpt/Codes/rscbPDB/poc_create_single.py {pdbFile}")

pdbDir="/home/data/jay/Vue-molOpt/Codes/rscbPDB/divided/mmCIF/mmCIF"
pdbFiles=glob(f"{pdbDir}/**/*.cif.gz")
res=imapper(10)(process_pdb, input=pdbFiles)



# process_pdb(pdbFile)
