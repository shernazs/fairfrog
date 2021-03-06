angular.module('webshop.controllers', [])
.controller("webshop-controller", function( $scope, $window ) {
	$scope.allProducts = [];
	$scope.items = [];
  $scope.advertorialProducts =[];
  $scope.popularProducts = [];
	$scope.loadedproducts = 0;
  $scope.homepage = 1;

	$scope.initFunction = function() {
		console.log("controller init");
    $scope.getAdvertorialProducts();
    $scope.getPopularProducts();
	}

   $scope.getAdvertorialProducts = function() {
    var config = {
          type: "GET",
          url: "http://localhost:8000/shop/get_featured_products",
          dataType: 'json',
          data: {
          },
        success: function( response ) {
        console.log( "success1");
        if( response.status == 1) {
          console.log( "success");
          $scope.advertorialProducts = response.advertorial_products_list;
          $scope.$apply();
          console.log("inside ad block");
          console.log($scope.advertorialProducts);
        }
       }
      };
    $.ajax(config);
   }

   $scope.getPopularProducts = function() {
    var config = {
          type: "GET",
          url: "http://localhost:8000/shop/get_popular_products",
          dataType: 'json',
          data: {
          },
        success: function( response ) {
        console.log( "success1");
        if( response.status == 1) {
          console.log( "success popular");
          $scope.popularProducts = response.popular_products_list;
          $scope.$apply();
          console.log($scope.popularProducts);
        }
       }
      };
    $.ajax(config);
   }

  $scope.getProducts = function(categories) {

    console.log("in get categories");

    caturl = "http://127.0.0.1:8000/get_products?cat=" + categories
    console.log(caturl);
    var config = {
          type: "GET",
          url: caturl,
          dataType: 'json',
          data: {
          },
        success: function( response ) {
        console.log( "success1");
        if( response.status == 1) {
          console.log( "success");
          $scope.allProducts = response.products_list;
          console.log( $scope.allProducts);
          $scope.homepage = null;
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

});

angular.module('webshop.controllers').directive('showonhoverparent',function() {
   	console.log("hello world");
      return {
         link : function(scope, element, attrs) {
            element.parent().parent().bind('mouseenter', function() {
                var div = element.childNodes[0];
      			div.style.display = "block";
            });
            element.parent().parent().bind('mouseleave', function() {
                 var div = element.childNodes[0];
      			 div.style.display = "none";
            });
       }
   };
});

