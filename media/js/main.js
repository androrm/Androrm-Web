$(document).observe("dom:loaded", function() {

    $("button-latest-release").observe("click", function() {
        
        Androrm.Utils.go("/downloads/latest/");
        
    });
 
});