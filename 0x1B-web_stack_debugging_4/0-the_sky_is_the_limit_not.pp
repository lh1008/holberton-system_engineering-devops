# Fix failed simulated HTTP requests using Apache ab
exec { 'Debug failed requests':
  command => 'sed -i \'s/15/15000/g\' /etc/default/nginx',
  path    => ['/bin']
}
exec { 'nginx service restart':
  command => 'service nginx restart',
  path    => ['/usr/bin']
}
