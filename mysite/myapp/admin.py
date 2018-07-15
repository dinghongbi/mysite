from django.contrib import admin
from myapp.models import Publisher,Author,Book

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name','email')
	search_fields = ('first_name','last_name')

class BookAdmin(admin.ModelAdmin):
	list_display = ('title','publisher','publication_date')
	list_filter = ('publication_date',)#查询过滤条件
	date_hierarchy = 'publication_date'#根据年度查询
	ordering = ('-publication_date',)#排序
	# fields = ('title','authors','publisher')#编辑表单顺序，隐藏字段publication_date
	filter_horizontal = ('authors',)#十个以上选项的多对多字段使用filter_horizontal
	# filter_vertical = ('authors',)	#十个以上选项的多对多字段使用filter_vertical
	raw_id_fields = ('publisher',)#有下拉列表数千条记录时，列表字段将被展现成`` 文本框`` ，而不再是`` 下拉框`` 。
class PublisherAdmin(admin.ModelAdmin):
	list_display = ('name','address','city','state_province','country','website')



# Register your models here.
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
