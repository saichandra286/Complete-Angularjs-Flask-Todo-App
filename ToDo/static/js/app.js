angular.module('ToDo', ['ngAnimate', 'tododirectives'])

.config(['$interpolateProvider', function($interpolateProvider){

	$interpolateProvider.startSymbol('(((');
	$interpolateProvider.endSymbol(')))');
}])


.controller('todocntrl', ['$scope', '$http', function($scope, $http){
var list=[];
$http.get('http://localhost:5000/saitodo/api/v1.0/tasks').then(function(data){
		list = data.data;
			$scope.lists = list.tasks;
}, function(error){
	console.log(error);
})

$scope.update = function(id){
			$scope.th = id;
			$scope.displayup = true;
		}

$scope.newtodo = function(){
	$http.post('http://localhost:5000/saitodo/api/v1.0/tasks', {'title': $scope.li.title}).then(function(data){
		var ln = data.data;
		console.log(ln);
		$scope.lists.push(ln.tsk);
		$scope.li.title=''; 
	}, function(error){
		alert('already exists');
	})
};

$scope.DelAll = function(){
	$http.delete('http://localhost:5000/saitodo/api/v1.0/tasks').then(function(data){
		var tn = data.data;
		console.log(tn);
		$scope.lists = tn.tasks;
	})
};

$scope.upda = function(id, nam){
			console.log(id);
			var id=id;
			$http.put('http://localhost:5000/saitodo/api/v1.0/tasks/'+id+'', {"title": nam}).then(function(data){
				var jn = data.data;
				console.log(jn.tasks);
				$scope.lists = jn.tasks;
				$scope.th='';
				//$scope.lists[0] = jn.tsk;
			}, function(error){
				alert("duplicates not allowed");
			});
			$http.delete('http://localhost:5000/saitodo/api/v1.0/tasks/undo').then(function(data){
					var hy = data.data;
					console.log(hy.jk);
					$scope.dn=hy.jk.length;
			})
};

$scope.dele = function(id, done){
	$http.delete('http://localhost:5000/saitodo/api/v1.0/tasks/'+id+'').then(function(data){
		var gn = data.data;
		console.log(gn);
		$scope.lists = gn.tasks;
	})
	$http.delete('http://localhost:5000/saitodo/api/v1.0/tasks/undo/'+id+'').then(function(data){
		var rn = data.data;
			console.log(rn.tk)
			$scope.dn = rn.tk.length;
	})
};

$scope.down=function(id1, index){
		if (index+1< $scope.lists.length)
		{
		var id2 = $scope.lists[index+1].id;
		$http.get('http://localhost:5000/saitodo/api/v1.0/tasks/'+id1+'/'+id2+'').then(function(data){
			var ng = data.data;
			console.log(ng.tasks);
			$scope.lists = ng.tasks;
		})
	}
	else{
		alert('cant mve');
	}
		};

$scope.up=function(id1, index){
		if (index>0)
		{
		var id2 = $scope.lists[index-1].id;
		$http.get('http://localhost:5000/saitodo/api/v1.0/tasks/'+id1+'/'+id2+'').then(function(data){
			var ng = data.data;
			console.log(ng.tasks);
			$scope.lists = ng.tasks;
		})
	}
	else{
		alert('cant mve');
	}				

		};

$scope.multdel = function(){
	$http.delete('http://localhost:5000/saitodo/api/v1.0/tasks/muldelet').then(function(data){
		var hk = data.data;
		console.log(hk.tasks);
		$scope.lists = hk.tasks; 
	})

	$http.delete('http://localhost:5000/saitodo/api/v1.0/tasks/undo').then(function(data){
		var h = data.data;
		console.log(h.jk);
		$scope.dn=h.jk.length;
	})
}

$scope.delesel = function(id, done){
	if(done == true)
	{   
		$http.delete('http://localhost:5000/saitodo/api/v1.0/tasks/muldelet/'+id+'').then(function(data){
		var hn = data.data;
		console.log(hn.tsk);
		$scope.dn = hn.tsk.length;
		console.log($scope.dn);
			})
	}
	else if(done == false){
		$http.delete('http://localhost:5000/saitodo/api/v1.0/tasks/undo/'+id+'').then(function(data){
			var kn = data.data;
			console.log(kn.tk)
			$scope.dn = kn.tk.length;
		})
	}
	else{
		return;
	}
}
}])
