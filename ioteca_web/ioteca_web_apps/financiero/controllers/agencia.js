app
	.controller('AgenciaCtrl', function($scope, API, $state, $stateParams, $window, $mdDialog, toastr){
		var url = 'ioteca_web_apps/financiero/views/agencia';
        var params = {};
		params.page = $stateParams.page ? $stateParams.page : 1;
		params.page_size = 5;
		$scope.lista = [];
        $scope.agencia = {};
        
        $scope.list = function(params){
			API.Agencia.list(params).$promise.then(function(r){
				$scope.lista = r;
			}, function(err){
				console.log("Err" +err);
			});
		};
		$scope.list(params);

        $scope.new = function(evt) {
            $scope.agencia.id = null;
            $scope.agencia = {};
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
            $scope.agencia = d;
            $mdDialog.show({
                scope: $scope,
                templateUrl: url +'/form.html',
                parent: angular.element(document.body),
                clickOutsideToClose: false,
                preserveScope: true,
            }).then(function() {
                $scope.list(params);
                $scope.agencia = {};
            }, function() {});
        };

        //mdDialog
        $scope.cancel = function() {
            $mdDialog.cancel();
            $scope.list(params);
        };

        //============================================================
        //guardar las agencias
        //============================================================
        $scope.save = function(nombre) {
            if ($scope.agencia.id) {
                API.Agencia.update({ id: $scope.agencia.id }, $scope.agencia).$promise.then(function(r) {
                    toastr.success('El Agencia se Actualizo correctamente');
                    $mdDialog.hide();
                    $scope.list(params);
                }, function(err) {
                });

            } else {
                API.Agencia.save($scope.agencia).$promise.then(function(r) {
                    toastr.success('El Agencia se agrego correctamente');
                    $mdDialog.hide();
                    $scope.list(params);
                }, function(err) {
                });                
                // }
            }
        };

        $scope.delete = function(d) {
        var confirm = $mdDialog.confirm()
              .title('Desea Eliminar Agencia?')
              .textContent('Esta Agencia se eliminará y ya no podrás encontrarla')
              .ariaLabel('Lucky day')
              .targetEvent()
              .ok('SI')
              .cancel('NO');
        $mdDialog.show(confirm).then(function() {
                API.Agencia.delete({ id: d.id }).$promise.then(function(r) {
                    toastr.info('El Agencia se elimino correctamente');
                    $scope.list(params);
                }, function(err) {
                });
        }, function() {
        });
      };

});
