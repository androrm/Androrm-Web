// Foo inherits from Model and can be serialized
public class Foo extends Model {
    
    // initializes the standard ID field
    // and sets it to autoincrement
    public Foo() {
        super();
    }
    
}

Foo foo = new Foo();

// foo is saved to the database and a
// id is automatically created
foo.save(getApplicationContext());