# usr/bin/pup
# install an especific version of flask (2.1.0)
# install an especific version of werkzeug (2.1.1)
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
