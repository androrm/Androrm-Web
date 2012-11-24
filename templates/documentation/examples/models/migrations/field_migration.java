public class Authro extends Model {

    protected CharField mName;
    protected CharField mSynonym;

    public Authro() {
        mName = new CharField();
        mSynonym = new CharField();
    }

    @Override
    protected void migrate(Context context) {
        Migrator&lt;Authro> migrator = new Migrator&lt;Authro>(Authro.class);

        // tell the name of the field an the type
        migrator.addField("mSynonym", new CharField());

        // roll out all migrations
        migrator.migrate(context);
    }

}