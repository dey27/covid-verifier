import logging, os

from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.http import HttpResponse



def download_file(file_path):
    if file_path and os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/force-download")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    else:
        raise RuntimeError("File Path does not exist")


def save_file(file, in_folder):
    try:
        fs = FileSystemStorage(location=in_folder)
        filename = fs.save(file.name, file)
        filepath = in_folder + filename
        logging.info("File saved. Full path - {}" .format(filepath))
        return filepath
    except Exception as e:
        logging.error("File Saving Failed - {}".format(e))


def get_extension(filename):
    extension = os.path.splitext(filename)[1]
    return extension


def rename_file(filename):
    logging.info("File Renamed - {}".format(filename))
    return filename


def get_folder_location():
    location = settings.LOCATION
    logging.info("Folder Location - {}".format(location))
    return location


def delete_file(filepath):
    try:
        os.remove(filepath)
    except Exception as e:
        logging.error(e)


class FileView(APIView):
    """
    Usage - path('<str:sample>/', SampleView.as_view(), name='SampleView'),
    """
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    """
    Class to CRUD on files, given the filepath.
    Usage - path('download_file/', FileView.as_view(), name='FileView'),
    """
    def get(self, request):
        try:
            file_path = request.GET.get('filePath')
            return download_file(file_path)
        except Exception as e:
            raise RuntimeError(e)
