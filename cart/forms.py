from django import forms

choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
    )


class QuantityForm(forms.Form):
        product_id = forms.IntegerField()
        quantity = forms.ChoiceField(choices=choices)

