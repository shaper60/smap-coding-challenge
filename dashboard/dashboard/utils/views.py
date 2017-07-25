from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .decorators import default_context
from .breadcrumbs import BreadcrumbList


class BreadcrumbMixin(object):
    def dispatch(self, *args, **kwargs):
        if hasattr(self, 'breadcrumbs'):
            kwargs['context'].update({
                'breadcrumbs': BreadcrumbList(self.breadcrumbs)
            })
        return super(BreadcrumbMixin, self).dispatch(*args, **kwargs)


class AdminViewMixin(BreadcrumbMixin):
    @method_decorator(default_context)
    def dispatch(self, *args, **kwargs):
        return super(BreadcrumbMixin, self).dispatch(*args, **kwargs)

def paginate(request, obj, per):
    paginator = Paginator(obj, per)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj