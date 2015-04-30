from .utils import safe_decode
from .utils import safe_encode
from .vocabularies import GROUPBY_CRITERIA
from .vocabularies import TEXT_IDX


def set_content_filter(context, event):
    """Set the content filter dictionary on the request, built from request
    parameters to narrow the results of the collection.
    """
    content_filter = {}
    request = event.request
    for val in GROUPBY_CRITERIA.values():
        idx = val['index']
        if idx in request.form:
            if idx == 'Subject':
                # Subject does not accept unicode values
                # https://github.com/plone/Products.CMFPlone/issues/470
                content_filter[idx] = safe_encode(request.form.get(idx))
            else:
                content_filter[idx] = safe_decode(request.form.get(idx))
    if TEXT_IDX in request.form:
        content_filter[TEXT_IDX] = safe_decode(request.form.get(TEXT_IDX))
    event.request['contentFilter'] = content_filter
