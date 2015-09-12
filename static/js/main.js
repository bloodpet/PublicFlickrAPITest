var app = angular.module('myApp', []).
config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/', {
        controller: 'SearchController',
        templateUrl: 'static/partials/search-form.html'
    })
}]);

app.controller('SearchController', function($scope, $http) {
    $scope.items = [];
    $scope.searchTerm = '';
    $scope.pageTitle = 'All images';
    $scope.search = function() {
        $scope.pageTitle = 'Search for ' + $scope.searchTerm;
        $http({
            method: 'GET',
            url: '/search?search_term=' + $scope.searchTerm
        }).success(function(data) {
            $scope.items = data.items;
        }).error(function(data, status) {
            console.log(data);
            console.log(status);
        });
    };
})
