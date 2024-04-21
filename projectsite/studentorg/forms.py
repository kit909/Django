from django.forms import ModelForm
from django import forms
from .models import Organization, OrgMember


class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"

class MemberForm(ModelForm):
    class Meta:
        model = OrgMember
        fields = "__all__"
        