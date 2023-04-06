from django import forms
from .models import Books


class BookHandler(forms.ModelForm):
    class Meta:
        model = Books
        fields = (
            "title",
            "author",
            "publication_date",
            "isbn",
            "page_count",
            "front_page_link",
            "language",
        )

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control mb-2", "placeholder": "Title..."}
            ),
            "author": forms.TextInput(
                attrs={"class": "form-control mb-2", "placeholder": "autor..."}
            ),
            "publication_date": forms.DateInput(
                attrs={"class": "form-control mb-2", "placeholder": "publication data..."}
            ),
            "isbn": forms.TextInput(
                attrs={"class": "form-control mb-2", "placeholder": "ISBN..."}
            ),
            "page_count": forms.NumberInput(
                attrs={"class": "form-control mb-2", "placeholder": "number of pages..."}
            ),
            "front_page_link": forms.TextInput(
                attrs={
                    "class": "form-control mb-2",
                    "placeholder": "link to the cover...",
                }
            ),
            "language": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "language of publication......",
                }
            ),
        }

        labels = {
            "title": "Title",
            "author": "Author",
            "publication_date": "Date of publication",
            "isbn": "ISBN",
            "page_count": "Number of pages",
            "front_page_link": "Link to the cover",
            "language": "Language",
        }

    def clean(self):
        cleaned_data = super().clean()
        author = cleaned_data.get("author")
        page_count = cleaned_data.get("page_count")
        validation_error_list = []
        if len(author) < 2:
            validation_error_list.append("au_short")
        if page_count < 0:
            validation_error_list.append("pc_small")
        if len(validation_error_list) > 0:
            raise forms.ValidationError(validation_error_list)


class ImportBooks(forms.Form):
    import_key_words = forms.CharField(
        label="Keywords",
        widget=forms. TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "The book you are looking for...",
                "style": "text-align:left;",
            }
        ),
    )
