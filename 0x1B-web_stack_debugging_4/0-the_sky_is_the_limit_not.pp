# reload nginx

exec { 'for-nginx':
  command => 'sed -i "s/15/8192/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

-> exec { 'restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
