from django.contrib import admin
from main.models import Desination,Hotel,Package,Tour, Activity,EmailTemplate,Addon,TourSchedule

# Register your models here.
admin.site.register(Desination)
admin.site.register(Hotel)
admin.site.register(Activity)
admin.site.register(Tour)
admin.site.register(Package)
admin.site.register(EmailTemplate)
admin.site.register(Addon)
admin.site.register(TourSchedule)

