<!--
.. title: django默认admin中Group添加选择User界面
.. slug: django-admin-group-user
.. date: 2013-07-28T13:46:42+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

django中的auth一般人都会用到不管是用他进入后台，还是自定义User model来实现用户管理，这都比必用的app，然后在使用中有一点很不方便，这两天研究了下，一般办法都是利用form解决的！但是苦于一直找不到想权限那样合适的控件！今天一个碰巧的情况解决了这些问题，不多说，重写groupadmin的form

~~~python
from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group,User

class GroupAdminForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all(),
                                           widget=FilteredSelectMultiple('Users', False),
                                           required=False)
    class Meta:
        model = Group
        
    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        if instance is not None:
            initial = kwargs.get('initial', {})
            initial['users'] = instance.user_set.all()
            kwargs['initial'] = initial
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        
    def save(self, commit=True):
        group = super(GroupAdminForm, self).save(commit=commit)
        
        if commit:
            group.user_set = self.cleaned_data['users']
        else:
            old_save_m2m = self.save_m2m
            def new_save_m2m():
                old_save_m2m()
                group.user_set = self.cleaned_data['users']
            self.save_m2m = new_save_m2m
        return group

class MyGroupAdmin(GroupAdmin):
    form = GroupAdminForm

admin.site.unregister(Group)
admin.site.register(Group, MyGroupAdmin)

~~~