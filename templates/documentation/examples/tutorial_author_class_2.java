public class Author extends Model {
    
    public static final QuerySet&lt;Author&gt; objects(Context context) {
        return objects(context, Author.class);
    }
    
    protected CharField mName;
    
    public Author() {
        super();
        
        mName = new CharField(80);
    }
    
}