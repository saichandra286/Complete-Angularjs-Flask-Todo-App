angular.module('tododirectives', ['ngAnimate'])
.directive('todoform', function(){
		return {
			restrict: 'E',
			templateUrl:'static/partials/todoform.html'
		};
	})

.directive('todoview', function(){
	return {
		restrict: 'E',
		templateUrl: 'static/partials/todoview.html'
	}
})
