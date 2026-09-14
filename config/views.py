from django.http import HttpResponse
 def landing_page(request):
 	return HttpResponse("Django loyhasi")
#def landing_page(request):
 #   return HttpResponse(f"Django loyhasi: {request.META['HTTP_USER_AGENT']}")
