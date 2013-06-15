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

  Site.prototype.loadPhrases = function($target) {
    $.ajax({
      url: "/static/js/phrases.json",
      success: function(data) {
        var template = _.template("<li><a href='#<%= phrase_id %>' data-toggle='tab'><%= phrase %></a></li>");
        var content = _.template("<div class='tab-pane' id='<%= phrase_id %>'><ul class='titles'></ul></div>");
        var title = _.template("<li><a href='http://www.youtube.com/results?search_query=<%= title %>'><%= title %></a></li>");

        _.each(data, function(result) {
          $target.find('ul.nav-tabs').append(template(result));
          $target.find('div.tab-content').append(content(result));

          _.each(result.titles, function(t) {
            $target.find('div.tab-content #' + result.phrase_id + ' ul').append(
              title({ title: t })
            );
          });
        });

        $('[data-toggle="tab"]:first').click();
      }
    });
  };

  window.Site = Site;
})(window);
