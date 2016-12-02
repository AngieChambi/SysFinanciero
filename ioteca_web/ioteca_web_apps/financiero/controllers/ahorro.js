app
	.controller('AhorroCtrl', function($scope, API, $state, $stateParams, $window, $mdDialog, toastr){
		var url = 'ioteca_web_apps/financiero/views/ahorro';
        var params = {};
		params.page = $stateParams.page ? $stateParams.page : 1;
		params.page_size = 5;
		$scope.lista = [];
        $scope.ahorro = {};
        
        $scope.list = function(params){
			API.Ahorro.list(params).$promise.then(function(r){
				$scope.lista = r;
			}, function(err){
				console.log("Err" +err);
			});
		};
		$scope.list(params);

        $scope.new = function(evt) {
            $scope.ahorro.id = null;
            $scope.ahorro = {};
            $mdDialog.show({
                scope: $scope,
                targetEvent: evt,
                templateUrl: url +'/form.html',
                parent: angular.element(document.body),
                clickOutsideToClose: false,
                preserveScope: true,
            }).then(function() {
                $scope.list(params);
            }, function() {});
        };

        //end mdDialog
        $scope.sel = function(d) {
            $scope.ahorro = d;
            $mdDialog.show({
                scope: $scope,
                templateUrl: url +'/form.html',
                parent: angular.element(document.body),
                clickOutsideToClose: false,
                preserveScope: true,
            }).then(function() {
                $scope.list(params);
                $scope.ahorro = {};
            }, function() {});
        };

        //mdDialog
        $scope.cancel = function() {
            $mdDialog.cancel();
            $scope.list(params);
        };

        //============================================================
        //guardar las ahorros
        //============================================================
        $scope.save = function(nombre) {
            if ($scope.ahorro.id) {
                API.Ahorro.update({ id: $scope.ahorro.id }, $scope.ahorro).$promise.then(function(r) {
                    toastr.success('El ahorro se Actualizo correctamente');
                    $mdDialog.hide();
                    $scope.list(params);
                }, function(err) {
                });

            } else {
                API.Ahorro.save($scope.ahorro).$promise.then(function(r) {
                    toastr.success('El ahorro se agrego correctamente');
                    $mdDialog.hide();
                    $scope.list(params);
                }, function(err) {
                });                
                // }
            }
        };

        $scope.delete = function(d) {
        var confirm = $mdDialog.confirm()
              .title('Desea Eliminar ahorro?')
              .textContent('Esta ahorro se eliminará y ya no podrás encontrarla')
              .ariaLabel('Lucky day')
              .targetEvent()
              .ok('SI')
              .cancel('NO');
        $mdDialog.show(confirm).then(function() {
                API.Ahorro.delete({ id: d.id }).$promise.then(function(r) {
                    toastr.info('El ahorro se elimino correctamente');
                    $scope.list(params);
                }, function(err) {
                });
        }, function() {
        });
      };

});