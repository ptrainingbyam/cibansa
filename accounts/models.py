from django.db import models
from django.contrib.auth.models import  AbstractBaseUser,PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class User(AbstractBaseUser,PermissionsMixin):
    USERNAME_FIELD ="email";
    REQUIRED_FIELDS= []

    email = models.EmailField(_('email address'), max_length=254, unique=True, db_index=True)
    username = models.CharField(_('username'),max_length=500,blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now())

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table="cb_user"

    def get_full_name(self):
        return self.profile.get_full_name()

    def get_short_name(self):
        return self.username

    def __str__(self):
        return "%s" % (self.get_full_name())



def photo_upload_path(instance,filename):
    return "".join(["%s%s%s%s" %("profile-photo/",str(instance.first_name),str(instance.last_name),"/"),filename])


class CbUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=16,null=True)
    dob = models.DateField(blank=True, null=True)
    country =models.CharField(max_length=2,null=True,blank=True)
    city=models.CharField(null=True,blank=True,max_length=50)

    gender = models.CharField(max_length=10, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    avatar= models.ImageField(blank=True, default="default_avatar.jpg", upload_to=photo_upload_path)
    has_photo = models.BigIntegerField(default=0,null=True)

    def get_full_name(self):
        return "%s %s" %(self.first_name,self.last_name)

    def get_short_name(self):
        return "%s" %(self.first_name)

    class Meta:
         # managed = False
        db_table = 'cb_user_profile'


