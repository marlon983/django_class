from django import forms
from .models import Kouka2

class Kouka2Form(forms.ModelForm):

    product = forms.CharField(label='商品名')

    area_list = [
        ('北海道', '北海道'),
        ('東北', '東北'),
        ('関東', '関東'),
        ('東海', '東海'),
        ('甲信越', '甲信越'),
        ('中部', '中部'),
        ('北陸', '北陸'),
        ('関西', '関西'),
        ('山陽', '山陽'),
        ('山陰', '山陰'),
        ('四国', '四国'),
        ('九州', '九州'),
        ('沖縄', '沖縄'),
    ]
    area = forms.ChoiceField(label='生産地', choices=area_list)

    delivery_list = [
        ('店舗', '店舗'),
        ('農協', '農協'),
        ('配送センター', '配送センター'),
        ('個人', '個人'),
    ]
    delivery = forms.ChoiceField(label='配送先', choices=delivery_list, widget=forms.RadioSelect())

    price = forms.IntegerField(label='価格')

    attachment_list = [
        ('生産者名', '生産者名'),
        ('栄養価', '栄養価'),
        ('使用農薬', '使用農薬'),
        ('効能', '効能'),
        ('関連商品', '関連商品'),
        ('問い合わせ先', '問い合わせ先'),
        ('その他', 'その他'),
    ]
    attachment = forms.MultipleChoiceField(label='添付情報', choices=attachment_list, widget=forms.SelectMultiple(attrs={'size':len(attachment_list)}))

    class Meta:
        model = Kouka2
        fields = ['product', 'area', 'delivery', 'price', 'attachment']

class FindKouka2(forms.Form):
    find = forms.CharField(label='検索語', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))