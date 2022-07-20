from rest_framework import serializers
from .models import Post, Category


class PostSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    subcategories = serializers.SerializerMethodField(
        read_only=True, method_name="get_child_categories")
    posts = PostSerializers(many=True)

    class Meta:
        model = Category
        fields = [
            'title',
            'subcategories',
            'posts'
        ]

    def get_child_categories(self, obj):

        serializer = CategorySerializer(
            instance=obj.category.all(),
            many=True
        )
        return serializer.data


# class CategorySerializers(serializers.ModelSerializer):
#     category = serializers.StringRelatedField(many=True)
#     posts = serializers.StringRelatedField(many=True)
#
#     class Meta:
#
#         model = Category
#         fields = ['title', 'category', 'posts']



    # title = serializers.CharField()
    # content = serializers.CharField()
    # time_create = serializers.DateTimeField(read_only=True)
    # time_update =  serializers.DateTimeField(read_only=True)
    # is_published = serializers.BooleanField(default=True)
    # category_id = serializers.IntegerField()

    # def create(self, validated_data):
    #     return Post.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get("title", instance.title)
    #     instance.content = validated_data.get("content", instance.content)
    #     instance.time_update = validated_data.get("time_update", instance.time_update)
    #     instance.is_published = validated_data.get("is_published", instance.is_published)
    #     instance.category_id = validated_data.get("category_id", instance.category_id)
    #     instance.save()
    #     return instance