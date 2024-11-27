from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Persona, Query
from .serializers import PersonaSerializer, QuerySerializer
from rest_framework import status
from openai import OpenAI
import os

class PersonaListView(APIView):
    def get(self, request):
        personas = Persona.objects.all()
        serializer = PersonaSerializer(personas, many=True)
        return Response(serializer.data)

client = OpenAI(api_key=os.getenv('OPENAI'))

class QueryView(APIView):
    def post(self, request):
        data = request.data
        try:
            persona = Persona.objects.get(id=data['persona_id'])
        except Persona.DoesNotExist:
            return Response({'error': 'Persona not found.'}, status=status.HTTP_404_NOT_FOUND)

        user_query = data.get('user_query', '')

        if not user_query:
            return Response({'error': 'User query is required.'}, status=status.HTTP_400_BAD_REQUEST)

        prompt = f"{persona.description}\nUser: {user_query}\nAssistant:"

        try:

            response = client.chat.completions.with_raw_response.create(
                messages=[{
                    "role": "user",
                    "content": prompt,
                }],
                model="gpt-4o-mini",
            )

            generated_response = response.parse() #response.choices[0].text.strip()
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Save the query and response
        query = Query.objects.create(
            persona=persona,
            user_query=user_query,
            generated_response=generated_response
        )
        serializer = QuerySerializer(query)

        return Response(serializer.data, status=status.HTTP_201_CREATED)