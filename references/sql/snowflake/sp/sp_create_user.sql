use role accountadmin;
use database DATAENG_TEST;
use schema TEST;


-- Review all parameters by searching for the prefix YOUR_
CREATE OR REPLACE PROCEDURE sp_create_user()
RETURNS string
LANGUAGE JAVASCRIPT
AS
$$
    //# Configuration
    var user_name = 'ihl_test'
    var login_name = 'ihl_test@xselltechnologies.com'
    var user_password = '';
    var warehouse_name = 'dateng_wh'
    var default_role = 'SANDBOX_ROLE'
    var roles = ['READALL_ROLE', 'SANDBOX_ROLE', 'DEV_ROLE', 'LEAD_DEV'];
    //# Create user
    snowflake.execute(
      {
        sqlText: `use role securityadmin;`
      }
    )
    try {
      snowflake.execute(
        {
          sqlText: `create user if not exists identifier(:1)
                    password = identifier(:2)
                    login_name = identifier(:3)
                    default_role = identifier(:4)
                    MUST_CHANGE_PASSWORD = False
                    default_warehouse = identifier(:5);`
          ,binds:[user_name,user_password,login_name,default_role,warehouse_name]
        }
      )
    }
    catch(err){
      return "Failed 1: " + err;
    };
    //# Assign roles to user in loop
    for (var rol of roles) {
        try {
            snowflake.execute(
                {
                 sqlText: `grant role identifier(:1) to user identifier(:2);`
                ,binds: [rol, user_name]
                }
            );
        }
        catch(err){
            return "Failed 2: " + err;
        };
    };
    
    return "Succeded.";
$$;

call sp_create_user();