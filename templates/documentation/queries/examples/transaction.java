Context ctx = getApplicationContext();

// Do _NOT_ instantiate with default constructor! Transactions only work if
// DatabaseAdapter is used as a singleton.
DatabaseAdapter adapter = DatabaseAdapter.getInstance(ctx);
adapter.beginTransaction();

Author brown = new Author();
brown.setName("Dan Brown");
brown.save(ctx);

Author grisham = new Author();
grisham.setName("John Grisham");
grisham.save(ctx);

adapter.commitTransaction();