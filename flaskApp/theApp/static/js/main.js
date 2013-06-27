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
        var content = _.template("<div class='tab-pane' id='<%= phrase_id %>'><p><a href='<%= story_link %>'><%= title %></a></p><ul class='song_list'></ul></div>");
        var song_list = _.template("<li><a href='http://www.youtube.com/results?search_query=<%= song %>'><%= song %></a></li>");

        _.each(JSON.parse(data), function(result) {
			if(result.titles.length>0){

	          $target.find('ul.nav-tabs').append(template(result));
	          $target.find('div.tab-content').append(content({phrase_id:result.phrase_id, story_link:result.top_link.aggregate_url, title:result.titles[0]}));
	
	          _.each(result.songs, function(s) {
	            $target.find('div.tab-content #' + result.phrase_id + ' ul').append(
	              song_list({ song: s.title })
	            );
	          });
          }
        });
        /*var template = _.template("<li><a href='#<%= phrase_id %>' data-toggle='tab'><%= phrase %></a></li>");
        var content = _.template("<div class='tab-pane' id='<%= phrase_id %>'><ul class='titles'></ul></div>");
        var title = _.template("<li><a href='http://www.youtube.com/results?search_query=<%= title %>'><%= title %></a></li>");

        _.each(JSON.parse(data), function(result) {
			console.log(result);

          $target.find('ul.nav-tabs').append(template(result));
          $target.find('div.tab-content').append(content(result));

          _.each(result.titles, function(t) {
            $target.find('div.tab-content #' + result.phrase_id + ' ul').append(
              title({ title: t })
            );
          });
        });*/

        $('[data-toggle="tab"]:first').click();
      }
    });
  };

  window.Site = Site;
})(window);
