from __future__ import absolute_import

try:
    # raise ImportError
    from libsourcemap import View, Index, IndexedSourceMap

    # until libsourcemap raises on an index that can't be flattened.
    def from_json(buffer):
        try:
            return View.from_json(buffer)
        except IndexedSourceMap:
            return Index.from_json(buffer).into_view()

except ImportError:
    from .native import from_json  # NOQA
