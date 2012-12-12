public class Author extends Model {
    
    protected CharField mName;
    
    // implicit field, that uses the ForeignKey 
    // on the Book model
    protected OneToManyField&lt;Author, Book&gt; mBooks;
    
    public Author() {
        super();
        
        mName = new CharField(80);
        mBooks = new OneToManyField&lt;Author, Book&gt;(Author.class, Book.class);
    }
    
}