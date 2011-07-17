public class Book extends Model {
    
    // fields visibility is set to protected,
    // so the Model class can access it
    protected CharField mTitle;
    
    // zero-argument constructor, that can be called 
    // by androrm, to gather field information
    public Book() {
        super();
        
        // set up field with maxLength parameter
        mTitle = new CharField(80);
    }
    
}