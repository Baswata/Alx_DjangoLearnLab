from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Relationship app URLs (already present)
    path('', include('relationship_app.urls')),

    # Advanced features & security: your_app URLs
    path('articles/', include(('your_app.urls', 'your_app'), namespace='your_app')),
]
