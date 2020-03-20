from .models import TopAd, BottomAd


def ads_processor(request):
    context = {
        'top_ad': TopAd.objects.order_by('-id').all().first(),
        'bottom_ad': BottomAd.objects.order_by('-id').all()[:4]
    }

    return context
