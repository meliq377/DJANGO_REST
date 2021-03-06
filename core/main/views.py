from .models import Post, Category
from .serializers import PostSerializers, CategorySerializer
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsUserOrReadOnly
from rest_framework.pagination import PageNumberPagination


# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers

#     @action(methods=['get'], detail=False)
#     def category(self, request):
#         cats = Category.objects.all()
#         return Response({'cats': [c.name for c in cats]})

class CategoryAPIListPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10000


class CategoryApiList(generics.ListCreateAPIView):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = CategoryAPIListPagination


class PostAPIListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000


class PostApiList(generics.ListCreateAPIView):
    search_fields = ['title', 'content']
    filter_backends = (filters.SearchFilter,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PostAPIListPagination


class PostAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = (IsAuthenticated,)


class PostAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = (IsAdminOrReadOnly,)

# class PostApiView(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         return Response({'posts': PostSerializers(posts, many=True).data})

#     def post(self, request):
#         serializer = PostSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({'post': serializer.data})

#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})

#         try:
#             instance = Post.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})

#         serializer = PostSerializers(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})

#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method  not allowed"})

#         post = Post.objects.get(pk=pk)
#         post.delete()
#         return Response({'post': 'delete post ' + str(pk)})
