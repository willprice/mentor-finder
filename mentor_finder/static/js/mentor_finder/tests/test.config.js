require.config({
  // ...paths and stuff
});

require([
  'test_app'
], function() {
  // INITIALIZE THE RUN
  if (window.mochaPhantomJS) { mochaPhantomJS.run(); }
  else { mocha.run(); }
});
