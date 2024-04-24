def custom_selector(tag):
    """Custom tag selector for 'span' with specific class names."""
    return tag.name == 'span' and tag.has_attr('class') and 'target_span' in tag.get('class')
