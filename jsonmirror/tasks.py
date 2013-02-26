from django.conf import settings
from jsonmirror.models import JSON_Archive, JSON_Archive_Set

import urllib, json
from datetime import datetime

JSON_OBJECT_ID_FIELD = getattr(settings, "JSON_OBJECT_ID_FIELD", "id")

def update_all_json_feeds():
	sets = JSON_Archive_Set.objects.all()
	for set in sets:
		update_json_feed(set)

def update_json_feed(json_archive_set):
	
	f = urllib.urlopen(json_archive_set.url)
	contents = f.read()
	f.close()
	

	contents_parsed = json.loads(contents)
	
	# checking for different JSON setups
	if isinstance( contents_parsed, list ):
		for content in contents_parsed:
			if isinstance(content, dict):
				json_archive = JSON_Archive()
				json_archive.set = json_archive_set
				json_archive.external_id = content[JSON_OBJECT_ID_FIELD]
				json_archive.content = json.dumps(content)
				json_archive.save()

	
	json_archive_set.date_updated = datetime.now()
	json_archive_set.save()
		

