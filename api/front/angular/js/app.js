var app = angular.module('MyApp', [
  'ngRoute',
  'controllers'
]);

app.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/list', {
        templateUrl: '../template/list.html',
        controller: 'listController'
      }).
      otherwise({
        redirectTo: '/'
      });
  }]);
