# GtkAda Map Editor Design Basis

The Forge Map Editor is intentionally smaller than Tiled, but borrows proven workflow ideas:

- A central map canvas with pan and zoom.
- A tile palette and paint tools.
- Separate tile, object, and trigger layers.
- A context-sensitive properties inspector.
- Selection, movement, custom properties, shortcuts, undo/redo, validation, and export.

GtkAda coverage includes hierarchical window composition, signals and callbacks, widget models, drawing with Cairo, file and error dialogs, Gtk.Builder/Glade-style XML, background work with safe main-loop handoff, custom composite widgets, and application packaging.

Reference families used while designing the curriculum:

- AdaCore GtkAda User's Guide and Reference Manual.
- Alire crate pages for gtkada, sdlada, and aunit.
- Tiled documentation for layers, objects, tile painting, custom properties, and map editing shortcuts.
