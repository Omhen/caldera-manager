// Filename: pending_user.js

define([
    'jquery',
    'underscore',
    'backbone',
    'models/pending_user'
], function($, _, Backbone, PendingUserModel){
    var PendingUserView = Backbone.View.extend({
	el: $("#frm-createuser"),
	initialize: function(){
	    _.bindAll(this, 'render', 'createUser');
	    this.render({token: null, message: null});
	},

	events: {
	    "click #btn-createuser": "createUser"
	},

	render: function(context){
	    var templateElement = $("#template_create_user_messages");
	    var contentElement = $("#template_create_user_messages");
	    if (templateElement.length == 0 && contentElement.length == 0)
		return;
	    var template = _.template(contentElement.html());
	    var content = template(context)
	    $("#cu-returnmessage").html(content);		
	},
	
	createUser: function(){
	    var that = this;
	    var username = $("#cu-username").val();
	    var firstName = $("#cu-firstname").val();
	    var lastName = $("#cu-lastname").val();
	    var email = $("#cu-email").val();
	    
	    var pendingUser = new PendingUserModel();
	    var userDetails = {
		username: username,
		first_name: firstName,
		last_name: lastName,
		email: email
	    };
	    pendingUser.save(userDetails,{
		wait: true,
		success: function(userModel, response){
		    that.render(userModel.toJSON());
		},
		error: function(response){
		    alert("Error while attempting to create user");
		}
	    });
	}
    });

    var initialize = function(){
	var view = new PendingUserView;
    };


    return { initialize: initialize };
});
