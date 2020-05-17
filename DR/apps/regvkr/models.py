from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
	first_name_S = models.CharField('Имя:', max_length=15)
	last_name_S = models.CharField('Фамилия:', max_length=25)
	num = models.PositiveIntegerField('Номер зачётной книжки:', unique=True)  # to confirm
	group = models.CharField('Группа:', max_length=8)
	user = models.OneToOneField(User)

	def __str__(self):
		template = '{0.last_name_S} {0.first_name_S} {0.group}'
		return template.format(self)

	class Meta(object):
		ordering = ['last_name_S']
		verbose_name = 'Студент'
		verbose_name_plural = 'Студенты'


class ScientificDirector(models.Model):
	ASSISTANT = '1'
	SENIOR = '2'
	DOCENT = '3'
	PROFESSOR = '4'
	HEAD = '5'
	position = (
		(ASSISTANT, 'ассистент'),
		(SENIOR, 'старший преподаватель'),
		(DOCENT, 'доцент'),
		(PROFESSOR, 'профессор'),
		(HEAD, 'зав.каф')
	)
	position_name = models.CharField('Должность:', choices=position, default=ASSISTANT, max_length=22)
	last_name_D = models.CharField('Фамилия:', max_length=25)
	first_name_D = models.CharField('Имя:', max_length=15)
	patronymic = models.CharField('Отчество:', max_length=25, null=True)
	user = models.OneToOneField(User)

	def __str__(self):
		template = '{0.last_name_D} {0.first_name_D} {0.patronymic}'
		return template.format(self)

	class Meta(object):
		ordering = ['last_name_D']
		verbose_name = 'Научный руководитель'
		verbose_name_plural = 'Научные руководители'


class Topic(models.Model):
	topic_name = models.CharField('Название темы:', max_length=300)
	director_id = models.ForeignKey(ScientificDirector, on_delete=models.CASCADE)

	def __str__(self):
		return self.topic_name

	class Meta(object):
		ordering = ['director_id']
		verbose_name = 'Тема ВКР'
		verbose_name_plural = 'Темы ВКР'


class Application(models.Model):
	PENDING = '1'
	REJECTED = '2'
	ACCEPTED = '3'
	status = (
		(PENDING, 'Заявка в рассмотрении'),
		(REJECTED, 'Заявка отклонена'),
		(ACCEPTED, 'Заявка принята')
	)
	status_name = models.CharField('Статус заявки:', choices=status, default=PENDING, max_length=20)
	created_at = models.DateField(auto_now_add=True)
	student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
	topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)

	def __str__(self):
		template = '{0.status_name} {0.created_at}'
		return template.format(self)

	class Meta(object):
		ordering = ['created_at']
		verbose_name = 'Заявки'
		verbose_name_plural = 'Заявки'
