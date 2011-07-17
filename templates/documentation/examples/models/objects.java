class Book extends Model {
    
    public static final QuerySet&lt;Book&gt; objects(Context context) {
        return objects(context, Book.class);
    }
    
}