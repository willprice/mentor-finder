define(function(require) {
    var cases = require('cases')

    suite('name validation', function () {
        var NameValidator = require('../lib/name_checker')
        var InvalidNameError = require('../lib/errors/InvalidNameError')
        suite('names that aren\'t alphabetic are not valid', function() {
            cases([
                ['Jason$'],
                ['('],
                ['ajkshdf"£']
            ], function(invalid_name) {
                test(invalid_name, function() {
                    var name_checker = new NameValidator(invalid_name)
                    assert.throw(name_checker.is_valid.bind(name_checker), InvalidNameError)
                })
            })()
        })

        suite('names that are alphabetic are valid', function() {
            cases([
                ['John'],
                ['James'],
                ['Will']
            ], function(valid_name) {
                test(valid_name, function() {
                    var name_checker = new NameValidator(valid_name)
                    assert.doesNotThrow(name_checker.is_valid.bind(name_checker), InvalidNameError)
                })
            })()
        })
    })

})
