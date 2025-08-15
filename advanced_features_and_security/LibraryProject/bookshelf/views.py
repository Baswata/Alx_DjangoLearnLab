from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from .models import Article
from .forms import ArticleForm
from .forms import ExampleForm


# View an article (requires 'can_view' permission)
@permission_required('your_app.can_view', raise_exception=True)
@require_http_methods(["GET"])
def view_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'your_app/view_article.html', {'article': article})

# Create an article (requires 'can_create' permission)
@permission_required('your_app.can_create', raise_exception=True)
@require_http_methods(["GET", "POST"])
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Article created successfully.")
            return redirect('article_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ArticleForm()

    return render(request, 'your_app/create_article.html', {'form': form})

# Edit an article (requires 'can_edit' permission)
@permission_required('your_app.can_edit', raise_exception=True)
@require_http_methods(["GET", "POST"])
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "Article updated successfully.")
            return redirect('article_detail', pk=article.pk)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ArticleForm(instance=article)

    return render(request, 'your_app/edit_article.html', {'form': form, 'article': article})

# Delete an article (requires 'can_delete' permission)
@permission_required('your_app.can_delete', raise_exception=True)
@require_http_methods(["GET", "POST"])
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        messages.success(request, "Article deleted successfully.")
        return redirect('article_list')

    return render(request, 'your_app/delete_article.html', {'article': article})
