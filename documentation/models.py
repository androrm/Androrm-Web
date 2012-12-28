from django.db import models

from androrm.page.models import Category
from androrm.downloads.models import Release


class Description(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    from_version = models.ForeignKey(Release,
                                     blank=True,
                                     null=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class ClassDescription(Description):
    functions = models.ManyToManyField("FunctionDescription")
    category = models.ForeignKey(Category)
    is_data_field = models.BooleanField()
    is_field = models.BooleanField()
    descriptors = models.ManyToManyField("TypeDescriptor",
                                         through="ClassDescriptor",
                                         blank=True)

    def __unicode__(self):
        if self.descriptors.count():
            d = []

            for descriptor in self.descriptors.all():
                d.append(str(descriptor))

            return self.name + "<" + ", ".join(d) + ">"

        return self.name

    def qualified_name(self):
        return self.__unicode__()

    class Meta:
        ordering = ["name"]


class FunctionDescription(Description):
    is_constructor = models.BooleanField()
    params = models.ManyToManyField("ParamDescription",
                                    through="Param",
                                    blank=True,
                                    null=True)
    descriptors = models.ManyToManyField("TypeDescriptor",
                                         through="FunctionDescriptor",
                                         blank=True)
    returns = models.ForeignKey("Type",
                                blank=True,
                                null=True)

    class Meta:
        ordering = ["-is_constructor", "name"]

    def __unicode__(self):
        d = []

        for descriptor in self.descriptors.all():
            d.append(str(descriptor))

        descriptor_list = "<" + ", ".join(d) + ">" if d else ""

        p = []

        for param in self.params.all():
            p.append(str(param))

        param_list = "(" + ", ".join(p) + ")"

        return self.name + descriptor_list + " " + param_list

    def params_short(self):
        types = []

        for p in self.params.all():
            types.append(str(p.type))

        return "(" + ", ".join(types) + ")"


class ClassDescriptor(models.Model):
    clazz = models.ForeignKey("ClassDescription")
    descriptor = models.ForeignKey("TypeDescriptor")
    position = models.IntegerField()


class FunctionDescriptor(models.Model):
    function = models.ForeignKey("FunctionDescription")
    descriptor = models.ForeignKey("TypeDescriptor")
    position = models.IntegerField()


class Param(models.Model):
    param = models.ForeignKey("ParamDescription")
    function = models.ForeignKey("FunctionDescription")
    position = models.IntegerField()

    class Meta:
        ordering = ["position"]


class ParamDescription(Description):
    type = models.ForeignKey("Type")

    class Meta:
        ordering = ["param__position"]

    def __unicode__(self):
        return str(self.type) + " " + self.name


class Type(models.Model):
    name = models.CharField(max_length=80)
    descriptors = models.ManyToManyField("TypeDescriptor",
                                         null=True,
                                         blank=True)

    def __unicode__(self):
        if self.descriptors.count():
            d = []

            for descriptor in self.descriptors.all():
                d.append(str(descriptor))

            return self.name + "<" + ", ".join(d) + ">"

        return self.name

    class Meta:
        ordering = ["name"]


class TypeDescriptor(models.Model):
    name = models.CharField(max_length=80)
    extends = models.CharField(max_length=80,
                               blank=True,
                               null=True)

    def __unicode__(self):
        if self.extends:
            return self.name + " extends " + self.extends

        return self.name

    class Meta:
        ordering = ["name"]
