if(!Androrm) { var Androrm = {}; }
if(!Androrm.Initialize) { Androrm.Initializer = {}; }

new function() {
    
    Androrm.Initializer = Class.create({
        
        menu: undefined,
        
        initialize: function() {
            $(document).observe("dom:loaded", function() {
                this.initialize_menu();
            }.bind(this));
        },
        
        initialize_menu: function() {
            this.menu = new Androrm.Menu({
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
    
    new Androrm.Initializer();
    
}();