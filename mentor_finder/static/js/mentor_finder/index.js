define(function(require) {
    var AgeValidator = require('./lib/age_validator')
    var $ = require('./bower_components/jquery/dist/jquery.min')
    console.log("Running FOOL!")

    window.onload = function () {
        wire_up_form_validation()
        var form = document.getElementById("register-mentor")
        for (element in document.getElementsByTagName("input")) {
            element.onblur = function() { form.checkValidity() }
        }
    }

    function wire_up_form_validation() {
        wire_up_password_validation()
        wire_up_date_of_birth_validation()
    }

    function wire_up_password_validation() {
        document.getElementById("password").onblur = validatePassword
        document.getElementById("password_conf").onblur = validatePassword
    }

    function wire_up_date_of_birth_validation() {
        document.getElementById("date_of_birth").onblur = validateDateOfBirth
    }


    function validatePassword() {
        var password = document.getElementById("password").value
        var password_confirmation = document.getElementById("password_conf").value

        if (password != password_confirmation) {
            document.getElementById("password").setCustomValidity("Passwords Don't Match")
            document.getElementById("password_conf").setCustomValidity("Passwords Don't Match")
        } else {
            //empty string means no validation error
            document.getElementById("password_conf").setCustomValidity('')
            document.getElementById("password").setCustomValidity('')
        }
    }

    function validateDateOfBirth() {
        var email = document.getElementById("date_of_birth")
    }
})
