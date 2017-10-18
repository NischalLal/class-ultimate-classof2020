from django.shortcuts import render, get_object_or_404, HttpResponse,\
                            HttpResponseRedirect
from django.urls import reverse
from downloads.models import DownloadItem
import os
from django.http import FileResponse
from django.utils.text import slugify
# Create your views here.

def download_item(request, id):
    item = get_object_or_404(DownloadItem, pk=id)
    file_name, file_extension = os.path.splitext(item.file.file.name)
    file_extension = file_extension[1:] # removes dot
    response = FileResponse(item.file.file, 
        content_type = "file/%s" % file_extension)
    response["Content-Disposition"] = "attachment;"\
        "filename=%s.%s" %(slugify(item.file.name)[:100], file_extension)
    return response


def download_list(request):
    all_downloads = DownloadItem.objects.all()
    context = {'all_downloads':all_downloads}
    template_name = 'downloads/list.html'
    return render(request, template_name, context)