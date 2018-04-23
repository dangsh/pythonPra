from django.db import models

# Create your models here.
class BxSlider(models.Model):
    status_choice = (
        (0 , '下线'),
        (1 , '上线'),
    )
    status = models.IntegerField(choices = status_choice , default=1)
    name = models.CharField(max_length=32 , db_index=True , unique=True)
    img = models.ImageField(upload_to='./static/images/focus/')
    href = models.CharField(max_length=256)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'BxSlider'
        verbose_name_plural = '首页轮播'

    def __str__(self):
        return self.name

