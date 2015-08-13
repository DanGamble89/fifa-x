from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import DetailView


class ObjectDetailView(DetailView):
    def pagination(self, queryset, page_count=28):
        # Create pagination for the players return
        paginator = Paginator(queryset, page_count)

        # Get the page from the URL
        page = self.request.GET.get('page')

        try:
            # Deliver the requested page
            pagination = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            pagination = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            pagination = paginator.page(paginator.num_pages)

        return pagination
