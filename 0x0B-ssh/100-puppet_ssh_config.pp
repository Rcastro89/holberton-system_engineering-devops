# update ssh config.
include stdlib

file_line { 'first line':
  path =>  '/etc/ssh/ssh_config',
  line =>  'PasswordAuthentication no',
}

file_line {  'second line':
  path =>  '/etc/ssh/ssh_config',
  line =>  'IdentityFile ~/.ssh/school',
}