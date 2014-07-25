define(function(require) {
    var cases = require('cases')

    suite('age validation', function () {
        var MILLISECONDS_IN_A_YEAR = 1000 * 60 * 60 * 24 * 365.25
        var AgeValidator = require('../lib/age_validator')

        test('is date over 18', function () {
            var birthday = new Date(1900, 1, 1)
            assert.equal(true, new AgeValidator(birthday).is_over_18())
        })

        test('is date under 18', function () {
            assert.equal(false, new AgeValidator(new Date(Date.now())).is_over_18())
        })

        test('is date under 18', function () {
            assert.equal(false, new AgeValidator(new Date(Date.now() - ((MILLISECONDS_IN_A_YEAR * 18) - 100))).is_over_18())
        })

        test('is date over 18', function () {
            assert.equal(true, new AgeValidator(new Date(Date.now() - ((MILLISECONDS_IN_A_YEAR * 18) + 100))).is_over_18())
        })
    })
})
