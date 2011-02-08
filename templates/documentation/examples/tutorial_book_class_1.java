public class Book extends Model {
    
    protected CharField mTitle;
    protected ForeignKeyField&lt;Author&gt; mAuthor;
    
    public Book() {
        super();
        
        mTitle = new CharField(80);
        mAuthor = new ForeignKeyField&lt;Author&gt;(Author.class);
    }
    
}