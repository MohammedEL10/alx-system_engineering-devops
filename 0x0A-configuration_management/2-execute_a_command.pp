# Executes a command
exec { 'pkill killmenu':
	path => '/usr/bin:/sbin:/bin'
}

