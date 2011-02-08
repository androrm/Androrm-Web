if(!Androrm) { var Androrm = {}; }
if(!Androrm.Urls) { Androrm.Urls = {}; }

new function() {
    
    $(document).observe("dom:loaded", function() {
        $("btn-download").observe("click", function() {
            window.location.href = Androrm.Urls.download_release;
        });
    });
    
}();