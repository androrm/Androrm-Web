List&lt;String&gt; values = Arrays.asList(new String[] {
		"Awesome book",
		"The boring book"
});

Filter filter = new Filter();
filter.in("mTitle", values);

QuerySet&lt;Book&gt; books = Book.objects(getApplicationContext()).filter(filter);