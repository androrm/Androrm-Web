Button saveBook = (Button) findViewById(R.id.save);
    saveBook.setOnClickListener(new OnClickListener() {
    
    @Override
    public void onClick(View v) {
        EditText title = (EditText) findViewById(R.id.title);
        String value = title.getText().toString();
        
        if(value.trim().equals("")) {
            showDialog(NO_TITLE);
        } else {
            if(mSelectedAuthor == null) {
                mSelectedAuthor = mSpinnerAdapter.getItem(0);
            }
            
            Book book = new Book();
            book.setTitle(value);
            book.setAuthor(mSelectedAuthor);
            book.save(getApplicationContext());
            
            resetForm();
        }
    }
});