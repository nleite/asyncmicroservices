var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope) {
    $scope.title= "Welcome!";
    $scope.name= "Doe";
});



app.controller( 'listController', function($scope, $http){
    $http.get("http://localhost:5002/data").success( function( response ){
      $scope.list = response._items;

    });
} );
