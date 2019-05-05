from nav.models import Path, Route, Street


def handle_uploaded_file(csv_file):
    file_data = csv_file.read().decode("utf-8")
    lines = file_data.split("\n")
    for i, line in enumerate(lines):
        if i == 0:
            continue  # skip header
        line = line.strip()
        street_names = line.split(";")
        if len(street_names) < 3:
            continue

        ids = []
        names = []
        start = None
        destination = None
        for j, street_name in enumerate(street_names):
            street_name = Street.prepare_name(street_name)
            if len(street_name) == 0:
                continue
            if j == 0:
                start, _ = Street.objects.get_or_create(name=street_name)
            elif j == 1:
                destination, _ = Street.objects.get_or_create(name=street_name)
            else:
                street, _ = Street.objects.get_or_create(name=street_name)
                ids.append(street.id)
                names.append(street_name)
        if destination is None or start is None or len(ids) == 0:
            return
        route, _ = Route.objects.get_or_create(start=start,
                                               destination=destination,
                                               name=Route.prepare_name(start.name, destination.name))
        route_path_text = Path.prepare_path_text(names)
        route_path_index = Path.prepare_path_index(route_path_text)

        Path.objects.update_or_create(route=route,
                                      path_index=route_path_index,
                                      path_text=route_path_text)
