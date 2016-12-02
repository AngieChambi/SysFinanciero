app
	.factory("API", function($resource, config_auths){
		var url = config_auths.financieroUrl;
		console.log("*************** " +url);
		return{
			
	        Agencia: $resource(url + "agencias/:id/", { 'id': '@id' }, {
	            "update": { method: 'PUT' },
	            "list": { method: 'GET', isArray: true }
	        }),
	        Ahorro: $resource(url + "ahorros/:id/", { 'id': '@id' }, {
	            "update": { method: 'PUT' },
	            "list": { method: 'GET', isArray: true }
            }),

	        Cargo: $resource(url + "cargos/:id/", { 'id': '@id' }, {
	            "update": { method: 'PUT' },
	            "list": { method: 'GET', isArray: true }
            }),
            
            Empleado: $resource(url + "empleados/:id/", { 'id': '@id' }, {
	            "update": { method: 'PUT' },
	            "list": { method: 'GET', isArray: true }
	        }), 
	        Persona: $resource(url + "personas/:id/", { 'id': '@id' }, {
	            "update": { method: 'PUT' },
	            "list": { method: 'GET', isArray: true }
	        }), 
		};
	});
