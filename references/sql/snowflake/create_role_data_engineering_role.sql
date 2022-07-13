begin;
-- create variables for user / password / role / warehouse / database (needs to be uppercase for objects)
use role securityadmin;
set role_name = 'data_engineering_role';
set warehouse_name = 'dataeng_wh';


-- create role and integrate with sysadmin
create role if not exists identifier($role_name);
grant role identifier($role_name) to role SYSADMIN; 


-- Create a warehouse
-------------------------------------------------------------------
use role sysadmin;
create warehouse if not exists identifier($warehouse_name)
warehouse_size = xsmall
warehouse_type = standard
auto_suspend = 60
auto_resume = true
initially_suspended = true;


-- grant the role access to warehouse
use role securityadmin;
grant USAGE
on warehouse identifier($warehouse_name)
to role identifier($role_name);


------------------------------------------------------------------------
--READONLY ACCESS
------------------------------------------------------------------------
-- grant the role to access to database
grant USAGE on database DEV_ENTERPRISE
    to role identifier($role_name);
grant USAGE on database DEV_SEMANTIC_LEGACY_CHAT
    to role identifier($role_name);
grant USAGE on database DEV_SEMANTIC_LEGACY_VOICE
    to role identifier($role_name);
grant USAGE on database DEV_SEMANTIC_MODULAR_CHAT
    to role identifier($role_name);
grant USAGE on database DEV_SEMANTIC_MODULAR_VOICE
    to role identifier($role_name);
grant USAGE on database RAW_DEV
    to role identifier($role_name);



-- grant the role to access usage privilege to all schemas in database
grant USAGE on all schemas in database DEV_ENTERPRISE
    to role identifier($role_name);
grant USAGE on all schemas in database DEV_SEMANTIC_LEGACY_CHAT
    to role identifier($role_name);
grant USAGE on all schemas in database DEV_SEMANTIC_LEGACY_VOICE
    to role identifier($role_name);
grant USAGE on all schemas in database DEV_SEMANTIC_MODULAR_CHAT
    to role identifier($role_name);
grant USAGE on all schemas in database DEV_SEMANTIC_MODULAR_VOICE
    to role identifier($role_name)
grant USAGE on all schemas in database RAW_DEV
    to role identifier($role_name);


-- grant role to select privilege to all tables in database
grant SELECT on all tables in database DEV_ENTERPRISE
    to role identifier($role_name);
grant SELECT on all tables in database DEV_SEMANTIC_LEGACY_CHAT
    to role identifier($role_name);
grant SELECT on all tables in database DEV_SEMANTIC_LEGACY_VOICE
    to role identifier($role_name);
grant SELECT on all tables in database DEV_SEMANTIC_MODULAR_CHAT
    to role identifier($role_name);
grant SELECT on all tables in database DEV_SEMANTIC_MODULAR_VOICE
    to role identifier($role_name)
grant SELECT on all tables in database RAW_DEV
    to role identifier($role_name);


-- grant role to select privilege to all tables in database
grant SELECT on all views in database DEV_ENTERPRISE
    to role identifier($role_name);
grant SELECT on all views in database DEV_SEMANTIC_LEGACY_CHAT
    to role identifier($role_name);
grant SELECT on all views in database DEV_SEMANTIC_LEGACY_VOICE
    to role identifier($role_name);
grant SELECT on all views in database DEV_SEMANTIC_MODULAR_CHAT
    to role identifier($role_name);
grant SELECT on all views in database DEV_SEMANTIC_MODULAR_VOICE
    to role identifier($role_name)
grant SELECT on all views in database RAW_DEV
    to role identifier($role_name);


-- grant role to future privileges in database
-- future schemas
grant SELECT on future schemas in database DEV_ENTERPRISE
    to role identifier($role_name);
grant SELECT on future schemas in database DEV_SEMANTIC_LEGACY_CHAT
    to role identifier($role_name);
grant SELECT on future schemas in database DEV_SEMANTIC_LEGACY_VOICE
    to role identifier($role_name);
grant SELECT on future schemas in database DEV_SEMANTIC_MODULAR_CHAT
    to role identifier($role_name);
grant SELECT on future schemas in database DEV_SEMANTIC_MODULAR_VOICE
    to role identifier($role_name)
grant SELECT on future schemas in database RAW_DEV
    to role identifier($role_name);

-- future tables
grant SELECT on future tables in database DEV_ENTERPRISE
    to role identifier($role_name);
grant SELECT on future tables in database DEV_SEMANTIC_LEGACY_CHAT
    to role identifier($role_name);
grant SELECT on future tables in database DEV_SEMANTIC_LEGACY_VOICE
    to role identifier($role_name);
grant SELECT on future tables in database DEV_SEMANTIC_MODULAR_CHAT
    to role identifier($role_name);
grant SELECT on future tables in database DEV_SEMANTIC_MODULAR_VOICE
    to role identifier($role_name)
grant SELECT on future tables in database RAW_DEV
    to role identifier($role_name);


-- future views
grant SELECT on future views in database DEV_ENTERPRISE
    to role identifier($role_name);
grant SELECT on future views in database DEV_SEMANTIC_LEGACY_CHAT
    to role identifier($role_name);
grant SELECT on future views in database DEV_SEMANTIC_LEGACY_VOICE
    to role identifier($role_name);
grant SELECT on future views in database DEV_SEMANTIC_MODULAR_CHAT
    to role identifier($role_name);
grant SELECT on future views in database DEV_SEMANTIC_MODULAR_VOICE
    to role identifier($role_name)
grant SELECT on future views in database RAW_DEV
    to role identifier($role_name);


commit;