```dataview
LIST rows.file.link
FROM #summer2026 AND (#math OR #physics)
GROUP BY choice(contains(file.tags, "#math"), "Calculus 3", "Physics Notes") AS Subject

```



#moc #school 