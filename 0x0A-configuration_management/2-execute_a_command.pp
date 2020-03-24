# Puppet that kills a process
exec { 'killmenow':
  path    => ['/usr/bin', '/bin', '/usr/local/bin'],
  command => "pkill -f killmenow",
}
