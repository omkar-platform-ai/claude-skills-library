# Obsidian Bases — Worked Examples

Complete, copy-friendly `.base` files for common patterns. Each example
includes filters, formulas, properties, and views in a single file.

## Task Tracker

Tracks notes tagged `#task` with a `status` and `priority` property.

```yaml
filters:
  and:
    - file.hasTag("task")
    - 'file.ext == "md"'

formulas:
  days_until_due: 'if(due, (date(due) - today()).days, "")'
  is_overdue: 'if(due, date(due) < today() && status != "done", false)'
  priority_label: 'if(priority == 1, "High", if(priority == 2, "Med", "Low"))'

properties:
  status:
    displayName: Status
  formula.days_until_due:
    displayName: "Days Until Due"
  formula.priority_label:
    displayName: Priority

views:
  - type: table
    name: "Active Tasks"
    filters:
      and:
        - 'status != "done"'
    order:
      - file.name
      - status
      - formula.priority_label
      - due
      - formula.days_until_due
    groupBy:
      property: status
      direction: ASC
    summaries:
      formula.days_until_due: Average

  - type: table
    name: "Completed"
    filters:
      and:
        - 'status == "done"'
    order:
      - file.name
      - completed_date
```

## Reading List

Notes tagged `#book` or `#article` with status tracking.

```yaml
filters:
  or:
    - file.hasTag("book")
    - file.hasTag("article")

formulas:
  reading_time: 'if(pages, (pages * 2).toString() + " min", "")'
  status_icon: 'if(status == "reading", "R", if(status == "done", "D", "T"))'
  year_read: 'if(finished_date, date(finished_date).year, "")'

properties:
  author:
    displayName: Author
  formula.status_icon:
    displayName: ""
  formula.reading_time:
    displayName: "Est. Time"

views:
  - type: cards
    name: "Library"
    order:
      - cover
      - file.name
      - author
      - formula.status_icon
    filters:
      not:
        - 'status == "dropped"'

  - type: table
    name: "Reading List"
    filters:
      and:
        - 'status == "to-read"'
    order:
      - file.name
      - author
      - pages
      - formula.reading_time
```

## Daily Notes Index

Lists notes that live in `Daily Notes/` with `YYYY-MM-DD` filenames.

```yaml
filters:
  and:
    - file.inFolder("Daily Notes")
    - '/^\d{4}-\d{2}-\d{2}$/.matches(file.basename)'

formulas:
  word_estimate: '(file.size / 5).round(0)'
  day_of_week: 'date(file.basename).format("dddd")'

properties:
  formula.day_of_week:
    displayName: "Day"
  formula.word_estimate:
    displayName: "~Words"

views:
  - type: table
    name: "Recent Notes"
    limit: 30
    order:
      - file.name
      - formula.day_of_week
      - formula.word_estimate
      - file.mtime
```

## Project Dashboard

Filters notes tagged `#project` and surfaces status + owner.

```yaml
filters:
  and:
    - file.hasTag("project")

formulas:
  age_days: '(today() - date(start_date)).days'
  status_emoji: 'if(status == "shipped", "S", if(status == "blocked", "B", "I"))'

properties:
  owner:
    displayName: Owner
  formula.age_days:
    displayName: "Age (days)"

views:
  - type: table
    name: "Active Projects"
    filters:
      not:
        - 'status == "shipped"'
    order:
      - file.name
      - owner
      - status
      - formula.age_days
    groupBy:
      property: owner
      direction: ASC

  - type: cards
    name: "All Projects"
    order:
      - file.name
      - status
      - formula.status_emoji
```

## Reference Library

Filters notes tagged `#reference`, groups by topic.

```yaml
filters:
  and:
    - file.hasTag("reference")

properties:
  topic:
    displayName: Topic
  source:
    displayName: Source

views:
  - type: table
    name: "All References"
    order:
      - file.name
      - topic
      - source
    groupBy:
      property: topic
      direction: ASC

  - type: list
    name: "Quick List"
    order:
      - file.name
      - topic
```

## Meetings Log

Notes tagged `#meeting` with a date property.

```yaml
filters:
  and:
    - file.hasTag("meeting")

formulas:
  days_ago: '(today() - date(meeting_date)).days'

properties:
  meeting_date:
    displayName: Date
  attendees:
    displayName: Attendees
  formula.days_ago:
    displayName: "Days Ago"

views:
  - type: table
    name: "Recent Meetings"
    limit: 25
    order:
      - file.name
      - meeting_date
      - formula.days_ago
      - attendees
```

## Map View (Location-Tagged Notes)

Requires lat/lng properties and the Maps community plugin.

```yaml
filters:
  and:
    - 'lat != null'
    - 'lng != null'

properties:
  location:
    displayName: Location

views:
  - type: map
    name: "Locations"
```

## Embedding a Base in a Note

Reference a `.base` file from inside a Markdown note:

```markdown
![[Projects.base]]

![[Projects.base#Active Projects]]
```

The first form embeds the whole base; the second embeds a single named view.
