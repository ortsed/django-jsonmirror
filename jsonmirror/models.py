from django.db import models


class JSON_Archive_Set(models.Model):
	
	class Meta:
	
		verbose_name = "JSON Archive Set"

	name = models.CharField(max_length=255, null=False, blank=False)
	
	url = models.URLField("Feed URL", help_text="URL of JSON feed", unique=True)
	
	date_updated = models.DateTimeField("Last updated", null=True, blank=True)
	
	def __unicode__(self):
		return self.name


class JSON_Archive(models.Model):

	class Meta:
	
		verbose_name = "JSON Archive"

	set = models.ForeignKey("JSON_Archive_Set", blank=False, null=False)

	external_id = models.CharField(max_length=1000, null=False, blank=False)
	
	content = models.TextField(blank=True, null=False)
	
	unique_together=("external_id", "set")
	
	parsed = models.BooleanField(default=False)
	
	def __unicode__(self):
		return u"%s - %s" % (self.set.name, self.external_id)
	