Spinner authors = (Spinner) findViewById(R.id.spinner);
mSpinnerAdapter = new ArrayAdapter<Author>(getApplicationContext(), 
                                           R.layout.spinner_item, 
                                           mAuthors);

authors.setAdapter(mSpinnerAdapter);