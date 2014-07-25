define(function(require) {
    var cases = require('cases')

    suite('password validation', function () {
        var PasswordValidator = require('../lib/password_checker')
        var PasswordIsNotLongEnoughError = require('../lib/errors/PasswordIsNotLongEnoughError')
        var PasswordIsNotAlphanumericError = require('../lib/errors/PasswordIsNotAlphanumericError')

        test('password and confirmation match', function () {
            var password_checker = new PasswordValidator('apprentice')
            assert.equal(true, password_checker.check_password('apprentice'))
        })

        test('password and confirmation don\'t match', function () {
            var password_checker = new PasswordValidator('apprentice')
            assert.equal(false, password_checker.check_password('Apprentice'))
        })

        test('a password less than 6 characters is not valid', function () {
            var password_checker = new PasswordValidator('pass')
            assert.throw(password_checker.is_valid.bind(password_checker), PasswordIsNotLongEnoughError)
        })

        test('a password 6 characters long is valid', function () {
            var password_checker = new PasswordValidator('appren')
            assert.doesNotThrow(password_checker.is_valid.bind(password_checker), PasswordIsNotLongEnoughError)
        })

        suite('passwords with non-alphanumeric characters are not valid', function () {
            cases([
                    [ 'apprentice!' ],
                    [ 'apprentice#' ],
                    [ 'apprentice(' ]
                ], function (invalid_password) {
                    test(invalid_password, function () {
                        var password_checker = new PasswordValidator(invalid_password)
                        assert.throw(password_checker.is_valid.bind(password_checker), PasswordIsNotAlphanumericError)
                    })
                }
            )()
        })
    })
})
