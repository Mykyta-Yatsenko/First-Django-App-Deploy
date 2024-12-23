from django.shortcuts import render

# Create your views here.
def get_date(request):
    # Create a simple html page as a string
    today = date.today()
    template = "<html>" \
                "Today's date is {}" \
               "</html>".format(today)
    # Return the template as content argument in HTTP response
    return HttpResponse(content=template)
