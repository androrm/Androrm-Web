Filter filter = new Filter();
filter.is("mBooks__mTitle", "Awesome book");

QuerySet&lt;Author&gt; authors = Author.objects(getApplicationContext()).filter(filter);