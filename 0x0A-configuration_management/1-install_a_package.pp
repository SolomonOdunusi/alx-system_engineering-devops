# Installing puppet-lint with puppet

package { 'puppet-lint':
ensure   => '2.1.1',
provider => 'gem',
install_options => ['--no-document']
}
