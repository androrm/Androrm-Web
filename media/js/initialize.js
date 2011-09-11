if(!Androrm) { var Androrm = {}; }

(function() {
    
    Androrm.Initializer = Class.create({
        
        initialize: function() {
            this.initializeMenu();
            this.deactivateInactiveItems();
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
        },
        
        initializeMenu: function() {
            new Androrm.Menu({
                node: $("menu"),
                items: [
                    {
                        name: "Home",
                        cls: "menu-item",
                        click: function() {
                            Androrm.Utils.go(Androrm.Urls.home);
                        }
                    },
                    {
                        name: "Documentation", 
                        cls: "menu-item",
                        click: function() {
                            Androrm.Utils.go(Androrm.Urls.documentation);
                        }
                    },
                    {
                        name: "Download",
                        cls: "menu-item",
                        click: function() {
                            Androrm.Utils.go(Androrm.Urls.download);
                        }
                    },
                    {
                        name: "Contribute",
                        cls: "menu-item",
                        click: function() {
                            Androrm.Utils.go(Androrm.Urls.contribute);
                        }
                    }
                ]
            })
        }
    });
    
}());