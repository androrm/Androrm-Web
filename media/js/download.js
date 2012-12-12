if(!window.Androrm) { var Androrm = {}; }
if(!Androrm.Urls) { Androrm.Urls = {}; }

(function() {

    $(document).observe("dom:loaded", function() {
        var tarDownload = $("btn-download-tar");

        if(tarDownload) {
            tarDownload.observe("click", function() {
                window.location.href = Androrm.Urls.download_release_tar;
            });
        }

        var zipDownload = $("btn-download-zip");

        if(zipDownload) {
            zipDownload.observe("click", function() {
                window.location.href = Androrm.Urls.download_release_zip;
            });
        }

        var sourceDownload = $("btn-download-source");

        if(sourceDownload) {
            sourceDownload.observe("click", function() {
                window.location.href = Androrm.Urls.download_source;
            });
        }

    });

}());