define(function(require) {
  suite('Array', function(){
    setup(function(){
      // Do something 
    });

    suite('#indexOf()', function(){
      test('should return -1 when not present', function(){
        assert.equal(-1, [1,2,3].indexOf(4));
      });
    });
  });
});
