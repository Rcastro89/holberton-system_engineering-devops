# first puppet create file

file { 'ssh_config':
  ensure  => 'file',
  path    => '/etc/.ssh',
  content => 'HOTS *
	IdentityFile ~/.ssh/school
    PasswordAuthentication no'
}