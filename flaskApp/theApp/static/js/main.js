(function() {
  var Site = function(element) {
    this.$element = element;
    this.setup();
  };

  Site.prototype.setup = function() {
    this.$element.on("click", function() {
      $("[data-element='target']").toggle();
    });
  };

  Site.protocol.loadPhrases = function($target) {
    $.ajax({
      url: "/get_hot_phrases",
      success: function(data) {
        console.log(data);
      }
    });
  };

  window.Site = Site;
})(window);
