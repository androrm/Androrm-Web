public class Author extends Model {
    
    protected CharField mName;
    
    public Author() {
        super();
        
        mName = new CharField(80);
    }
}

public class Book extends Model {
    
    public static final QuerySet&lt;Book&gt; objects(Context context) {
        return objects(context, Book.class);
    }
    
    protected CharField mTitle;
    protected ForeignKeyField&lt;Author&gt; mAuthor;
    
    public Book() {
        super();
        
        mTitle = new CharField(80);
        mAuthor = new ForeignKeyField&lt;Author&gt;(Author.class);
    }
}