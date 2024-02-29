from django.shortcuts import render
from .models import Comments
# Create your views here.

def index(request):
    if request.method == "POST":

        search_text = request.POST.get('search_text')

        selected_sent = []
        if request.POST.get('toggle_pos_sent'):
            selected_sent.append("pos")
        if request.POST.get('toggle_neg_sent'):
            selected_sent.append("neg")

        latest_comments_list = latest_comments_list = Comments.objects.filter(
            comment__icontains=search_text,
            sentiment__in = selected_sent
        ).order_by('-published_date')
        
    else:
        latest_comments_list = Comments.objects.order_by("-published_date")
        
    context = {"latest_comments_list": latest_comments_list}
    return render(request, "anl_txts_dash/index.html", context)