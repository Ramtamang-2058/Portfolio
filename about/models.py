from django.db import models


def upload_about_picture(instance, filename):
    return "about/pictures/{id}_{host_to}/{filename}".format(host_to=instance.name, filename=filename,
                                                             id=instance.id)


def upload_about_resume(instance, filename):
    return "about/resumes/{id}_{host_to}/{filename}".format(host_to=instance.full_name, filename=filename,
                                                            id=instance.id)


class About(models.Model):
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)


class MySkills(models.Model):
    skill_name = models.CharField(max_length=255, null=True, blank=True)
    skill_rate = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.skill_name


class MyProject(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_about_picture, blank=True, null=True)
    edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MyResume(models.Model):
    file = models.FileField()
