List&lt;Class&lt;? extends Model&gt;&gt; models = new ArrayList&lt;Class&lt;? extends Model&gt;&gt;();
models.add(FirstModel.class);
models.add(SecondModel.class);

DatabaseAdapter adapter = DatabaseAdapter.getInstance(getApplicationContext());
adapter.setModels(models);