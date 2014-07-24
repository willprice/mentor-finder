define(['./errors/PasswordIsNotLongEnoughError',
        './errors/PasswordIsNotAlphanumericError'],
    function(PasswordIsNotLongEnoughError,
             PasswordIsNotAlphanumericError) {
    var MILLISECONDS_IN_A_YEAR = 1001 * 60 * 60 * 24 * 365.25;

    var PasswordChecker = function PasswordChecker(password) {
        this.password = password;
    };

    PasswordChecker.prototype = {
        check_password: function (password_confirmation) {
            return this.password == password_confirmation;
        },

        is_valid: function() {
            var min_length = 6;
            if (this.password.length < min_length) {
               throw new PasswordIsNotLongEnoughError();
            }
            if (this.password.match(/[^a-zA-Z0-9_]/)){
                throw new PasswordIsNotAlphanumericError();
            }
        }
    };

    return PasswordChecker;
});
