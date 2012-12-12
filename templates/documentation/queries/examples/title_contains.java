Filter filter = new Filter();
filter.contains("mTitle", "some book");

QuerySet&lt;Book&gt; books = Book.objects(getApplicationContext()).filter(filter);