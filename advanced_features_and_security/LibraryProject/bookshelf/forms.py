from django import forms
from .models import Article
import re

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'maxlength': 200}),
            'content': forms.Textarea(attrs={'rows': 5}),
        }

    def clean_title(self):
        """
        Additional sanitization for title:
        - Trim whitespace
        - Optionally forbid certain dangerous patterns
        """
        title = self.cleaned_data.get('title', '').strip()

        # Example: forbid script tags in the title
        if re.search(r'<script.*?>', title, re.IGNORECASE):
            raise forms.ValidationError("Invalid characters detected in title.")

        return title

    def clean_content(self):
        """
        Optional: You can sanitize or validate content as needed.
        For rich text, use a sanitizer like 'bleach' to strip unsafe HTML.
        """
        content = self.cleaned_data.get('content', '').strip()

        # Example check: block <script> tags in content too
        if re.search(r'<script.*?>', content, re.IGNORECASE):
            raise forms.ValidationError("Content contains unsafe HTML.")

        return content
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()