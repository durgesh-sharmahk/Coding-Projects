function AppCtrl($scope, $http){
	console.log("Hello from controller");

	var refresh = function(){
    $http.get("/contactList").then(function(response){
    	console.log("I got data i have requested");
    	$scope.contactList = response.data;
    	$scope.contact = {};
    })
};
refresh();

    $scope.addContact = function(){
    	console.log($scope.contact);
    	$http.post('/contactList',$scope.contact).then(function(response){
    		console.log(response);
    		refresh();
    	});
    };

    $scope.remove = function(id){
        console.log(id);
        $http.delete('/contactList/'+id).then(function(response){
            refresh();
        })
    }
    $scope.edit = function(id){
        console.log(id);
        $http.get('/contactList/'+id).then(function(response){
            $scope.contact = response.data;
        })
    }
    $scope.update = function(){
        console.log($scope.contact._id);
        $http.put('/contactList/'+$scope.contact._id, $scope.contact).then(function(response){
            refresh();
        })
    }
    $scope.deselect = function(){
        $scope.contact = {};
    }
}


angular.module('myApp', [])
.controller('personCtrl', AppCtrl);
