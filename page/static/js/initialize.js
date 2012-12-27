if(!Androrm) { var Androrm = {}; }

(function() {
    
    Androrm.Initializer = Class.create({
        
        initialize: function() {
            this.deactivateInactiveItems();
            this.enableButtons();
        },

        enableButtons: function() {
            $$("button.btn-latest-release").each(function(btn) {
                $(btn).observe("click", function() {
                
                    Androrm.Utils.go("/downloads/latest/");
                });
            });
        },
        
        deactivateInactiveItems: function() {
            $A($(document).getElementsByClassName("inactive")).each(function(el) {
                $A(el.getElementsByTagName("a")).each(function(a) {
                    a.observe("click", function(e) {
                        e.stop();
                        return false;
                    });
                });
            });
        }
    });
    
}());