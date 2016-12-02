app
// gperfl routers
    .config(function($stateProvider, $urlRouterProvider){
    $stateProvider

        .state("financiero.agencia", {
            url:"/agencia",
            data: {section:'Financiero', page:'agencia'},
            templateUrl: "ioteca_web_apps/financiero/views/agencia/index.html"
        })
        .state("financiero.persona", {
            url:"/persona",
            data: {section:'Financiero', page:'persona'},
            templateUrl: "ioteca_web_apps/financiero/views/persona/index.html"
        })
        .state("financiero.socio", {
            url:"/socio",
            data: {section:'Financiero', page:'socio'},
            templateUrl: "ioteca_web_apps/financiero/views/socio/index.html"
        })
        .state("financiero.empleado", {
            url:"/empleado",
            data: {section:'Financiero', page:'empleado'},
            templateUrl: "ioteca_web_apps/financiero/views/empleado/index.html"
        })
        .state("financiero.ahorro", {
            url:"/ahorro",
            data: {section:'Financiero', page:'ahorro'},
            templateUrl: "ioteca_web_apps/financiero/views/ahorro/index.html"
        })
        .state("financiero.prestamo", {
            url:"/prestamo",
            data: {section:'Financiero', page:'prestamo'},
            templateUrl: "ioteca_web_apps/financiero/views/prestamo/index.html"
        });
    });
