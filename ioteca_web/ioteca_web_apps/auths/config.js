var baseUrl = 'http://localhost:9001';
var authsUrl = baseUrl+'/api/auths/';
var financieroUrl = baseUrl+'/api/financiero/';


var config = {
    
    authsUrl: authsUrl,
    financieroUrl: financieroUrl,


};

app

.value('config_auths', config);
