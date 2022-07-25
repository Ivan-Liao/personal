# syntax, remove dryrun to actually delete
aws s3 rm --dryrun --recursive --exclude '*' --include 'abc_1*' s3://mybucket/my/path/to/topdir/
# e.g. 
aws s3 rm --dryrun --recursive --exclude '*' --include '*test*' s3://optus-production-data/extracts/scheduled/