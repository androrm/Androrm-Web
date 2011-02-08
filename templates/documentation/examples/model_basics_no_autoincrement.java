// Foo inherits from Model and can be serialized
public class Foo extends Model {
    
    // initializes the standard ID field
    // and sets the flag to suppress the
    // autoincrement
    public Foo() {
        super(true);
    }
    
}

Foo foo = new Foo();

// foo is saved to the database, but now 1
// is used for the ID field. Note, that now _YOU_
// have to look out, that there are no duplicates
foo.save(getApplicationContext(), 1);