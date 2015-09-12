var app = angular.module('myApp', []).
config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/', {
        controller: 'SearchController',
    })
}]);

app.controller('SearchController', function($scope, $http) {
    $scope.searchTerm = '';
    $scope.pageTitle = 'All images';
    $scope.search = function() {
        console.log('Start search for ' + $scope.searchTerm);
        $scope.pageTitle = 'Search for ' + $scope.searchTerm;
    };
})
