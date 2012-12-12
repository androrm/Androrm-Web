Author author = new Author();
author.setName(value);
author.save(getContext());
    
AddBook activity = (AddBook) getOwnerActivity();
activity.addAuthor(author);