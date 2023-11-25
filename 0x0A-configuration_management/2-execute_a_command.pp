# Creating a manifest that kills killmenow process

exec { 'conditions':
command => '/usr/bin/pkill killmenow',
}
