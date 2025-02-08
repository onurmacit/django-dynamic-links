from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Item

def item_redirect_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
    app_scheme_url = f"myapp://item_detail/{item_id}"

    if 'iphone' in user_agent or 'ipad' in user_agent:
        fallback_url = "https://apps.apple.com/app/my-app-id"
    elif 'android' in user_agent:
        fallback_url = "https://play.google.com/store/apps/details?id=com.myapp"
    else:
        fallback_url = request.build_absolute_uri(reverse('item_detail', args=[item_id]))

    return render(request, 'redirect.html', {
        'app_scheme_url': app_scheme_url,
        'fallback_url': fallback_url,
    })