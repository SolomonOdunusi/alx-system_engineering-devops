# Debugging with Apachebench
exec { 'change ulimit':
  path    => '/bin',
  command => "sed -i 's/15/2000/g' /etc/default/nginx",
}

exec { 'nginx restart':
  path    => '/etc/init.d',
  command => '/etc/init.d/nginx restart',
  require => Exec['change ulimit'],  # Ensure 'change ulimit' runs before 'nginx restart'
}
