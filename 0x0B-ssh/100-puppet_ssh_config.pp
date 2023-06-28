# configure ssh
exec {'Configure file':
   command => '/bin/echo -e "IdentityFile ~/.ssh/school\npasswordAuthentication no" >> /etc/ssh/ssh_config',
   path => '/etc/ssh/ssh_config',
}
