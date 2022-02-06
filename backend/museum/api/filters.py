from django_filters import CharFilter, FilterSet


class CollectionAndNameFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')
    collection_code = CharFilter(method='filter_by_collection_code')

    @staticmethod
    def filter_by_collection_code(queryset, _, value):
        return queryset.filter(
            record__collection_code__name__iexact=value
        ).distinct()


class RecordFilter(FilterSet):
    genus = CharFilter(lookup_expr='name__iexact')
    scientific_name = CharFilter(lookup_expr='name__iexact')
    family = CharFilter(lookup_expr='name__iexact')
    collection = CharFilter(
        lookup_expr='name__iexact', field_name='collection_code'
    )
