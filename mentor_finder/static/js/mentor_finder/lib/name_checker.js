define(['./errors/InvalidNameError'],
    function(InvalidNameError) {

        var NameChecker = function NameChecker(name) {
            this.name = name;
        };

        NameChecker.prototype = {
            is_valid: function() {
                if (this.name.match(/[^a-zA-Z]/)) {
                    throw new InvalidNameError()
                }
            }
        };

        return NameChecker;
    });
