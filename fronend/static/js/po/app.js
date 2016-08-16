angular.module('webshop', [
		'webshop.controllers'
])
.config([
	'$httpProvider',
	function($httpProvider) {
		$httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
	}
])
