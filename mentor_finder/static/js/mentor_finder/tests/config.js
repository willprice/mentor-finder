require.config({
    paths: {
        async: "../node_modules/cases/node_modules/async/lib/async",
        cases: "../node_modules/cases/lib/cases"
    }
})

require([
    './test_name_validator',
    './test_age_validator',
    './test_password_validator',
], function initializeRun () {
    if (window.mochaPhantomJS) { mochaPhantomJS.run() }
    else { mocha.run() }
})
