from django.contrib import admin
from main.models import CbCategory,CbTag,CbTopic,CbTopicTags,CbQuestion,CbQuestionTag,CbCategoryTags
from django import forms
from main.forms import CbCategoryForm,CbTopicAdminForm,CbQuestionAdminForm
from ast import  literal_eval
from django.contrib.admin.actions import delete_selected as delete_selected_
from django.core.exceptions import PermissionDenied

# Register your models here.


class CbCategoryAdmin(admin.ModelAdmin):
    list_display = ("id","id","name","owner","created_at","owner","slug")
    search_fields = ("name",)
    form = CbCategoryForm

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == "description" or db_field.name == "meta_data":
            kwargs["widget"] = forms.Textarea
        if db_field.name == "owner":
            kwargs["initial"] = request.user
            kwargs["label"] = "Owner *"
        return super(CbCategoryAdmin,self).formfield_for_dbfield(db_field,request,**kwargs)

    def save_model(self, request, obj, form, change):
        super(CbCategoryAdmin, self).save_model(request, obj, form, change)
        if form.cleaned_data.get("tag"):
            obj.category_tags.all().delete()
            for tag in literal_eval(form.cleaned_data.get("tag")):
                CbCategoryTags.objects.create(
                    category=obj,
                    tag=CbTag.objects.get(pk=tag)
                )


    #
    # # def get_form(self, request, obj=None, **kwargs):
    # #     form = super(CbCategoryAdmin,self).get_form(request,obj,**kwargs)
    # #     form.owner = request.user
    # #     return form


class CbTagAdmin(admin.ModelAdmin):
    list_display = ("id","name","slug")


class CbCategoryTagsAdmin(admin.ModelAdmin):
    list_display = ("id","tag","category")


class CbTopicTagsAdmin(admin.ModelAdmin):
    list_display = ("id","tag","topic")


class CbQuestionTagsAdmin(admin.ModelAdmin):
    list_display = ("id","tag","question")
    search_fields = ("question",)


class CbTopicAdmin(admin.ModelAdmin):
    list_display = ("id","title","category","owner","slug")
    search_fields = ("title",)
    list_filter = ("category",)
    form = CbTopicAdminForm

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(CbTopicAdmin,self).get_form(request,obj,**kwargs)
    #     form.owner = request.user.id
    #     return form
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == "owner":
            kwargs["initial"] = request.user
            kwargs["label"] = "Owner *"
        if db_field.name == "category":
            kwargs["label"] = "Category *"
        return super(CbTopicAdmin,self).formfield_for_dbfield(db_field,request,**kwargs)

    def save_model(self, request, obj, form, change):
        super(CbTopicAdmin, self).save_model(request, obj, form, change)
        if form.cleaned_data.get("tag"):
            obj.topic_tags.all().delete()
            for tag in literal_eval(form.cleaned_data.get("tag")):
                CbTopicTags.objects.create(
                    topic=obj,
                    tag=CbTag.objects.get(pk=tag)
                )

def delete_selected(modeladmin, request, queryset):
    if not modeladmin.has_delete_permission(request):
        raise PermissionDenied
    if request.POST.get('post'):
            for obj in queryset:
                obj.is_deleted = True
                obj.save()
    else:
        return delete_selected_(modeladmin, request, queryset)

delete_selected.short_description = "Delete selected objects"


class CbQuestionAdmin(admin.ModelAdmin):
    form=CbQuestionAdminForm
    search_fields = ("title",)
    list_filter = ("topic","category")
    actions = [delete_selected]
    list_display = ("id","title","topic","owner","created_at","updated_at","category","is_deleted")

    def save_model(self, request, obj, form, change):
        super(CbQuestionAdmin, self).save_model(request, obj, form, change)
        if form.cleaned_data.get("tag"):
            obj.question_tags.all().delete()
            for tag in literal_eval(form.cleaned_data.get("tag")):
                CbQuestionTag.objects.create(
                    question=obj,
                    tag=CbTag.objects.get(pk=tag)
                )


    # def save_related(self, request, form, formsets, change):

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == "owner":
            kwargs["initial"] = request.user
            kwargs["label"] = "Owner *"
        return super(CbQuestionAdmin,self).formfield_for_dbfield(db_field,request,**kwargs)

    def delete_model(self, request, obj):
        obj.is_deleted = True
        obj.save()


    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(CbQuestionAdmin,self).get_form(request,obj,**kwargs)
    #     print(request,request.user.id)
    #     form.owner = request.user.id
    #     return form

    # def delete_selected(self):

admin.site.register(CbCategory,CbCategoryAdmin)
admin.site.register(CbTopic,CbTopicAdmin)
admin.site.register(CbTag,CbTagAdmin)
admin.site.register(CbQuestion,CbQuestionAdmin)
admin.site.register(CbTopicTags,CbTopicTagsAdmin)
admin.site.register(CbCategoryTags,CbCategoryTagsAdmin)
admin.site.register(CbQuestionTag,CbQuestionTagsAdmin)
