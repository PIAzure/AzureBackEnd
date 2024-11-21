from apiazure.Modelo.Events import Event
from apiazure.Seralizer.Eventsseralizer import EventSerializer
from apiazure.Modelo.Organization import Organization
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view,permission_classes
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

@api_view(["POST"])
@permission_classes([AllowAny])
def post_event(request) -> Response:
    event = EventSerializer(data=request.data)
    if event.is_valid():
        event.save()
        return Response(data=event.data, status=HTTP_201_CREATED)
    else:
        return Response(data={"msg": "BAD REQUEST"}, status=HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_events(request,email) -> Response:
    events = Event.objects.filter(organizator_id=email)
    events_serializer = EventSerializer(events, many=True)
    return Response(data=events_serializer.data, status=HTTP_200_OK)

@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_events_admin(request) -> Response:
    events = Event.objects.all()
    events_serializer = EventSerializer(events, many=True)
    print(events_serializer.data)
    return Response(data=events_serializer.data, status=HTTP_200_OK)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([AllowAny])
def get_update_delete_event(request, primary_key):
    try:
        event = Event.objects.get(pk=primary_key)
    except Event.DoesNotExist:
        return Response(data={"msg": "Event not found"}, status=HTTP_400_BAD_REQUEST)
    
    if request.method == "GET":
        event_serializer = EventSerializer(event)
        return Response(data=event_serializer.data, status=HTTP_200_OK)

    elif request.method == "PUT":
        event_serializer = EventSerializer(event, data=request.data)
        if event_serializer.is_valid():
            event_serializer.save()
            return Response(data=event_serializer.data, status=HTTP_200_OK)
        else:
            return Response(data={"msg": "BAD REQUEST"}, status=HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        event.delete()
        return Response(data={"msg": "Event deleted successfully"}, status=HTTP_200_OK)
