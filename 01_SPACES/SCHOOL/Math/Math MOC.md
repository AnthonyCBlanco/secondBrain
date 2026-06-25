```dataview
LIST rows.file.link FROM #math GROUP BY choice(contains(file.tags, "#math/calculus"), "Calculus", choice(contains(file.tags, "#phys"), "Physics Notes", choice(contains(file.tags, "#linearalgebra"), "Linear Algebra", choice(contains(file.tags, "#diffq"), "Differential Equations", "General Math")))) AS Subject
```
