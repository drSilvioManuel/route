from django.db import models

# Create your models here.


class Street(models.Model):
    name = models.CharField(max_length=255, unique=True)

    @staticmethod
    def prepare_name(name: str) -> str:
        return name.strip().lower().replace(r'\n+', ' ').capitalize()


class Route(models.Model):
    start = models.ForeignKey(Street, on_delete=models.CASCADE, related_name='start_street')
    destination = models.ForeignKey(Street, on_delete=models.CASCADE, related_name='destination_street')
    name = models.TextField()

    class Meta:
        unique_together = (('start', 'destination'),)

    @staticmethod
    def prepare_name(start: str, destination: str) -> str:
        return start + ';' + destination


class Path(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    path_index = models.BigIntegerField(null=False, default=None)
    path_text = models.TextField(null=False, default=None)

    class Meta:
        unique_together = (('route', 'path_index'),)

    @staticmethod
    def prepare_path_index(path_text: str) -> int:
        return hash(path_text)

    @staticmethod
    def prepare_path_text(streets: list) -> str:
        return ';'.join(map(str, streets))
