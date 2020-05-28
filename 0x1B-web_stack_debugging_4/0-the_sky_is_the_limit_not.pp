# Fix failed simulated HTTP requests using Apache ab
exec { 'Debug failed requests':
  command => 'sed -i "s/15/2000/g" /etc/default/nginx',
  path    => '/usr/local/bin/'
}
exec { 'nginx service restart':
  command => 'sudo service nginx restart',
  path    => ['/usr/sbin/service']
}
