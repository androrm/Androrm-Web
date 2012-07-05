public class Author {

    protected CharField mName;
    protected CharField mSynonym;

    public Author() {
        mName = new CharField();
        mSynonym = new CharField();
    }

    @Override
    protected void migrate(Context context) {
        return;
    }

}