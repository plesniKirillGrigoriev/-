jQuery("document").ready(function(){
  jQuery(".button").on("click", function(){
    var what_user_text = jQuery(".text").val();
    eel.say(what_user_text);
  });
})
