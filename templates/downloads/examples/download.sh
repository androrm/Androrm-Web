wget http://www.androrm.com{% url 'downloads.views.download_latest_tar' %}
tar -xvzf androrm_{{ latest_version }}.tar.gz
cd androrm_{{ latest_version }}
mv androrm.jar /path/to/your/lib/folder