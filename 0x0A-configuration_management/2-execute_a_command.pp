# kill process killme now

exec { 'kill':
	command => 'killmenow',
	provider => 'shell',
}

