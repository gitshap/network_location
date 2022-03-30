from django.contrib import admin
from equipment.models import Building, Router, Office, Floor, Switch, Computer

admin.site.register(Router)

admin.site.register(Building)
admin.site.register(Office)
admin.site.register(Floor)
admin.site.register(Switch)
admin.site.register(Computer)

