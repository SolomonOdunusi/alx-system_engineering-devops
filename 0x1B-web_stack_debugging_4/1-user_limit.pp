# Change the OS config
exec { 'change-os-configuration-for-holberton-user':
  path    => '/bin',
  command => "ulimit -n 2048",
}
