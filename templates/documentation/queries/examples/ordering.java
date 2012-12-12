// Class definition for author with method to retrieve books
public class Author extends Model {
    
    public static final QuerySet&lt;Author&gt objects(Context context) {
        return objects(context, Author.class);
    }
    
    protected OneToManyField&lt;Author, Book&gt; mBooks;
    
    public Author() {
        mBooks = new OneToManyField&lt;Author, Book&gt;(Author.class, Book.class);
    }
    
    public QuerySet&lt;Book&gt; getBooks(Context context) {
        return mBooks.get(context, this);
    }
    
}

// get a context instance
Context context = getApplicationContext();

// Get the author with id = 1
Author author = Author.objects(context).get(1);

// Querying for books
QuerySet&lt;Book&gt; books = author.getBooks(context).all().orderBy("-mTitle");

for(Book book : books) {
    ...
}