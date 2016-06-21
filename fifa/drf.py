from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'pages': {
                'current': self.page.number,
                'total': self.page.paginator.num_pages
            },
            'count': self.page.paginator.count,
            'results': data
        })
