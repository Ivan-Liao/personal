set USER_INITIALS "**********"
set AWS_ACCESS_KEY_ID "**********"
set AWS_SECRET_ACCESS_KEY "**********"
set FLORENCE_USERNAME "**********"
set FLORENCE_PASSWORD "**********"
set FLORENCE_VH_DB_CONFIG 'florence:
    db_loc : "13.58.128.89"
    root_cert_loc : "/home/.ssh/ankara_home.crt"
    ssl_cert_loc  : "/home/.ssh/florence.crt"
    sslkey_loc    : "/home/.ssh/florence.key"
    database      : "apcd"
    username      : "'"$FLORENCE_USERNAME"'"
    password      : "'"$FLORENCE_PASSWORD"'"'
set GENEVA_VH_DB_CONFIG 'geneva:
    db_loc : "18.223.194.252"
    root_cert_loc : "/home/.ssh/ankara_home.crt"
    ssl_cert_loc  : "/home/.ssh/florence.crt"
    sslkey_loc    : "/home/.ssh/florence.key"
    database      : "apcd"
    username      : "'"$FLORENCE_USERNAME"'"
    password      : "'"$FLORENCE_PASSWORD"'"'
