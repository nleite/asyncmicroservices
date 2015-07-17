var searchApp = angular.module('Search', ['infinite-scroll']);
myApp.controller('SearchController', function($scope) {
  $scope.images = [1, 2, 3, 4, 5, 6, 7, 8];

  $scope.loadMore = function() {
    var last = $scope.images[$scope.images.length - 1];
    for(var i = 1; i <= 8; i++) {
      $scope.images.push(last + i);
    }
  };
});

searchApp.factory('Data', function($http){
  var Data = function(){
    this.title ="";
    //FIXME change to a default picture link
    this.permalink = '';
    this.busy = false;
    this.after = '';
  };

  Data.prototype.nextPage = function(){
    if (this.busy) return;
    this.busy = true;
    var url = "OUR NEW REST SERVICE API CALL ";
    $http.jsonp(url).success(function(data) {
      var items = data.data.children;
      for (var i = 0; i < items.length; i++) {
        this.items.push(items[i].data);
      }
      this.after = "t3_" + this.items[this.items.length - 1].id;
      this.busy = false;
    }.bind(this));
  };
  return Data;

});
