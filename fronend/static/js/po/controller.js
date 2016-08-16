angular.module('webshop.controllers', [])
.controller("webshop-controller", function( $scope ) {

	$scope.initFunction = function() {
		console.log("controller init");
		
		$scope.getProducts();
	}

	$scope.getProducts = function() {
		var config = {
      		type: "GET",
      		url: "https://fairfrog-alok416.c9users.io/webshop/get_products",
      		dataType: 'json',
      		data: {
        		// 'longitude' : $scope.longitude,
        		// 'latitude' : $scope.latitude,
      		},
      	success: function( response ) {
		   	console.log( "success1");
				if( response.status == 1) {
					console.log( "success");
					//$scope.address = response.address;
					//$scope.$apply();
					console.log( response.products_list );
					//$scope.setMapMarker($scope.latitude, $scope.longitude, response.address );
				}
		   }
    };
    $.ajax(config);
   }

 
})
