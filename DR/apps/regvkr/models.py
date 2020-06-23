from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        template = '{0.last_name} {0.first_name}'
        return template.format(self)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    num = models.PositiveIntegerField('Номер зачётной книжки:', unique=True)  # to confirm
    group = models.CharField('Группа:', max_length=8)
    form = (
        ('1', 'бакалавр'),
        ('2', 'магистр'),
    )
    edu_form = models.CharField('Форма обучения:', choices=form, default='1', max_length=10)

    # is_student = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        template = '{0.user} {0.group}'
        return template.format(self)

    class Meta(object):
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    # class ReadonlyMeta:
    #     readonly = ['is_student']


class ScientificDirector(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    position = (
        ('1', 'ассистент'),
        ('2', 'старший преподаватель'),
        ('3', 'доцент'),
        ('4', 'профессор'),
        ('5', 'зав.каф')
    )
    position_name = models.CharField('Должность:', choices=position, default='1', max_length=22)
    patronymic = models.CharField('Отчество:', max_length=25, null=True)

    # is_student = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def __str__(self):
        template = '{0.position_name} {0.user} {0.patronymic}'
        return template.format(self)

    class Meta(object):
        verbose_name = 'Научный руководитель'
        verbose_name_plural = 'Научные руководители'

    # class ReadonlyMeta:
    #     readonly = ['is_student']


class Topic(models.Model):
    topic_name = models.CharField('Название темы:', max_length=300)
    director = models.ForeignKey(ScientificDirector, on_delete=models.CASCADE)
    comment = models.TextField('Примечание:', blank=True, max_length=300)

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
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)

    def __str__(self):
        template = '{0.status_name} {0.created_at}'
        return template.format(self)

    class Meta(object):
        ordering = ['created_at']
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявки'