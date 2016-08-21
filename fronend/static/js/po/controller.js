angular.module('webshop.controllers', [])
.controller("webshop-controller", function( $scope, $window ) {
	$scope.allProducts = [];
	$scope.initFunction = function() {
		console.log("controller init");
		$scope.getProducts();
	}
	$scope.getProducts = function() {
		var config = {
      		type: "GET",
      		url: "http://localhost:8000/shop/get_products",
      		dataType: 'json',
      		data: {
      		},
      	success: function( response ) {
		   	console.log( "success1");
				if( response.status == 1) {
					console.log( "success");
					$scope.allProducts = response.products_list;
					$scope.$apply();
				}
		   }
    	};
    $.ajax(config);
   }
   $scope.goToPDP = function(url) {
		console.log("inPDP: "+ url);
		$window.open(url);

   }
})

