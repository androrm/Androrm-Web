public class Authro extends Model {

    protected CharField mName;

    public Authro() {
        mName = new CharField();
    }

    @Override
    protected void migrate(Context context) {
        return;
    }

}