from django.shortcuts import render
from .models import Comments
# Create your views here.

def index(request):
    latest_comments_list = Comments.objects.order_by("-published_date")
    context = {"latest_comments_list": latest_comments_list}
    return render(request, "anl_txts_dash/index.html", context)