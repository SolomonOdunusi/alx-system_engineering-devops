# Creating a file in tmp with puppet

file {'/tmp/holberton':
content => 'I love Puppet',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
}
