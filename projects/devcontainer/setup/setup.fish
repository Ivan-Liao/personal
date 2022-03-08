#!usr/bin/fish

# region configuration
# using in fish shell like # python $WORKING_DIR/vh_core/vh_core/scripts/vishnu_workshop_demo.py
set -Ux WORKING_DIR /workspaces/vscode_dev_env
# env var for the path to the vscode settings.json file
set -Ux VSCODE_SETTINGS /home/.vscode-server/data/Machine/settings.json
# locale configuration
set -Ux LC_ALL C.UTF-8
set -Ux LANG C.UTF-8
# loading sensitive env variables from user configured file set_shell_var_local.fish
source $WORKING_DIR/setup/set_shell_var_local.fish
# endregion


# conda environment creation
and ~/miniconda3/bin/conda init fish
and if test -d /home/miniconda3/envs/pgcli_3.9.5
    echo pgcli_3.9.5 venv already exists
else
    conda create -y -n pgcli_3.9.5 python=3.9.5
end
and conda activate pgcli_3.9.5
and pip install pgcli==3.3.1
and if test -d /home/miniconda3/envs/core_3.6.8
echo core_3.6.8 venv already exists
else
    conda create -y -n core_3.6.8 python=3.6.8
end
and conda activate core_3.6.8
and cd $WORKING_DIR
# git cloning
and if test -d vh_core
    echo vh_core already exists
else
    git clone https://github.com/validatehealth/vh_core.git
end
and if test -d vldt_dags
    echo vldt_dags already exists
else
    git clone https://github.com/validatehealth/vldt_dags.git
end
and if test -d vldt_vrdc
    echo vldt_vrdc already exists
else
    git clone https://github.com/validatehealth/vldt_vrdc.git
end
# python dependencies installation
and pip install -r $WORKING_DIR/setup/requirements.txt
and pip install -e $WORKING_DIR/vh_core
and pip install -e $WORKING_DIR/vldt_dags
# aws setup
and mkdir -p ~/.aws
and printf "[default]\nregion=us-east-1\noutput=json" >~/.aws/config
and printf "[default]\naws_access_key_id=$AWS_ACCESS_KEY_ID\naws_secret_access_key=$AWS_SECRET_ACCESS_KEY" >~/.aws/credentials
# core database connection, creating vh_core/config/vh_env_config.yml
and cp $WORKING_DIR/vh_core/config/vh_env_config_example.yml $WORKING_DIR/vh_core/config/vh_env_config.yml
and sed -i "s|xyz|$USER_INITIALS|" $WORKING_DIR/vh_core/config/vh_env_config.yml
and sed -i 's|dev|florence|' $WORKING_DIR/vh_core/config/vh_env_config.yml
and sed -i "s|/home/users/me/my_directory/|$WORKING_DIR/vh_core|" $WORKING_DIR/vh_core/config/vh_env_config.yml
and printf "gdrive_token: "$WORKING_DIR/vh_core/token.json"" >>$WORKING_DIR/vh_core/config/vh_env_config.yml
# sqltools database settings
and sed -i "s|FLORENCE_USERNAME|$FLORENCE_USERNAME|" $VSCODE_SETTINGS
and sed -i "s|FLORENCE_PASSWORD|$FLORENCE_PASSWORD|" $VSCODE_SETTINGS
#h vh_core/token.json
and aws s3 cp s3://vldt-admin/infrastructure/config/token.json $WORKING_DIR/vh_core
# google_secret.json
and mkdir -p ~/.config/gspread_pandas
and cd ~/.config/gspread_pandas
and aws s3 cp s3://vldt-admin/infrastructure/config/google_secret.json .
# ssl certs
and mkdir -p ~/.ssh
and cd ~/.ssh 
and aws s3 cp s3://vldt-admin/infrastructure/config/ . --recursive --exclude "**" --include "*florence*" 
and chmod 400 *florence* 
and echo $FLORENCE_VH_DB_CONFIG > ~/.ssh/vh_db_config.yml 
and echo $GENEVA_VH_DB_CONFIG >> ~/.ssh/vh_db_config.yml 
and aws s3 cp s3://vldt-admin/infrastructure/config/ . --recursive --exclude "**" --include "*ankara_root.crt" 
and chmod 400 ankara_root.crt
# fish config
and mkdir -p ~/.config/fish
and cp $WORKING_DIR/setup/config.fish ~/.config/fish
and ~/miniconda3/bin/conda init fish
# git default config
and git config --global user.email "$USER_INITIALS@vldt.us"
and git config --global user.name "$USER_INITIALS"
and mkdir -p $WORKING_DIR/.vscode
# first time setup for code snippets
and if test -e $WORKING_DIR/.vscode/base.code-snippets
    echo base.code-snippets
else
    cp $WORKING_DIR/setup/base.code-snippets $WORKING_DIR/.vscode/base.code-snippets
end
# setup new logging path
and sed -i "s|expanduser(\"~\")+'/vhlogs'|'/workspaces/vscode_dev_env/vhlogs'|" /workspaces/vscode_dev_env/vh_core/vh_core/vh_logging.py 
