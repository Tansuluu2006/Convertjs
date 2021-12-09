from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe


class Category(MPTTModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True, upload_to="category/")
    status = models.CharField(max_length=10, choices=STATUS, default=True)
    slug = models.SlugField(null=True, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    class MPTTMeta:
        order_insertion_by = ['title']
        
    
    class Meta:
        verbose_name_plural = "Категории"


class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    title = models.CharField(max_length=150, unique=True, verbose_name="Заговолок")
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True, upload_to="product/")
    price = models.DecimalField(max_digits=12, decimal_places=2)
    detail = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS, default=True, verbose_name="Статус")
    slug = models.SlugField(null=True, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50px">'.format(self.image.url))
    image_tag.short_description = 'Фото'
    
    class Meta:
        verbose_name_plural = "Товары"


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # many to one
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"id: {self.id} -------- товар: {self.product}"
    
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="80px">'.format(self.image.url))
    image_tag.short_description = 'Фото'
    
    class Meta:
        verbose_name_plural = "Картинки"


class Comment(models.Model):
    pass