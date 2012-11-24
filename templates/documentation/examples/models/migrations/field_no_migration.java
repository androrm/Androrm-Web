public class Authro extends Model {

    protected CharField mName;
    protected CharField mSynonym;

    public Authro() {
        mName = new CharField();
        mSynonym = new CharField();
    }

    @Override
    protected void migrate(Context context) {
        return;
    }

}