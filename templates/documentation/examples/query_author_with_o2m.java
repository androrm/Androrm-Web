public class Author extends Model {
	
	public static final QuerySet&lt;Author&gt; objects(Context context) {
		return objects(context, Author.class);
	}
	
	protected CharField mName;
	protected OneToManyField&lt;Author, Book&gt; mBooks;
	
	public Author() {
		super();
		
		mName = new CharField(80);
		mBooks = new OneToManyField&lt;Author, Book&gt;(Author.class, Book.class);
	}
}