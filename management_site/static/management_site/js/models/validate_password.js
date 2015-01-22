// Filename: validatE_password.js

define([
    'underscore',
    'backbone'
], function(_, Backbone){
    var ValidatePasswordModel = Backbone.Model.extend({
	urlRoot: '/auth/validatepassword/',
	defaults: {
	    token: "",
	    password: "",
	    confirm_password: ""
	}
    });
    
    return ValidatePasswordModel;
});
