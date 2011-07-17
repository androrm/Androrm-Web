Filter filter = new Filter();
filter.is("mAuthor__mName", "Dan Brown");

QuerySet&lt;Book&gt; books = Book.objects(getApplicationContext()).filter(filter);