# -*- coding: utf-8 -*-
import itsdangerous


class EmailDeserializer(object):
    def deserialize_token_to_email(self, key, token):
        serializer = itsdangerous.URLSafeSerializer(key)
        email = serializer.loads(token)
        return email
