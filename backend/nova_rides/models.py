import uuid

from django.db import models



class RidePostings(models.Model):

    id = models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, editable=False)
    created_by = models.CharField()
    created_on = models.DateTimeField(auto_now=True)


    source_location = models.CharField()
    destination_location = models.CharField()
    start_time = models.DateTimeField()


class RideRequests(models.Model):
    id = models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, editable=False)

    created_at = models.DateTimeField(auto_now=True)
    provided_by = models.CharField()

    posting_id = models.ForeignKey(RidePostings, related_name="ride_reqeust", on_delete=models.CASCADE)
    user_accepted = models.BooleanField(default=False)


class RideChats(models.Model):
    id = models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now=True)

    created_by = models.CharField()

    body = models.TextField()

    ride_request_id = models.ForeignKey(RideRequests, related_name="ride_chats", on_delete=models.CASCADE)



