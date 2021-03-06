public class Author extends Model {

    protected CharField mName;
    protected CharField mSynonym;

    public Author() {
        mName = new CharField();
        mSynonym = new CharField();
    }

    @Override
    protected void migrate(Context context) {
        Migrator&lt;Author> migrator = new Migrator&lt;Author>(Author.class);

        // tell the name of the field and the type
        migrator.addField("mSynonym", new CharField());

        // tell androrm the old name of the model
        migrator.renameModel("Authro", Author.class);

        // roll out all migrations
        migrator.migrate(context);
    }

}