# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions

alias av0="source /home/ec2-user/Dvenv/bin/activate"
alias rs0="python manage.py runserver ec2-3-89-115-172.compute-1.amazonaws.com:8000"
alias mi0="python manage.py migrate"
alias runno0="nohup python3 magage.py runserver 0.0.0.0:8000"
