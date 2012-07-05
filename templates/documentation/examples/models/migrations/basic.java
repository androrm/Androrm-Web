public class Author extends Model {

    protected CharField mName;

    public Author() {
        mName = new CharField();
    }

    @Override
    protected void migrate(Context context) {
        return;
    }

}