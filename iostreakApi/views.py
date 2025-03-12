from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import contactUs
from .serializer import ContactUsSerializer
import re


class ContactUsView(APIView):

    def get(self, request):
        """Fetch all contact form submissions."""
        queryset = contactUs.objects.all()
        serializer = ContactUsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Submit the contact form with proper validation."""
        serializer = ContactUsSerializer(data=request.data)

        if serializer.is_valid():
            # Extract and validate data
            name = serializer.validated_data.get('Name')
            email = serializer.validated_data.get('Email')
            subject = serializer.validated_data.get('Subject')
            message = serializer.validated_data.get('Message')

            # Name Validation
            if not name or len(name) < 2:
                return Response({"error": "Name must be at least 2 characters long."}, status=status.HTTP_400_BAD_REQUEST)

            # Email Validation
            email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if not re.match(email_regex, email):
                return Response({"error": "Invalid email format."}, status=status.HTTP_400_BAD_REQUEST)

            # Subject Validation
            if not subject or len(subject) < 3:
                return Response({"error": "Subject must be at least 3 characters long."}, status=status.HTTP_400_BAD_REQUEST)

            # Message Validation
            if not message or len(message) < 10:
                return Response({"error": "Message must be at least 10 characters long."}, status=status.HTTP_400_BAD_REQUEST)

            # Save the valid data to the database
            serializer.save()

            return Response({"message": "Form submitted successfully!"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
