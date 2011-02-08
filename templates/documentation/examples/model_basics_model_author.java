public class Author extends Model {
    
    protected CharField mName;
    
    public Author() {
        super();
        
        mName = new CharField(80);
    }
    
}