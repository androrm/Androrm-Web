from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext

from androrm.page.models import Category
from androrm.documentation.models import ClassDescription, FunctionDescription

def index(request):
    categories = []
    
    for category in Category.objects.filter(parent__name = "Documentation"):
        subcategories = []
        
        for subcategory in Category.objects.filter(parent__id = category.id):
            subcategories.append({"id": subcategory.id,
                                  "name": subcategory.name,
                                  "description": subcategory.description,
                                  "url": subcategory.get_url()})
        
        categories.append({"name": category.name,
                           "id": category.id,
                           "url": category.get_url(),
                           "description": category.description,
                           "subcategories": subcategories})
    
    return render_to_response('documentation/index.html', 
                              locals(), 
                              context_instance = RequestContext(request))
    
def category(request, id):
    return render_to_response('documentation/browse_category.html', 
                              locals(), 
                              context_instance = RequestContext(request))
                              
def models(request):
    categories = []
    
    
    for category in Category.objects.filter(parent__name__contains = "Defining Models"):
        categories.append({"name": category.name,
                           "id": category.id,
                           "url": category.url,
                           "description": category.description})
    
    return render_to_response('documentation/models.html',
                              locals(),
                              context_instance = RequestContext(request))
                              
def fields(request):
    data_fields = []
    relation_fields = []
    
    for field in ClassDescription.objects.filter(is_field = True):
        if field.is_data_field:
            data_fields.append({"name": field.name})
        else:
            relation_fields.append({"name": field.name})
    
    categories = [{"name": "Data Fields",
                   "description": Category.objects.filter(name = "Data Fields")[0].description,
                   "url": reverse('documentation_data_fields'),
                   "fields": data_fields},
                  {"name": "Relational Fields",
                  "description": Category.objects.filter(name = "Relational Fields")[0].description,
                   "url": reverse('documentation_relational_fields'),
                   "fields": relation_fields}]
    
    return render_to_response('documentation/fields.html',
                              locals(),
                              context_instance = RequestContext(request))
                              
def data_fields(request):
    fields = ClassDescription.objects.filter(is_field = True, is_data_field = True)
    relational_fields = ClassDescription.objects.filter(is_field = True, is_data_field = False)
    
    return render_to_response('documentation/data_fields.html',
                              locals(),
                              context_instance = RequestContext(request))
                              
def relational_fields(request):
    fields = ClassDescription.objects.filter(is_field = True, is_data_field = False)
    
    data_fields = ClassDescription.objects.filter(is_field = True, is_data_field = True)
    
    return render_to_response('documentation/relational_fields.html',
                              locals(),
                              context_instance = RequestContext(request))
                              
def queries(request):

    query_set = ClassDescription.objects.get(pk = 12)

    order_by = ClassDescription.objects.get(pk = 11)
    
    categories = Category.objects.filter(parent__name = "Making Queries")

    return render_to_response('documentation/queries.html',
                              locals(),
                              context_instance = RequestContext(request))

def beginners(request):
    categories = Category.objects.filter(parent__name = "Beginners")

    return render_to_response('documentation/beginners.html',
                              locals(),
                              context_instance = RequestContext(request))

def installation(request):
    categories = Category.objects.filter(parent__name = "Beginners")

    return render_to_response('documentation/installation.html',
                              locals(),
                              context_instance = RequestContext(request))
                              
def kick_start(request):
    return render_to_response('documentation/get_started.html',
                              locals(),
                              context_instance = RequestContext(request))
                              
def tutorials(request):
    return render_to_response('documentation/tutorials.html',
                              locals(),
                              context_instance = RequestContext(request))
                              
def tutorial(request, part):
    return render_to_response('documentation/tutorial_part_' + str(part) + '.html',
                              locals(),
                              context_instance = RequestContext(request))