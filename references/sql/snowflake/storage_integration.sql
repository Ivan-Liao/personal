-- https://docs.snowflake.com/en/user-guide/data-load-s3-config-storage-integration.html
-- get role arn from devops

create or replace storage integration <YOUR_STORAGE_INTEGRATION_NAME>
  type = external_stage
  storage_provider = s3
  storage_aws_role_arn = '<YOUR_ROLE_ARN>'
  enabled = true
  storage_allowed_locations = ('<YOUR_BUCKET_NAME>');

-- example
create or replace storage integration extract_test
  type = external_stage
  storage_provider = s3
  storage_aws_role_arn = '<YOUR_ROLE_ARN>'
  enabled = true
  storage_allowed_locations = ('<YOUR_BUCKET_NAME>');
desc integration extract_test;

-- have devops update trust relationship policy

CREATE or replace STAGE test_sample_data_extract
url = '<YOUR_S3_URL>'
STORAGE_INTEGRATION = extract_test
COMMENT = 'This stage is for test extract data from snowflake_sample_data';

COPY INTO @test_sample_data_extract/data.csv
FROM (SELECT * FROM DATAENG_TEST.EXTRACT.SUPPLIER_4_PERCENT) 
//STORAGE_INTEGRATION = extract_test
FILE_FORMAT = ( TYPE = CSV null_if=('') COMPRESSION = None) 
OVERWRITE = TRUE 
SINGLE = TRUE 
HEADER = TRUE;


/*
-- json for role permission policy and trust relationship policy below


-- policy
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "s3:Get*",
                "s3:List*",
                "s3:Put*"
            ],
            "Resource": [
                "arn:aws:s3:::xsell-data-engineering-test"
                "arn:aws:s3:::xsell-data-engineering-test/*"
            ],
            "Effect": "All"
            
        }    
    ]
}


--trust
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::210437325872:user/0x89-s-ohst7464"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "sts:ExternalId": "HH46454_SFCRole=5_jkGqRsAa6QkG9YQs7qHcdy0OteY="
                }
            }
        }
    ]
}
*/