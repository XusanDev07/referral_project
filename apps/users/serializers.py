from rest_framework import serializers
from .models import User


class PhoneSerializer(serializers.Serializer):
    phone_number = serializers.CharField()


class VerifyCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    code = serializers.CharField()


class ProfileSerializer(serializers.ModelSerializer):
    referrals = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['phone_number', 'invite_code', 'used_invite_code', 'referrals']

    def get_referrals(self, obj):
        return User.objects.filter(used_invite_code=obj.invite_code).values_list('phone_number', flat=True)


class InviteCodeInputSerializer(serializers.Serializer):
    code = serializers.CharField()
