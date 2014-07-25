define(function() {
    var MILLISECONDS_IN_A_YEAR = 1000 * 60 * 60 * 24 * 365.25
    AgeValidator = function AgeValidator(age) {
        this.age = age
    }

    AgeValidator.prototype = {
        is_over_18: function() {
            var date_of_18th_birthday = (this.age.getTime() + MILLISECONDS_IN_A_YEAR * 18)
            return Date.now() > date_of_18th_birthday
        }
    }

    return AgeValidator
})
