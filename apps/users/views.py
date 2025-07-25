import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import (
    PhoneSerializer, VerifyCodeSerializer,
    ProfileSerializer, InviteCodeInputSerializer
)

TEMP_CODES = {}


class SendCodeView(APIView):
    def post(self, request):
        serializer = PhoneSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data['phone_number']
            code = '1234'
            TEMP_CODES[phone] = code
            time.sleep(2)
            return Response({"message": "OTP send successfully!"}, status=200)
        return Response(serializer.errors, status=400)


class VerifyCodeView(APIView):
    def post(self, request):
        serializer = VerifyCodeSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data['phone_number']
            code = serializer.validated_data['code']
            if TEMP_CODES.get(phone) == code:
                user, created = User.objects.get_or_create(phone_number=phone)
                user.is_verified = True
                user.save()
                return Response({"message": "Coniform!"}, status=200)
            return Response({
                "error": 'Code not match or expired'
            }, status=400)
        return Response(serializer.errors, status=400)


class ProfileView(APIView):
    def get(self, request):
        phone = request.query_params.get('phone')
        if not phone:
            return Response({
                'error': 'Phone number is required'
            }, status=400)
        try:
            user = User.objects.get(phone_number=phone)
            serializer = ProfileSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)


class UseInviteCodeView(APIView):
    def post(self, request):
        phone = request.query_params.get('phone')
        try:
            user = User.objects.get(phone_number=phone)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

        if user.used_invite_code:
            return Response({
                'message': 'You have already used an invite code'
            }, status=400)

        serializer = InviteCodeInputSerializer(data=request.data)
        if serializer.is_valid():
            code = serializer.validated_data['code']
            if User.objects.filter(invite_code=code).exists():
                user.used_invite_code = code
                user.save()
                return Response({
                    'message': 'Invite code applied successfully!'
                })
            return Response({'error': 'Code not found'}, status=404)
        return Response(serializer.errors, status=400)
