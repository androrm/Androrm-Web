Filter filter = new Filter();
filter.is("mBooks__mTitle", "Awesome book");

QuerySet&lt;Author&gt; books = Author.objects(getApplicationContext()).filter(filter);