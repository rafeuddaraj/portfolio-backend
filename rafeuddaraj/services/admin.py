from django.contrib import admin
from .models import Services,Skills,Blog,Category,Client,ClientsReview,Comment,Package,Portfolio,Resume,Education
# Register your models here.

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name',)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('user',)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title',)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name',)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name',)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name',)
class ClientReviewAdmin(admin.ModelAdmin):
    list_display = ('clients',)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user',)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('name',)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree_name',)

admin.site.register(Blog,BlogAdmin)
admin.site.register(Portfolio,PortfolioAdmin)
admin.site.register(Resume,ResumeAdmin)
admin.site.register(Package,PackageAdmin)
admin.site.register(Client,ClientAdmin)
admin.site.register(ClientsReview,ClientReviewAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Services,ServicesAdmin)
admin.site.register(Education,EducationAdmin)
admin.site.register(Skills,SkillsAdmin)
