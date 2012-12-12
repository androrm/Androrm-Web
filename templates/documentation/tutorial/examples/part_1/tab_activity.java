public class Tabs extends TabActivity {
    
    /** Called when the activity is first created. **/
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        
        // always call this before you do something else
        // in order to have the correct database layout
        syncDB();
        
        createTab(BrowseBooks.class, "Browse Books", R.drawable.tab_button);
        createTab(BrowseAuthors.class, "Browse Authors", R.drawable.tab_button);
        createTab(AddBook.class, "Add Book", R.drawable.tab_button);
        
        getTabHost().setCurrentTab(0);
    }
    
    /** Creates a new tab with the given activity class as content **/
    private void createTab(Class&lt;? extends Activity&gt; activity, 
            String tabAlias,
            int drawable) {
        
        Intent intent = new Intent().setClass(this, activity);
        
        Resources res = getResources();
        TabHost tabHost = getTabHost();
        
        TabHost.TabSpec spec = tabHost
            .newTabSpec(tabAlias.toLowerCase().replace(" ", "_"))   // this is optional
            .setIndicator(tabAlias, res.getDrawable(drawable))      // sets the drawable
            .setContent(intent);                                    // should be self-explaning
        
        tabHost.addTab(spec);
    }
    
    /** Will set up the database definition **/
    private void syncDB() {
        List&lt;Class&lt;? extends Model&gt;&gt; models = new ArrayList&lt;Class&lt;? extends Model&gt;&gt;();
        models.add(Author.class);
        models.add(Book.class);
        
        DatabaseAdapter.setDatabaseName("books_db");
        DatabaseAdapter adapter = new DatabaseAdapter(getApplicationContext());
        adapter.setModels(models);
    }
}