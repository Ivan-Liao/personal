-- set parameters
use role securityadmin;
set role_names = 'ROLE_HERE'; -- e.g. 'data_engineering_role';
set user_name = 'USER_NAME_HERE' -- e.g. 'supratik_das';
set login_name = 'LOGIN_NAME_HERE' -- e.g. 'supratik.das@xselltechnologies.com';
set user_password = ''; -- empty string for individual users
set warehouse_name = 'WAREHOUSE_HERE' -- e.g. 'dataeng_wh';



-- create role and integrate with sysadmin -- @ihl seems dangerous
create role if not exists identifier($role_name);
grant role identifier($role_name) to role SYSADMIN;


--CREATE A USER
create user if not exists identifier($user_name)
password = $user_password
login_name = $login_name
default_role = $role_name
MUST_CHANGE_PASSWORD = False
default_warehouse = $warehouse_name;
grant role identifier($role_name) to user identifier($user_name);

