from django.db import models


class Category(models.Model):
    """
    Model representing a product category.
    Categories can be nested (i.e., sub-categories).
    """
    sub_category = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='subcategory',
        null=True,
        blank=True
    )
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Model representing a product in the store.
    """
    category = models.ManyToManyField(Category, related_name='product')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    price = models.IntegerField()
    description = models.TextField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
