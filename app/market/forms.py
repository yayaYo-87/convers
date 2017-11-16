from django import forms

from app.market.models import Goods


class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['related_goods'].queryset = Goods.objects.filter(category=self.instance.category)