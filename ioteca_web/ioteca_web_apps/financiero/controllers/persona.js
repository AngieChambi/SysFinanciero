app
	.controller('PersonaCtrl', function($scope, API, $state, $stateParams, $window, $mdDialog, toastr){
		var url = 'ioteca_web_apps/financiero/views/persona';
        var params = {};
		params.page = $stateParams.page ? $stateParams.page : 1;
		params.page_size = 5;
		$scope.lista = [];
        $scope.persona = {};
        
        $scope.list = function(params){
			API.Persona.list(params).$promise.then(function(r){
				$scope.lista = r;
			}, function(err){
				console.log("Err" +err);
			});
		};
		$scope.list(params);

        $scope.new = function(evt) {
            $scope.persona.id = null;
            $scope.persona = {};
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
            $scope.persona = d;
            $mdDialog.show({
                scope: $scope,
                templateUrl: url +'/form.html',
                parent: angular.element(document.body),
                clickOutsideToClose: false,
                preserveScope: true,
            }).then(function() {
                $scope.list(params);
                $scope.persona = {};
            }, function() {});
        };

        //mdDialog
        $scope.cancel = function() {
            $mdDialog.cancel();
            $scope.list(params);
        };

        //============================================================
        //guardar las personas
        //============================================================
        $scope.save = function(nombre) {
            if ($scope.persona.id) {
                API.Persona.update({ id: $scope.persona.id }, $scope.persona).$promise.then(function(r) {
                    toastr.success('El persona se Actualizo correctamente');
                    $mdDialog.hide();
                    $scope.list(params);
                }, function(err) {
                });

            } else {
                API.Persona.save($scope.persona).$promise.then(function(r) {
                    toastr.success('El persona se agrego correctamente');
                    $mdDialog.hide();
                    $scope.list(params);
                }, function(err) {
                });                
                // }
            }
        };

        $scope.delete = function(d) {
        var confirm = $mdDialog.confirm()
              .title('Desea Eliminar persona?')
              .textContent('Esta persona se eliminará y ya no podrás encontrarla')
              .ariaLabel('Lucky day')
              .targetEvent()
              .ok('SI')
              .cancel('NO');
        $mdDialog.show(confirm).then(function() {
                API.Persona.delete({ id: d.id }).$promise.then(function(r) {
                    toastr.info('El persona se elimino correctamente');
                    $scope.list(params);
                }, function(err) {
                });
        }, function() {
        });
      };

});
