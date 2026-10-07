# Meeting Notes — {{ meeting_title }}

**Date:** {{ meeting_date }}
**Facilitator:** {{ facilitator_name }}
**Location:** {{ meeting_location }}
**Type:** {{ meeting_type }}

---

## Attendees

{{ attendees }}

---

## Agenda

{{ agenda }}

---

## Discussion

{{ discussion_summary }}

{% if meeting_type == 'workshop' %}
### Workshop Materials

{{ workshop_materials }}
{% endif %}

{% if meeting_type == 'review' %}
### Items Reviewed

{{ items_reviewed }}
{% endif %}

---

## Action Items

{% for item in action_items %}
- **{{ item.description }}** — Assigned to: {{ item.assignee }}, Due: {{ item.due_date }}
{% endfor %}

---

{% if decisions_made %}
## Decisions

{{ decisions }}

{% endif %}

{% if include_next_meeting %}
## Next Meeting

**Date:** {{ next_meeting_date }}
**Topic:** {{ next_meeting_topic }}
{% else %}
*No follow-up meeting scheduled.*
{% endif %}

---

*Notes recorded by {{ recorder_name }}.*
