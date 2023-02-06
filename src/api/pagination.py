from rest_framework.pagination import PageNumberPagination


class DefaultPaginationCLass(PageNumberPagination):
    page_size = 3