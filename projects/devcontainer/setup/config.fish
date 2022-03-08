# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
eval /opt/conda/bin/conda "shell.fish" "hook" $argv | source
# <<< conda initialize <<<
source $WORKING_DIR/setup/set_shell_var_local.fish

# aliases
function mkcd --description "mkdir and cd"
        mkdir $argv[1] && cd $argv[1]
end

function la --description "ls -la"
    ls -la
end

function gitone --description "shorthand for git log --oneline"
    git log --oneline
end

function gitname --description "shorthand for git log --name-status"
    git log --name-status
end

# need to set up public/private key configuration
function in_flo --description "ssh into florence ec2 instance"
        ssh -i ~/.ssh/id_rsa -L 4003:localhost:5901 ubuntu@13.58.128.89  -v
end

# need to set up public/private key configuration
function in_gen --description "ssh into geneva ec2 instance"
        ssh -i ~/.ssh/id_rsa -L 4003:localhost:5901 ubuntu@18.223.194.252  -v
end

# pgcli functions 
function pgcli_connect_florence --description "function to use pgcli to connect to florence"
    pgcli "port=5432 \
        host=13.58.128.89 user=$FLORENCE_USERNAME  password=$FLORENCE_PASSWORD \
        sslmode=require \
        sslrootcert=/home/.ssh/ankara_root.crt \
        sslcert=/home/.ssh/florence.crt \
        sslkey=/home/.ssh/florence.key \
        dbname=apcd"
end
    
function pgcli_connect_geneva --description "function to use pgcli to connect to geneva"
    pgcli "port=5432 \
        host=18.223.194.252 user=$FLORENCE_USERNAME  password=$FLORENCE_PASSWORD \
        sslmode=require \
        sslrootcert=/home/.ssh/ankara_root.crt \
        sslcert=/home/.ssh/florence.crt \
        sslkey=/home/.ssh/florence.key \
        dbname=apcd"
end

# function to clean and color psycopg2 output
function colorstuff
        while read -l input
            set input (echo $input | sed 's|\\\n| & |g')
            switch $input
                case "[SQL:*" 
                    for word in (string split ' ' $input)
                        switch $word
                            case "FROM"
                                set_color blue
                                echo -e "$word"
                            case "*"
                                set_color normal
                                echo -e "$word"
                        end
                    end
                case "*InternalError*"
                    set_color red
                    echo -e "$input"
                case "*TASK_ID:*"
                    set_color 196F3D # dark green
                    echo -e "$input"
                case "*TEMPLATE:*"
                    set_color 229954 # green
                    echo -e "$input"
                case "*CMD#*"
                    set_color 7DCEA0 # light green
                    echo -e "$input"
                case "*warning*"
                    set_color yellow
                    echo -e "$input"
                case "*FROM*"
                    set_color blue
                    echo -e "$input"
                case "\n"
                    set_color normal
                    echo -e "\n"
                case "*"
                    set_color normal
                    echo -e "$input"
            end
        end
        set_color normal
    end