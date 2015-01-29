from django.db import models

class Order(models.Model):
	ORDER_STATUS = (
		('DO', 'В обработке'),
		('OK', 'Выполнена')
	)
	address = models.CharField('Адрес', max_length=255)
	name = models.CharField('Имя', max_length=255)
	phone = models.CharField('Телефон', max_length=16)
	status = models.CharField('Статус заявки', max_length=2, choices=ORDER_STATUS)
	breaking_type = models.CharField('Тип поломки', max_length=255)
	date_added = models.DateTimeField('Время и дата создания заявки')
	date_end = models.DateTimeField('Время и дата выполнения заявки', blank=True, null=True)

	class Meta:
		verbose_name = 'заявка'
		verbose_name_plural = 'Заявки'

	def __str__(self):
		return self.address


class Cost(models.Model):
	title = models.CharField('Цель расходов', max_length=255)
	total_price = models.DecimalField('Общая стоимость (грн)', max_digits=19, decimal_places=2)
	order_no = models.ForeignKey(Order, verbose_name='Расходы по заявке')

	class Meta:
		verbose_name = 'расходы'
		verbose_name_plural = 'Расходы'

	def __str__(self):
		return self.title

	def order_link(self):
		return '<a href="/admin/service/order/%s">%s</a>' % (self.order_no.id, self.order_no.address)
	order_link.allow_tags = True
	order_link.short_description = 'Расходы по заявке'