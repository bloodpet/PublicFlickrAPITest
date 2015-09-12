var app = angular.module('myApp', []);

app.controller('SearchController', function($scope) {
    $scope.searchTerm = '';
    $scope.search = function() {
        console.log('Start search for ' + $scope.searchTerm);
    };
})
