def parse_graph_text(text, graph=None, head=None):
    """Parse a graph description in the strict format:

    Parent:Children;Parent2:Children2

    - Definitions separated by `;` (or newlines)
    - Each definition must contain a single-character Parent, a colon, then contiguous Children characters
      (spaces around tokens are allowed but commas are NOT allowed)
    - Example: `A:BC;B:PO` -> A->B, A->C and B->P, B->O

    Returns (graph, head) where graph is a dict and head is the first declared parent if head was None.
    """
    if graph is None:
        graph = {}

    if not text or not text.strip():
        return graph, head

    parts = [p.strip() for p in text.replace('\n', ';').split(';') if p.strip()]
    first_parent = None

    for part in parts:
        # require colon
        if ':' not in part:
            raise ValueError("Invalid format: each definition must be Parent:Children (e.g. A:BC)")

        parent_raw, children_raw = part.split(':', 1)
        parent = parent_raw.strip().upper()
        if not parent or len(parent) != 1:
            raise ValueError('Parent must be a single character')

        # children: remove spaces but do not allow commas
        children_clean = children_raw.replace(' ', '')
        if ',' in children_clean:
            raise ValueError("Invalid children separator: do not use commas; use contiguous characters (e.g. 'BC')")

        # children may be empty to declare a node without children
        if children_clean == '':
            children = []
        else:
            children = [c.upper() for c in children_clean]

        # merge into graph, avoiding duplicates and self-edges
        if not children:
            if parent not in graph:
                graph[parent] = []
        else:
            if parent not in graph:
                graph[parent] = []
            for c in children:
                if c != parent and c not in graph[parent]:
                    graph[parent].append(c)

        if first_parent is None:
            first_parent = parent

    if head is None and first_parent is not None:
        head = first_parent

    return graph, head


def graph_maker():
    graph = {}
    head = None
    print("GRAPH CREATOR")
    print("------------------------------")
    print("Enter graph definitions in the format: A:BC;B:PO")
    print("- Definitions separated by ';' or newlines")
    print("- Parent must be a single character; children are contiguous characters (no commas)")
    print("Type 'Done' to finish and return the graph")
    print("------------------------------")

    while True:
        print("Current graph:", graph)
        text = input("")
        if text.lower().strip() == 'done':
            break

        try:
            graph, head = parse_graph_text(text, graph, head)
        except ValueError as e:
            print(f"Parse error: {e}")
            continue

    return [graph, head]


def graph_maker_gui(widgets, callback):
    """GUI helper: reads the entry widget and calls callback(graph, head).

    Expects `widgets` to contain "DFSGraphEntry" and "DFSGraphEntryText" keys.
    """
    widgets["DFSGraphEntry"].place(relx=0.5, rely=0.3, anchor="center")
    widgets["DFSGraphEntryText"].place(relx=0.5, rely=0.2, anchor="center")

    def on_enter(widgets):
        widgets["DFSGraphEntry"].place_forget()
        text = widgets["DFSGraphEntry"].get()
        try:
            graph, head = parse_graph_text(text)
        except ValueError as e:
            print(f"Parse error: {e}")
            return
        callback(graph, head)

    widgets["DFSGraphEntry"].bind("<Return>", lambda event: on_enter(widgets))


if __name__ == "__main__":
    g, h = graph_maker()
    print('Result:', g, h)
