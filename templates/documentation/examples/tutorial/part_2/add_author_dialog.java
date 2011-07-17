public class AddAuthorDialog extends Dialog {

    public AddAuthorDialog(Context context) {
        super(context);
        setContentView(R.layout.new_author_dialog);
        
        setTitle("Add a new author");
        
        registerOkButton();
        registerCancelButton();
    }
    
    private void registerOkButton() {
        final EditText name = (EditText) findViewById(R.id.name);
        Button ok = (Button) findViewById(R.id.button_ok);
        
        ok.setOnClickListener(new View.OnClickListener() {
            
            @Override
            public void onClick(View v) {
                String value = name.getText().toString();
                
                if(value.trim().equals("")) {
                    return;
                }
                
                Author author = new Author();
                author.setName(value);
                author.save(getContext());
                    
                AddBook activity = (AddBook) getOwnerActivity();
                activity.addAuthor(author);
                
                name.setText("");
                dismiss();
            }
        });
    }
    
    private void registerCancelButton() {
        Button cancel = (Button) findViewById(R.id.button_cancel);
        cancel.setOnClickListener(new View.OnClickListener() {
            
            @Override
            public void onClick(View v) {
                dismiss();
            }
        });
    }
    
}