from import_export.widgets import ForeignKeyWidget


class LocalityForeignKeyWidget(ForeignKeyWidget):
    def clean(self, value, row=None, *args, **kwargs):
        if value:
            return self.get_queryset(value, row, *args, **kwargs).get(
                name=row['locality'],
                verbatim_locality=row['verbatimLocality']
            )
        else:
            return None
