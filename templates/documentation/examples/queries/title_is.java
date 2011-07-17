Filter filter = new Filter();
filter.is("mTitle", "Awesome book");

QuerySet&lt;Book&gt; books = Book.objects(getApplicationContext()).filter(filter);