# rsync -rlpt -v -z --delete --port=33444 \
# rsync.wwpdb.org::ftp/data/structures/divided/mmCIF ./divided/mmCIF


rsync -rlpt -v -z --delete \
rsync.ebi.ac.uk::pub/databases/pdb/data/structures/divided/pdb/ ./divided/pdb


# rsync -rlpt -v -z --delete \
# rsync.ebi.ac.uk::pub/databases/pdb/data/structures/divided/mmCIF/ \
# ./mmCIF