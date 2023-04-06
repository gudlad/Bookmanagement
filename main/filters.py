import django_filters
from django import forms
from .models import Books
from django_filters import CharFilter, DateFilter


class BooksFilter(django_filters.FilterSet):
    """Books filter that enables filtering of Books with the title,
    author, language and publication date range parameters.
    """
    title = CharFilter(
        field_name="title",
        lookup_expr="contains",
        label="Title",
        widget=forms. TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Searched title...",
                "style": "text-align:left;",
            }
        ),
    )

    author = CharFilter(
        field_name="author",
        lookup_expr="contains",
        label="Author",
        widget=forms. TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Author sought...",
                "style": "text-align:left;",
            }
        ),
    )

    language = CharFilter(
        field_name="language",
        lookup_expr="contains",
        label="Language",
        widget=forms. TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Searched language...",
                "style": "text-align:left;",
            }
        ),
    )

    start_date = DateFilter(
        field_name="publication_date",
        lookup_expr="gte",
        label="Date from",
        widget=forms. DateInput(
            attrs={
                "class": "form-control",
                "placeholder": "YYYY-MM-DD",
                "style": "text-align:left;",
            }
        ),
    )



    end_date = DateFilter(
        field_name="publication_date",
        lookup_expr="lte",
        label="Date to",
        widget=forms. DateInput(
            attrs={
                "class": "form-control",
                "placeholder": "YYYY-MM-DD",
                "style": "text-align:left;",
            }
        ),
    )

    class Meta:
        model = Books
        fields = []
