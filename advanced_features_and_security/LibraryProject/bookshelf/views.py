from django.shortcuts import render

# advanced_features_and_security/your_app/views.py

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm  # You can create a basic ModelForm

# View an article (requires 'can_view' permission)
@permission_required('your_app.can_view', raise_exception=True)
def view_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'your_app/view_article.html', {'article': article})

# Create an article (requires 'can_create' permission)
@permission_required('your_app.can_create', raise_exception=True)
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'your_app/create_article.html', {'form': form})

# Edit an article (requires 'can_edit' permission)
@permission_required('your_app.can_edit', raise_exception=True)
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'your_app/edit_article.html', {'form': form, 'article': article})

# Delete an article (requires 'can_delete' permission)
@permission_required('your_app.can_delete', raise_exception=True)
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'your_app/delete_article.html', {'article': article})

