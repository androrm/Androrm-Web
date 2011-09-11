if(!Androrm) { var Androrm = {}; }

(function() {
    
    Androrm.Menu = Class.create({
        
        cls: undefined,
        node: undefined,
        items: [],
        
        initialize: function(config) {
            this.cls = config.cls || "";
            this.node = $(config.node);
            
            this.createItems(config.items || []);
            this.createNode();
        },
        
        createItems: function(itemConfig) {
            itemConfig.each(function(config) {
                this.createItem(config);
            }.bind(this));
        },
        
        createItem: function(config) {
            var item = new Element("div", {"class": config.cls || ""});
            
            item.insert(config.name || "");
            item.observe("click", config.click || Prototype.emptyFunction);
            item.observe("mouseover", this.select.bind(this, this.items.length));
            item.observe("mouseout", this.deselect.bind(this, this.items.length));
            
            this.items.push(item);
        },
        
        createNode: function() {
            this.items.each(function(item) {
                this.node.insert({bottom: item});
            }.bind(this));
        },
        
        select: function(index) {
            if(this.node.children[index]) {
                var item = this.node.children[index];
                var cls = item.readAttribute("class");
                
                item.writeAttribute("class", cls + " menu-item-selected")
            }
        },
        
        deselect: function(index) {
            if(this.node.children[index]) {
                var item = this.node.children[index];
                var cls = item.readAttribute("class");
                
                cls = cls.split(" ");
                cls = cls.slice(0, cls.length - 1).join(" ");
                
                item.writeAttribute("class", cls);
            }
        }
        
    });
}());