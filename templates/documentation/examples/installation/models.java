List&lt;? extends Model&gt; models = new ArrayList&lt;? extends Model&gt;();
models.add(FirstModel.class);
models.add(SecondModel.class);

DatabaseAdapter adapter = new DatabaseAdapter(getApplicationContext());
adapter.setModels(models);