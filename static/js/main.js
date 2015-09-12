var app = angular.module('myApp', []).
config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/', {
        controller: 'SearchController',
        init: 'search',
        templateUrl: 'static/partials/search-form.html'
    })
}]);

app.controller('SearchController', function($scope, $http) {
    $scope.items = [];
    $scope.searchTerm = '';
    $scope.pageTitle = 'All images';
    $scope.search = function() {
        $scope.statusMsg = 'Searching...'
        if ($scope.searchTerm) {
            $scope.pageTitle = 'Search for ' + $scope.searchTerm;
        } else {
            $scope.pageTitle = 'All images';
        }
        $http({
            method: 'GET',
            url: '/search?search_term=' + $scope.searchTerm
        }).success(function(data) {
            if (! data.items.length) {
                $scope.statusMsg = 'No images found.'
            }
            $scope.items = data.items;
        }).error(function(data, status) {
            console.log(data);
            console.log(status);
            $scope.search();
        });
    };
    $scope.search();
})
