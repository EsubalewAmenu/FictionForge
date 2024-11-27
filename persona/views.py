from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Persona, Query
from .serializers import PersonaSerializer, QuerySerializer

class PersonaListView(APIView):
    def get(self, request):
        personas = Persona.objects.all()
        serializer = PersonaSerializer(personas, many=True)
        return Response(serializer.data)

class QueryView(APIView):
    def post(self, request):
        data = request.data
        persona = Persona.objects.get(id=data['persona_id'])
        user_query = data['user_query']

        # Dummy response for now
        generated_response = f"This is a {persona.name} response for: {user_query}"

        # Save the query
        query = Query.objects.create(
            persona=persona,
            user_query=user_query,
            generated_response=generated_response
        )
        serializer = QuerySerializer(query)

        return Response(serializer.data)