---
# Required fields
title: "Web3 Idea Example"
description: "This is a great idea for the Web3 space."
tags:
  - "DeFi"
  - "Innovation"
contributors:
  - name: "LXDAO Contributor"
    github: "lxdao-contributor"

# Optional fields
links:
  - title: "Link1 Description"
    url: "https://example.com"
  - title: "Link2 Description"
    url: "https://another-example.com"
status: "ideation"
estimated_time: "3 months"
difficulty: "medium"
---

# 💡 {{title}}

## 📝 Description
{{description}}

## 🏷️ Tags
{% for tag in tags %}
- {{tag}}
{% endfor %}

## 👥 Contributors
{% for contributor in contributors %}
- {{contributor.name}} (GitHub: [@{{contributor.github}}](https://github.com/{{contributor.github}}))
{% endfor %}

{% if links %}
## 🔗 Related Links
{% for link in links %}
- [{{link.title}}]({{link.url}})
{% endfor %}
{% endif %}

{% if status or estimated_time or difficulty %}
## 📊 Additional Information
{% if status %}- Status: {{status}}{% endif %}
{% if estimated_time %}- Estimated Time: {{estimated_time}}{% endif %}
{% if difficulty %}- Difficulty: {{difficulty}}{% endif %}
{% endif %}