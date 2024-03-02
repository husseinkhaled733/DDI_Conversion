namespace py menu

struct MenuItem {
    1: required string id,
    2: optional string label,
}

struct Menu {
    1: required string header,
    2: optional list<MenuItem> items,
}
