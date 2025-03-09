---
# Required fields
title: "[Your Idea Name]"  # The name of your idea
description: "[A clear and concise description of your idea]"  # Brief introduction about your idea
tags:  # At least one tag is required
  - "[Tag1, e.g., DeFi, NFT, DAO]"  # Main category
  - "[Tag2]"  # Additional categories if applicable
contributors:  # At least one contributor is required
  - name: "[Your Name]"  # Your name
    github: "[Your GitHub Username]"  # Your GitHub username

# Optional fields
links:  # Optional related links
  - title: "[Link Title]"  # Description of the link
    url: "[URL]"  # The actual URL
status: "[ideation/in-progress/completed]"  # Current status of the idea
estimated_time: "[Time estimate]"  # Estimated time to implement
difficulty: "[easy/medium/hard]"  # Implementation difficulty
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
